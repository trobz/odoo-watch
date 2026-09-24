---
version: "20.0"
app: "Technical"
app_slug: "technical"
source_url: "https://www.odoo.com/odoo-19-1-release-notes#table_of_content_heading_1_19"
item_count: 3
---

# Technical — Odoo 20.0

## Many-to-one field improvements

Many-to-one fields are now synced with the backend, and adding/removing values has been improved, even with large lists.

## Push notifications

Push notifications are no longer handled by Firebase but rather by in-house Odoo push tools.

## Mail: in-body tracking

Tracking values have been removed; the tracking message is now generated on the fly. All features linked to tracking values (burndown charts, stage duration, etc.) have been updated for this new framework. Admins that still need tracking values can get them by installing a dedicated module.
