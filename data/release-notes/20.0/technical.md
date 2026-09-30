---
version: "20.0"
app: "Technical"
app_slug: "technical"
source_url: "https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_77"
item_count: 5
---

# Technical — Odoo 20.0

## Mail: in-body tracking

Tracking values have been removed; the tracking message is now generated on the fly. All features linked to tracking values (burndown charts, stage duration, etc.) have been updated for this new framework. Admins who still need tracking values can install a dedicated module.

## Many-to-one field improvements

Many-to-one fields are now synced with the backend, and adding/removing values has been improved, even with large lists.

## Push notifications

Push notifications are no longer handled by Firebase but rather by in-house Odoo push tools.

## Track source of postings

Mail.mail records now specify the source of their content to ease auditing.

## Tracking user group changes

User group changes are now logged in the user's chatter as well as in the console logs.
