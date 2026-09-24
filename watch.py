#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from bs4 import BeautifulSoup

from orm_changelog import parse as parse_orm_changelog
from release_notes import (
    ARCHIVED_PINS,
    ARCHIVED_SNAPSHOT_URL,
    ReleaseNotesError,
    parse as parse_release_notes,
    parse_multi as parse_release_notes_multi,
)
from utils import fold_version, normalize_version

WATCHES = [
    {
        "path": "data/odoo_sh_faq.html",
        "url": "https://www.odoo.sh/faq",
        "extract": "selector",
        "selector": "#o-sh-faq",
    },
    {
        # Use raw RST source for clean diffs
        "path": "data/enterprise_terms.rst",
        "url": "https://raw.githubusercontent.com/odoo/documentation/master/content/legal/terms/enterprise.rst",
        "raw": True,
    },
    {
        "path": "data/odoo_partners_vietnam.txt",
        "url": "https://www.odoo.com/partners/country/viet-nam-232",
        "extract": "partners",
        "paginate": True,
        # Every listed partner's link carries the active country filter. If
        # odoo.com ever falls back to geo-IP defaults (it does for the
        # ?country_id= form), this catches it instead of silently saving
        # another country's partners.
        "expect": "country_id=232",
    },
    {
        "path": "data/odoo_status.html",
        "url": "https://status.odoo.com",
    },
    {
        # New-version alarm: one line per /odoo-*-release-notes link. Must run
        # before the release_notes_corpus entry below -- that entry reads the
        # data/release_notes_versions.txt this watch writes.
        "path": "data/release_notes_versions.txt",
        "url": "https://www.odoo.com/page/release-notes",
        "extract": "release_note_links",
    },
    {
        # Per-version release-notes corpus. Ordering-dependent on the entry
        # above: reads data/release_notes_versions.txt, which must already
        # reflect this run's fetch before this entry resolves its fetch set.
        "outdir": "data/release-notes",
        "url": "https://www.odoo.com/page/release-notes",
        "extract": "release_notes_corpus",
    },
    {
        # Single page carries the full ORM history; folded into major versions by the parser.
        "outdir": "data/orm-changelog",
        "url": "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html",
        "extract": "orm_changelog",
    },
]

HEADERS = {"User-Agent": "odoo-watch/1.0 (https://github.com/trobz/odoo-watch)"}

# The two corpus watches and their helpers resolve against the script's own
# directory, so a run from another cwd cannot silently read an empty corpus.
ROOT = Path(__file__).resolve().parent
CORPUS_ROOT = ROOT / "data/release-notes"
RELEASE_NOTES_INDEX_URL = "https://www.odoo.com/page/release-notes"
VERSION_HREF_RE = re.compile(r"^/odoo-(\d+)(?:-(\d+))?-release-notes$")
# Watches that render a whole directory tree instead of one file: they stage,
# validate and move their outputs, and are the only ones `--check` covers.
CORPUS_EXTRACTS = frozenset({"orm_changelog", "release_notes_corpus"})


def version_key(version: str) -> tuple:
    """Numeric ordering for `"16.0"`-style versions (string order breaks at 9 vs 10)."""
    return tuple(int(part) for part in version.split("."))


# Oldest version odoo.com still serves. Its index links 9.0-11.0 too, but those
# pages 404; the archived pins mark where usable history actually starts.
CORPUS_FLOOR = min(ARCHIVED_PINS, key=version_key)

_UNIQUE_RE = re.compile(r"\?unique=[a-zA-Z0-9]+")
_RELEASE_NOTE_HREF_RE = re.compile(r"^/odoo-[\d-]+-release-notes$")


