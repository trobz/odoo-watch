# odoo-watch

Monitors Odoo-related URLs for changes and opens a pull request automatically when content changes.

## Watched URLs

| File | URL |
|------|-----|
| `data/odoo_sh_faq.html` | https://www.odoo.sh/faq |
| `data/enterprise_terms.rst` | https://raw.githubusercontent.com/odoo/documentation/master/content/legal/terms/enterprise.rst |
| `data/odoo_partners_vietnam.html` | https://www.odoo.com/partners/country/vietnam-232 |

## How it works

A GitHub Actions workflow runs every day at 7:00 UTC. It fetches the watched URLs and compares them against the stored snapshots. If any content changed, it:

1. Creates a branch `auto-update/YYYY-MM-DD-HHmmss`
2. Commits the updated files
3. Opens a pull request
4. Auto-merges the pull request

You can also trigger it manually via **Actions > Watch Odoo URLs > Run workflow**.

## Getting notified

To receive notifications when content changes, **watch this repository** on GitHub:

1. Click the **Watch** button at the top of this page
2. Select **All Activity** (or **Custom > Pull requests**) to be notified when a change PR is opened
