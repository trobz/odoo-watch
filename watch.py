#!/usr/bin/env python3
"""Fetch watched URLs and save their content to files for change tracking."""

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
]

HEADERS = {"User-Agent": "odoo-watch/1.0 (https://github.com/trobz/odoo-watch)"}


def main():
    Path("data").mkdir(exist_ok=True)
    for watch in WATCHES:
        url = watch["url"]
        path = Path(watch["path"])
        print(f"Fetching {url} ...")
        response = requests.get(url, timeout=30, headers=HEADERS)
        response.raise_for_status()
        path.write_text(response.text, encoding="utf-8")
        print(f"  -> saved to {path}")


if __name__ == "__main__":
    main()