def clean_html(html: str) -> str:
    """Parse HTML, remove CSRF tokens and ?unique= cache-busters."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove CSRF hidden inputs
    for tag in soup.find_all("input", {"name": "csrf_token"}):
        tag.decompose()

    # Blank out csrf_token values in inline scripts
    for tag in soup.find_all("script"):
        if tag.string and "csrf_token" in tag.string:
            tag.string.replace_with(re.sub(r'csrf_token:\s*"[^"]*"', 'csrf_token: ""', tag.string))

    # Strip ?unique=... from href/src/content/action attributes
    for tag in soup.find_all(True):
        for attr in ("href", "src", "content", "action"):
            val = tag.get(attr)
            if val and "unique=" in val:
                tag[attr] = _UNIQUE_RE.sub("", val)

    return str(soup)


def extract_selector(html: str, selector: str) -> str:
    """Extract a single HTML element by CSS selector, stripping ?unique= params."""
    soup = BeautifulSoup(html, "html.parser")
    el = soup.select_one(selector)
    if el is None:
        raise ValueError(f"Selector {selector!r} matched nothing")
    for tag in el.find_all(True):
        for attr in ("href", "src", "content", "action"):
            val = tag.get(attr)
            if val and "unique=" in val:
                tag[attr] = _UNIQUE_RE.sub("", val)
    return el.prettify()


def extract_partners(html: str) -> str:
    """Extract partner list as plain text for clean, focused diffs."""
    soup = BeautifulSoup(html, "html.parser")
    lines = []
    for a in soup.find_all("a", {"aria-label": "Go to reseller"}):
        href = a.get("href", "")
        h5 = a.find("h5")
        name_span = h5.find("span") if h5 else None
        name = name_span.get_text(strip=True) if name_span else "?"
        badge = a.find("span", class_=lambda c: c and "badge" in c)
        grade = badge.get_text(strip=True) if badge else ""
        lines.append(f"{name} [{grade}] {href}")
    return "\n".join(lines) + "\n"


class FetchError(Exception):
    """A URL could not be fetched."""

    def __init__(self, url: str, reason: str):
        super().__init__(f"{reason} for {url}")
        self.reason = reason


def check_expected(content: str, expect: str) -> None:
    """Raise unless every line of content contains expect."""
    bad = [line for line in content.strip().splitlines() if expect not in line]
    if bad:
        msg = f"{len(bad)} line(s) missing {expect!r}, first: {bad[0]!r}"
        raise ValueError(msg)


def release_note_hrefs(html: str) -> set[str]:
    """The `/odoo-*-release-notes` paths linked from the index page's `#wrap`.

    Sole parser of the index markup: both the alarm file and the corpus's fetch
    scope derive from this, so the two can never disagree about what upstream
    publishes.
    """
    soup = BeautifulSoup(html, "html.parser")
    links = {
        a["href"]
        for a in soup.select("#wrap a[href]")
        if _RELEASE_NOTE_HREF_RE.match(a["href"])
    }
    if not links:
        raise ValueError("No /odoo-*-release-notes links found under #wrap")
    return links


def release_note_links(html: str) -> str:
    """New-version alarm file: one `/odoo-*-release-notes` path per line.

    A new Odoo version shows up as a one-line diff -- that is this watch's whole
    purpose.
    """
    links = release_note_hrefs(html)
    return "# DO NOT EDIT manually -- generated by watch.py\n" + "\n".join(sorted(links)) + "\n"


def resolve_urls(version: str, index: dict | None = None) -> list[str]:
    """Source pages for a version: Wayback snapshot when pinned, else the live
    pages the index links to (`index`), else the conventional live URL.

    A version maps to a list rather than one URL because several alpha pages
    fold into one unpublished major -- e.g. `/odoo-19-1..4-release-notes` all
    fold into 20.0, whose own `/odoo-20-release-notes` does not exist yet
    (404). Merging such pages is handled by `release_notes.parse_multi`.
    """
    major = version.split(".")[0]
    if version in ARCHIVED_PINS:
        return [ARCHIVED_SNAPSHOT_URL.format(ts=ARCHIVED_PINS[version], major=major)]
    if index and version in index:
        return sorted(index[version])
    _, _, minor = version.partition(".")
    path = major if minor in ("", "0") else f"{major}-{minor}"
    return [f"https://www.odoo.com/odoo-{path}-release-notes"]


def committed_versions() -> list[str]:
    """Versions already present under `data/release-notes/`."""
    if not CORPUS_ROOT.is_dir():
        return []
    return sorted(p.name for p in CORPUS_ROOT.iterdir() if p.is_dir())


def known_versions() -> list[str]:
    """Archived pins plus every version already committed under the corpus root."""
    return sorted(set(ARCHIVED_PINS) | set(committed_versions()))


def upstream_index(html: str | None = None) -> dict[str, list[str]]:
    """Map each upstream-listed version to the live pages that feed it.

    Parsed from the index markup itself, never from the alarm file the sibling
    watch writes: a stale or absent `data/release_notes_versions.txt` must not
    be able to shrink the corpus's fetch scope to nothing.

    Versions below the oldest archived pin are dropped -- odoo.com serves 404
    for them (verified for 9.0-11.0), which is why the pins exist at all.
    """
    if html is None:
        html = fetch_with_retry(RELEASE_NOTES_INDEX_URL).decode("utf-8")
    index: dict[str, list[str]] = {}
    for href in sorted(release_note_hrefs(html)):
        match = VERSION_HREF_RE.match(href)
        if not match:
            continue
        major, minor = match.groups()
        version = fold_version(int(major), int(minor or 0))
        if version_key(version) < version_key(CORPUS_FLOOR):
            continue
        index.setdefault(version, []).append(f"https://www.odoo.com{href}")
    if not index:
        raise ValueError("index page listed release-note links but no parsable versions")
    return index


def upstream_versions(html: str | None = None) -> list[str]:
    """Versions upstream's release-notes index links to, oldest first."""
    return sorted(upstream_index(html), key=version_key)


