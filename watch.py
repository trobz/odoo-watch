#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

import argparse
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from bs4 import BeautifulSoup

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
]

HEADERS = {"User-Agent": "odoo-watch/1.0 (https://github.com/trobz/odoo-watch)"}

_UNIQUE_RE = re.compile(r"\?unique=[a-zA-Z0-9]+")


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", metavar="PATH", help="Run only the watch matching this file path")
    args = parser.parse_args()

    watches = [w for w in WATCHES if not args.only or w["path"] == args.only]
    if args.only and not watches:
        print(f"ERROR: no watch found for path {args.only!r}", file=sys.stderr)
        sys.exit(1)

    Path("data").mkdir(exist_ok=True)
    errors = []
    for watch in watches:
        url = watch["url"]
        path = Path(watch["path"])
        print(f"Fetching {url} ...")
        try:
            html = fetch_with_retry(url).decode("utf-8")
            if watch.get("raw"):
                content = html
            elif watch.get("extract") == "partners":
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
            elif watch.get("extract") == "selector":
                content = extract_selector(html, watch["selector"])
            else:
                content = clean_html(html)
            if watch.get("expect"):
                check_expected(content, watch["expect"])
            path.write_text(content, encoding="utf-8")
            print(f"  -> saved to {path}")
        except (FetchError, ValueError) as e:
            print(f"  -> ERROR: {e}", file=sys.stderr)
            errors.append(url)

    if errors:
        print(f"\nFailed to fetch {len(errors)} URL(s):", file=sys.stderr)
        for url in errors:
            print(f"  - {url}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
