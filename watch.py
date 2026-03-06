#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

import re
import sys
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
        "url": "https://www.odoo.com/partners/country/vietnam-232",
        "extract": "partners",
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


def main():
    Path("data").mkdir(exist_ok=True)
    errors = []
    for watch in WATCHES:
        url = watch["url"]
        path = Path(watch["path"])
        print(f"Fetching {url} ...")
        try:
            response = requests.get(url, timeout=30, headers=HEADERS)
            response.raise_for_status()
            html = response.content.decode("utf-8")
            if watch.get("raw"):
                content = html
            elif watch.get("extract") == "partners":
                content = extract_partners(html)
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