def missing() -> list[str]:
    """Upstream-visible versions absent from the committed corpus."""
    committed = set(committed_versions())
    return [v for v in upstream_versions() if v not in committed]


def versions_to_fetch(index: dict, committed: list[str]) -> list[str]:
    """Newest version always; older ones only when their directory is absent."""
    if not index:
        return []
    committed_set = set(committed)
    newest = max(index, key=version_key)
    fetch = {v for v in index if v == newest or v not in committed_set}
    return sorted(fetch, key=version_key)


def diff_outputs(outputs: dict, prune_roots: list) -> bool:
    """Report how freshly rendered outputs differ from the checkout. Writes nothing.

    Same `(outputs, prune_roots)` shape the renderers hand to `commit_outputs`,
    so `--check` exercises exactly the code a real run would write from.
    """
    committed_files = {
        p for root in prune_roots if root.is_dir() for p in root.rglob("*") if p.is_file()
    }
    rendered_files = set(outputs)
    missing_files = sorted(rendered_files - committed_files)
    stale = sorted(committed_files - rendered_files)
    drifted = [
        p for p in sorted(rendered_files & committed_files)
        if p.read_text(encoding="utf-8") != outputs[p]
    ]
    for path in missing_files:
        print(f"  -> MISSING from committed corpus: {path}")
    for path in stale:
        print(f"  -> STALE in committed corpus: {path}")
    for path in drifted:
        print(f"  -> DRIFT: {path}")
    if missing_files or stale or drifted:
        return False
    print(f"  -> OK ({len(rendered_files)} files match)")
    return True


def check_corpus(watch: dict) -> bool:
    """Re-render a corpus watch and diff it against the checkout. Writes nothing.

    Release notes are checked one version per render call rather than in a
    single batch: a version whose page 404s or fails to parse must not hide the
    verdict for every other version.
    """
    ok = True
    if watch.get("extract") == "release_notes_corpus":
        for version in known_versions():
            version = normalize_version(version)
            print(f"Checking release notes {version} ...")
            try:
                outputs, prune_roots = render_release_notes_corpus(watch, versions=[version])
            except (FetchError, ReleaseNotesError, ValueError, OSError, NotImplementedError) as e:
                print(f"  -> ERROR ({type(e).__name__}): {e}", file=sys.stderr)
                ok = False
                continue
            ok = diff_outputs(outputs, prune_roots) and ok
        return ok

    print(f"Checking {watch_key(watch)} ...")
    try:
        outputs, prune_roots = render_orm_changelog(watch)
    except (FetchError, ValueError, OSError) as e:
        print(f"  -> ERROR ({type(e).__name__}): {e}", file=sys.stderr)
        return False
    return diff_outputs(outputs, prune_roots)


