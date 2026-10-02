#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

import argparse
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
from utils import fold_version

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
        "outdir": "data/release-notes",
        "url": "https://www.odoo.com/page/release-notes",
        "extract": "release_notes",
    },
    {
        "outdir": "data/orm-changelog",
        "url": "https://www.odoo.com/documentation/master/developer/reference/backend/orm/changelog.html",
        "extract": "orm_changelog",
    },
]

HEADERS = {"User-Agent": "odoo-watch/1.0 (https://github.com/trobz/odoo-watch)"}

ROOT = Path(__file__).resolve().parent
RELEASE_NOTES_ROOT = ROOT / "data/release-notes"
RELEASE_NOTES_INDEX_URL = "https://www.odoo.com/page/release-notes"
VERSION_HREF_RE = re.compile(r"^/odoo-(\d+)(?:-(\d+))?-release-notes$")


def version_key(version: str) -> tuple:
    """Numeric ordering for `"16.0"`-style versions (string order breaks at 9 vs 10)."""
    return tuple(int(part) for part in version.split("."))


# start at odoo 12.0
RELEASE_NOTES_FLOOR = min(ARCHIVED_PINS, key=version_key)

UNIQUE_RE = re.compile(r"\?unique=[a-zA-Z0-9]+")
RELEASE_NOTE_HREF_RE = re.compile(r"^/odoo-[\d-]+-release-notes$")


def clean_html(html: str) -> str:
    """Parse HTML, remove CSRF tokens and ?unique= cache-busters."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove CSRF hidden inputs
    for tag in soup.find_all("input", {"name": "csrf_token"}):
        tag.decompose()

    # Blank out csrf_token values in inline scripts
    for tag in soup.find_all("script"):
        if tag.string and "csrf_token" in tag.string:
            tag.string.replace_with(
                re.sub(r'csrf_token:\s*"[^"]*"', 'csrf_token: ""', tag.string)
            )

    # Strip ?unique=... from href/src/content/action attributes
    for tag in soup.find_all(True):
        for attr in ("href", "src", "content", "action"):
            val = tag.get(attr)
            if val and "unique=" in val:
                tag[attr] = UNIQUE_RE.sub("", val)

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
                tag[attr] = UNIQUE_RE.sub("", val)
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


TIER_ORDER = {"Gold": 0, "Silver": 1, "Ready": 2}
PARTNER_LINE_RE = re.compile(r"^(?P<name>.*) \[(?P<grade>[^\]]*)\] ")


def sort_partners(content: str) -> str:
    """Sort partner lines by tier then name.

    odoo.com's listing order is unstable between runs; sorting keeps pure
    reorders from showing up as diffs.
    """

    def key(line: str) -> tuple:
        match = PARTNER_LINE_RE.match(line)
        name, grade = (match["name"], match["grade"]) if match else (line, "")
        return (TIER_ORDER.get(grade, len(TIER_ORDER)), name.casefold(), line)

    lines = sorted(content.strip().splitlines(), key=key)
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

    Sole parser of the index markup: `upstream_index` derives the
    fetch scope from this.
    """
    soup = BeautifulSoup(html, "html.parser")
    links = {
        a["href"]
        for a in soup.select("#wrap a[href]")
        if RELEASE_NOTE_HREF_RE.match(a["href"])
    }
    if not links:
        raise ValueError("No /odoo-*-release-notes links found under #wrap")
    return links


def resolve_urls(version: str, index: dict | None = None) -> list[str]:
    major = version.split(".")[0]
    # Wayback machine snapshot for old version
    if version in ARCHIVED_PINS:
        return [ARCHIVED_SNAPSHOT_URL.format(ts=ARCHIVED_PINS[version], major=major)]
    if index and version in index:
        return sorted(index[version])
    # best-effort guess
    _, _, minor = version.partition(".")
    path = major if minor in ("", "0") else f"{major}-{minor}"
    return [f"https://www.odoo.com/odoo-{path}-release-notes"]


def committed_versions() -> list[str]:
    """Versions already present under `data/release-notes/`."""
    if not RELEASE_NOTES_ROOT.is_dir():
        return []
    return sorted(p.name for p in RELEASE_NOTES_ROOT.iterdir() if p.is_dir())


def upstream_index(html: str | None = None) -> dict[str, list[str]]:
    if html is None:
        html = fetch_with_retry(RELEASE_NOTES_INDEX_URL).decode("utf-8")
    index: dict[str, list[str]] = {}
    for href in sorted(release_note_hrefs(html)):
        match = VERSION_HREF_RE.match(href)
        if not match:
            continue
        major, minor = match.groups()
        version = fold_version(int(major), int(minor or 0))
        if version_key(version) < version_key(RELEASE_NOTES_FLOOR):
            continue
        index.setdefault(version, []).append(f"https://www.odoo.com{href}")
    if not index:
        raise ValueError(
            "index page listed release-note links but no parsable versions"
        )
    return index


# NOTE: if odoo edits old release note page, odoo-watch won't catch it, it is presumably intentional -> old version immutable
def versions_to_fetch(index: dict, committed: list[str]) -> list[str]:
    """Newest version always; older ones only when their directory is absent."""
    if not index:
        return []
    committed_set = set(committed)
    newest = max(index, key=version_key)
    fetch = {v for v in index if v == newest or v not in committed_set}
    return sorted(fetch, key=version_key)


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
        print(
            f"  -> {reason}, retrying in {wait:.0f}s (attempt {attempt + 1}/{retries})..."
        )
        time.sleep(wait)
    raise AssertionError("unreachable")


