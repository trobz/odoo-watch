---
version: "12.0"
app: "Technical"
app_slug: "technical"
source_url: "http://web.archive.org/web/20241213201014id_/https://www.odoo.com/odoo-12-release-notes"
item_count: 10
---

# Technical — Odoo 12.0

## Robustness

Prevent users from deleting base data like UoM categories or activity types. Prevent users from breaking email templates. Super Admin created to prevent users from breaking admin access rights.

## Action Manager

Action manager refactored. Removed View Manager which is now included in action manager.

## Staging Performance

Optimized the notification process and follower computation.

## Remove Action on Fetchmail

Incoming email servers are no longer linked to a unique model. With aliases and automatic thread creation, emails can create records in various models.

## Fewer Dependencies

Survey doesn't depend on website anymore. Purchases don't depend on stock. UoM has been extracted from products.

## Python Test

Yml tests have been removed and replaced by Python test.

## Bootstrap 4

The UI has been migrated from bootstrap 3.3.7 to bootstrap 4

## Performance Optimization

Translations loaded 10x faster and module installation time reduced 15% by avoiding view validation.

## Translations

Warning messages when updating a mulit-language record have been simplified/reduced. "ZeroClipboard" js lib has been replaced with "Clipboard" js lib.

## Less to SCSS

Migrate less to SCSS.