def is_retryable(status_code: int) -> bool:
    """Whether a status is worth retrying.

    Besides 5xx, odoo.com's edge intermittently answers 403 ("Request forbidden
    by administrative rules") for requests it serves normally moments later, so
    treat 403 as transient too. 429 is retried for the obvious reason.
    """
    return status_code >= 500 or status_code in (403, 429)


def curl_get(url: str, timeout: int = 60) -> tuple[int, bytes]:
    """GET url via curl, returning (status_code, body).

    curl rather than requests: since 2026-09-17 odoo.com's edge black-holes
    requests carrying urllib3's TLS fingerprint (connection accepted, response
    never sent -> read timeout), while curl to the same URL from the same host
    and User-Agent is served normally.
    """
    with tempfile.NamedTemporaryFile() as body:
        # fixed argv, no shell; curl resolved from PATH (present on CI runners)
        proc = subprocess.run(  # noqa: S603
            [  # noqa: S607
                "curl",
                "--silent",
                "--show-error",
                "--location",
                "--compressed",
                "--max-time",
                str(timeout),
                "--user-agent",
                HEADERS["User-Agent"],
                "--output",
                body.name,
                "--write-out",
                "%{http_code}",
                url,
            ],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise FetchError(url, f"curl exit {proc.returncode}: {proc.stderr.strip()}")
        try:
            status = int(proc.stdout.strip())
        except ValueError:
            raise FetchError(url, "curl returned no status") from None
        return status, Path(body.name).read_bytes()


def fetch_with_retry(url: str, retries: int = 3, backoff: float = 10.0) -> bytes:
    """Fetch URL with retry on transient errors (bad status or network failure)."""
    for attempt in range(retries):
        last = attempt == retries - 1
        try:
            status, body = curl_get(url)
        except FetchError as e:
            if last:
                raise
            reason = str(e)
        else:
            reason = f"HTTP {status}"
            if not is_retryable(status):
                if status >= 400:
                    raise FetchError(url, reason)
                return body
            if last:
                raise FetchError(url, reason)
        wait = backoff * (2**attempt)
        print(f"  -> {reason}, retrying in {wait:.0f}s (attempt {attempt + 1}/{retries})...")
        time.sleep(wait)
    raise AssertionError("unreachable")


def stage_outputs(staging_dir: Path, outputs: dict) -> dict:
    """Write rendered content into the staging tree; return staged -> real paths."""
    staged_map = {}
    for real_path, content in outputs.items():
        staged = staging_dir / real_path.relative_to(ROOT)
        staged.parent.mkdir(parents=True, exist_ok=True)
        staged.write_text(content, encoding="utf-8")
        staged_map[staged] = real_path
    return staged_map


def validate_staged(staged_map: dict, outputs: dict) -> None:
    """Re-read every staged file from disk and compare against its rendered content.

    Reads back rather than trusting the write: this is the only point where a
    truncated or encoding-mangled file is caught before it reaches the checkout.
    """
    for staged, real_path in staged_map.items():
        if not staged.is_file() or staged.read_text(encoding="utf-8") != outputs[real_path]:
            raise ValueError(f"staged content mismatch or missing for {real_path}")


def sync_outputs(staged_map: dict, prune_roots: list) -> None:
    """Move validated staged files into the checkout and prune stale ones.

    `os.replace` rather than a second write: each file lands whole or not at
    all, and the bytes that land are the exact bytes `validate_staged` read.
    The staging tree lives under ROOT so the rename never crosses filesystems.
    """
    real_paths = set(staged_map.values())
    for staged, real_path in sorted(staged_map.items()):
        real_path.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staged, real_path)
    for prune_root in prune_roots:
        for stale in sorted(prune_root.rglob("*")):
            if stale.is_file() and stale not in real_paths:
                stale.unlink()
                print(f"  -> pruned {stale}")
    for prune_root in prune_roots:
        for stale in sorted(prune_root.rglob("*"), reverse=True):
            if stale.is_dir() and not any(stale.iterdir()):
                stale.rmdir()


