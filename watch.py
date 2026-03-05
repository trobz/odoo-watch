#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

import sys

import requests
from pathlib import Path

WATCHES = [
    {
        "path": "data/odoo_sh_faq.html",
        "url": "https://www.odoo.sh/faq",
    },
    {
        # Use raw RST source for clean diffs
        "path": "data/enterprise_terms.rst",
        "url": "https://raw.githubusercontent.com/odoo/documentation/master/content/legal/terms/enterprise.rst",
    },
    {
        "path": "data/odoo_partners_vietnam.html",
        "url": "https://www.odoo.com/partners/country/vietnam-232",
    },
]

HEADERS = {"User-Agent": "odoo-watch/1.0 (https://github.com/trobz/odoo-watch)"}


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
            path.write_text(response.text, encoding="utf-8")
            print(f"  -> saved to {path}")
        except requests.RequestException as e:
            print(f"  -> ERROR: {e}", file=sys.stderr)
            errors.append(url)

    if errors:
        print(f"\nFailed to fetch {len(errors)} URL(s):", file=sys.stderr)
        for url in errors:
            print(f"  - {url}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
