#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

import argparse
import re
import sys
import time
from pathlib import Path

import requests
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
        # odoo.com returns 403 on any /partners/<subpath> URL; only the
        # query-param form of the listing is served.
        "url": "https://www.odoo.com/partners?country_id=232",
        "extract": "partners",
        "paginate": True,
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
            tag.string.replace_with(
                re.sub(r'csrf_token:\s*"[^"]*"', 'csrf_token: ""', tag.string)
            )

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


def fetch_with_retry(url: str, retries: int = 3, backoff: float = 10.0) -> requests.Response:
    """Fetch URL with retry on 5xx errors."""
    for attempt in range(retries):
        response = requests.get(url, timeout=(10, 30), headers=HEADERS)
        if response.status_code < 500 or attempt == retries - 1:
            response.raise_for_status()
            return response
        wait = backoff * (2**attempt)
        print(f"  -> HTTP {response.status_code}, retrying in {wait:.0f}s (attempt {attempt + 1}/{retries})...")
        time.sleep(wait)
    response.raise_for_status()
    return response


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
            response = fetch_with_retry(url)
            html = response.content.decode("utf-8")
            if watch.get("raw"):
                content = html
            elif watch.get("extract") == "partners":
                content = extract_partners(html)
                if watch.get("paginate"):
                    seen_lines = set(content.strip().splitlines())
                    page = 2
                    max_pages = watch.get("max_pages", 20)
                    while page <= max_pages:
                        sep = "&" if "?" in url else "?"
                        paged_url = f"{url}{sep}page={page}"
                        print(f"  -> fetching page {page}/{max_pages} ...")
                        resp = fetch_with_retry(paged_url)
                        more = extract_partners(resp.content.decode("utf-8"))
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
            path.write_text(content, encoding="utf-8")
            print(f"  -> saved to {path}")
        except (requests.RequestException, ValueError) as e:
            print(f"  -> ERROR: {e}", file=sys.stderr)
            errors.append(url)

    if errors:
        print(f"\nFailed to fetch {len(errors)} URL(s):", file=sys.stderr)
        for url in errors:
            print(f"  - {url}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