def write_outputs(outputs: dict[Path, str], prune_roots: list[Path]) -> None:
    """Write files to disk

    "Disk" here is the local git working tree that CI already checked out

    Steps:
    1. For each root, pick a hidden sibling folder to use as a scratch
       copy (e.g. root `20.0` gets scratch folder `.20.0.new`), and delete
       that scratch folder if one is already there from a previous failed
       run.
    2. Write every file into its root's scratch folder, not into the real
       root. Nothing under the real root is touched yet.
    3. If any write fails partway through, delete all scratch folders and
       stop. The real roots are untouched, so the previous good files are
       still there.
    4. If every file was written successfully, then for each root: delete
       the real root's current contents and rename the scratch folder to
       take its place.
    """
    shadow_by_root = {root: root.parent / f".{root.name}.new" for root in prune_roots}
    for shadow in shadow_by_root.values():
        shutil.rmtree(shadow, ignore_errors=True)

    try:
        for path, content in sorted(outputs.items()):
            root = None
            for candidate in prune_roots:
                if path == candidate or candidate in path.parents:
                    root = candidate
                    break
            target = shadow_by_root[root] / path.relative_to(root) if root else path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
    except BaseException:
        for shadow in shadow_by_root.values():
            shutil.rmtree(shadow, ignore_errors=True)
        raise

    for root, shadow in shadow_by_root.items():
        shutil.rmtree(root, ignore_errors=True)
        shadow.rename(root)


def watch_key(watch: dict) -> str:
    """Identifier used by `--only` and error messages."""
    return watch.get("path") or watch["outdir"]


def render_orm_changelog(watch: dict) -> tuple[dict[Path, str], list[Path]]:
    url = watch["url"]
    response = fetch_with_retry(url)
    html = response.decode("utf-8")
    outdir = ROOT / watch["outdir"]
    rendered = parse_orm_changelog(html, url)
    stray = sorted(
        rel for rel in rendered if rel.startswith("/") or ".." in Path(rel).parts
    )
    if stray:
        raise ValueError(f"parsed output escapes its outdir: {stray}")
    outputs = {outdir / rel: content for rel, content in rendered.items()}
    prune_roots = [outdir]
    for root in prune_roots:
        if root in outputs:
            raise ValueError(f"prune root {root} must not equal an output path")
    return outputs, prune_roots


def render_release_notes(watch: dict) -> tuple[dict[Path, str], list[Path]]:
    """Fetch scope comes from the live index page: the newest version every
    run, older ones only when their artifact directory is absent
    (`versions_to_fetch`).

    Prune roots are one per fetched version, never the whole release-notes
    root -- otherwise a run that skips an older version would delete its artifacts.
    """
    index = upstream_index(fetch_with_retry(watch["url"]).decode("utf-8"))
    fetch_versions = versions_to_fetch(index, committed_versions())
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
        rendered = (
            parse_release_notes(pages[0][0], version, pages[0][1])
            if len(pages) == 1
            else parse_release_notes_multi(pages, version)
        )
        prefix = f"{version}/"
        version_root = outdir / version
        for rel, content in rendered.items():
            outputs[version_root / rel[len(prefix) :]] = content
        prune_roots.append(version_root)
        if i < len(fetch_versions) - 1:
            # archive.org rate-limits harder than odoo.com's politeness gap.
            time.sleep(2 if version in ARCHIVED_PINS else 1)
    return outputs, prune_roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--only",
        metavar="PATH",
        help="Run only the watch matching this file path or outdir",
    )
    args = parser.parse_args()

    watches = [w for w in WATCHES if not args.only or watch_key(w) == args.only]
    if args.only and not watches:
        print(f"ERROR: no watch found for path {args.only!r}", file=sys.stderr)
        sys.exit(1)

    Path("data").mkdir(exist_ok=True)
    errors = []
    for watch in watches:
        url = watch["url"]
        extract = watch.get("extract")
        print(f"Fetching {url} ...")
        try:
            # Multi-file watches render a whole directory tree.
            if extract == "orm_changelog":
                write_outputs(*render_orm_changelog(watch))
                continue
            if extract == "release_notes":
                write_outputs(*render_release_notes(watch))
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
                        more = extract_partners(
                            fetch_with_retry(paged_url).decode("utf-8")
                        )
                        if not more.strip():
                            print(f"  -> no more results at page {page}, stopping.")
                            break
                        new_lines = [
                            l for l in more.strip().splitlines() if l not in seen_lines
                        ]
                        if not new_lines:
                            print(
                                f"  -> page {page} returned duplicate data, stopping."
                            )
                            break
                        seen_lines.update(new_lines)
                        content = (
                            content.rstrip("\n") + "\n" + "\n".join(new_lines) + "\n"
                        )
                        page += 1
                        time.sleep(1)  # be polite between page fetches
                    else:
                        print(f"  -> reached max_pages={max_pages}, stopping.")
                content = sort_partners(content)
            elif extract == "selector":
                content = extract_selector(html, watch["selector"])
            else:
                content = clean_html(html)
            if watch.get("expect"):
                check_expected(content, watch["expect"])
            path.write_text(content, encoding="utf-8")
            print(f"  -> saved to {path}")
        except (
            FetchError,
            ReleaseNotesError,
            ValueError,
            OSError,
            NotImplementedError,
        ) as e:
            print(f"  -> ERROR: {e}", file=sys.stderr)
            errors.append(url)

    if errors:
        print(f"\nFailed to fetch {len(errors)} URL(s):", file=sys.stderr)
        for url in errors:
            print(f"  - {url}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