def commit_outputs(outputs: dict, prune_roots: list) -> None:
    """Stage a corpus watch's rendered files, validate them, then move them in.

    Scoped to the multi-file watches: a half-failed corpus must never leave
    the checkout half-written. Single-file watches keep writing directly.
    """
    staging_dir = Path(tempfile.mkdtemp(prefix=".watch-staging-", dir=ROOT))
    try:
        staged_map = stage_outputs(staging_dir, outputs)
        validate_staged(staged_map, outputs)
        sync_outputs(staged_map, prune_roots)
        print(f"  -> synced {len(outputs)} file(s)")
    finally:
        shutil.rmtree(staging_dir, ignore_errors=True)


def watch_key(watch: dict) -> str:
    """Identifier used by `--only` and error messages."""
    return watch.get("path") or watch["outdir"]


def dump_debug_html(key: str, html: str) -> None:
    """Dump the fetched HTML when ODOO_WATCH_DEBUG_DIR is set (CI artifact)."""
    debug_dir = os.environ.get("ODOO_WATCH_DEBUG_DIR")
    if not debug_dir:
        return
    target = Path(debug_dir)
    target.mkdir(parents=True, exist_ok=True)
    name = key.strip("/").replace("/", "_") + ".html"
    (target / name).write_text(html, encoding="utf-8")
    print(f"  -> dumped fetched HTML to {target / name}", file=sys.stderr)


def render_orm_changelog(watch: dict) -> tuple[dict[Path, str], list[Path]]:
    url = watch["url"]
    response = fetch_with_retry(url)
    html = response.decode("utf-8")
    outdir = ROOT / watch["outdir"]
    try:
        rendered = parse_orm_changelog(html, url)
    except ValueError:
        dump_debug_html(watch_key(watch), html)
        raise
    stray = sorted(rel for rel in rendered if rel.startswith("/") or ".." in Path(rel).parts)
    if stray:
        raise ValueError(f"parsed output escapes its outdir: {stray}")
    outputs = {outdir / rel: content for rel, content in rendered.items()}
    prune_roots = [outdir]
    for root in prune_roots:
        if root in outputs:
            raise ValueError(f"prune root {root} must not equal an output path")
    return outputs, prune_roots


def render_release_notes_corpus(
    watch: dict, versions: list[str] | None = None
) -> tuple[dict[Path, str], list[Path]]:
    """Fetch scope comes from the live index page: the newest version every
    run, older ones only when their artifact directory is absent
    (`versions_to_fetch`). `versions` overrides that scope -- `--check` uses it
    to re-render one known version at a time without writing.

    Prune roots are one per fetched version, never the whole corpus root --
    otherwise a run that skips an older version would delete its artifacts.
    """
    index = None
    if versions is None:
        index = upstream_index(fetch_with_retry(watch["url"]).decode("utf-8"))
        fetch_versions = versions_to_fetch(index, committed_versions())
    else:
        fetch_versions = versions
    outdir = ROOT / watch["outdir"]
    outputs: dict[Path, str] = {}
    prune_roots: list[Path] = []
    for i, version in enumerate(fetch_versions):
        urls = resolve_urls(version, index)
        print(f"  -> fetching release notes {version} ({len(urls)} page(s)) ...")
        pages = []
        for j, page_url in enumerate(urls):
            pages.append((fetch_with_retry(page_url).decode("utf-8"), page_url))
            if j < len(urls) - 1:
                time.sleep(1)  # be polite between an alpha-fold target's pages
        try:
            rendered = (
                parse_release_notes(pages[0][0], version, pages[0][1])
                if len(pages) == 1
                else parse_release_notes_multi(pages, version)
            )
        except ValueError:
            for k, (html, _url) in enumerate(pages):
                dump_debug_html(f"release-notes_{version}_{k}", html)
            raise
        prefix = f"{version}/"
        stray = sorted(rel for rel in rendered if not rel.startswith(prefix))
        if stray:
            raise ValueError(f"parsed output for {version} escapes its version directory: {stray}")
        version_root = outdir / version
        committed_count = sum(1 for p in version_root.rglob("*") if p.is_file()) if version_root.is_dir() else 0
        rendered_count = len(rendered)
        if committed_count and rendered_count < committed_count / 2:
            raise ValueError(
                f"refusing to prune {version_root}: fresh fetch rendered {rendered_count} "
                f"file(s) vs {committed_count} committed -- looks like a partial or "
                f"degraded upstream page, not a real content change"
            )
        for rel, content in rendered.items():
            outputs[version_root / rel[len(prefix):]] = content
        prune_roots.append(version_root)
        if i < len(fetch_versions) - 1:
            # archive.org rate-limits harder than odoo.com's politeness gap.
            time.sleep(2 if version in ARCHIVED_PINS else 1)
    for root in prune_roots:
        if root in outputs:
            raise ValueError(f"prune root {root} must not equal an output path")
    return outputs, prune_roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--only", metavar="PATH", help="Run only the watch matching this file path or outdir"
    )
    parser.add_argument(
        "--missing", action="store_true",
        help="List upstream-visible release-notes versions absent locally; writes nothing",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Re-render the corpus watches fresh and diff against the checkout; "
             "writes nothing, exits 1 on drift. Narrow with --only.",
    )
    args = parser.parse_args()

    watches = [w for w in WATCHES if not args.only or watch_key(w) == args.only]
    if args.only and not watches:
        print(f"ERROR: no watch found for path {args.only!r}", file=sys.stderr)
        sys.exit(1)

    if args.check:
        corpora = [w for w in watches if w.get("extract") in CORPUS_EXTRACTS]
        if not corpora:
            print("ERROR: --check applies to the corpus watches only", file=sys.stderr)
            sys.exit(1)
        results = [check_corpus(w) for w in corpora]
        sys.exit(0 if all(results) else 1)

    if args.missing:
        missing_versions = missing()
        if missing_versions:
            print("Missing from data/release-notes/:")
            for version in missing_versions:
                print(f"  - {version}")
        else:
            print("Nothing missing.")
        return

    Path("data").mkdir(exist_ok=True)
    errors = []
    for watch in watches:
        url = watch["url"]
        extract = watch.get("extract")
        print(f"Fetching {url} ...")
        try:
            # Multi-file watches render a whole corpus; they stage, validate and
            # sync their own outputs rather than writing a single `path`.
            if extract == "orm_changelog":
                commit_outputs(*render_orm_changelog(watch))
                continue
            if extract == "release_notes_corpus":
                commit_outputs(*render_release_notes_corpus(watch))
                continue

            path = Path(watch["path"])
            html = fetch_with_retry(url).decode("utf-8")
            if watch.get("raw"):
                content = html
            elif extract == "partners":
                content = extract_partners(html)
                if watch.get("paginate"):
                    seen_lines = set(content.strip().splitlines())
                    page = 2
                    max_pages = watch.get("max_pages", 20)
                    while page <= max_pages:
                        paged_url = f"{url}/page/{page}"
                        print(f"  -> fetching page {page}/{max_pages} ...")
                        more = extract_partners(fetch_with_retry(paged_url).decode("utf-8"))
                        if not more.strip():
                            print(f"  -> no more results at page {page}, stopping.")
                            break
                        new_lines = [l for l in more.strip().splitlines() if l not in seen_lines]
                        if not new_lines:
                            print(f"  -> page {page} returned duplicate data, stopping.")
                            break
                        seen_lines.update(new_lines)
                        content = content.rstrip("\n") + "\n" + "\n".join(new_lines) + "\n"
                        page += 1
                        time.sleep(1)  # be polite between page fetches
                    else:
                        print(f"  -> reached max_pages={max_pages}, stopping.")
            elif extract == "selector":
                content = extract_selector(html, watch["selector"])
            elif extract == "release_note_links":
                content = release_note_links(html)
            else:
                content = clean_html(html)
            if watch.get("expect"):
                check_expected(content, watch["expect"])
            path.write_text(content, encoding="utf-8")
            print(f"  -> saved to {path}")
        except (FetchError, ReleaseNotesError, ValueError, OSError, NotImplementedError) as e:
            print(f"  -> ERROR: {e}", file=sys.stderr)
            errors.append(url)

    if errors:
        print(f"\nFailed to fetch {len(errors)} URL(s):", file=sys.stderr)
        for url in errors:
            print(f"  - {url}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
