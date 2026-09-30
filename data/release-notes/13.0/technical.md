---
version: "13.0"
app: "Technical"
app_slug: "technical"
source_url: "http://web.archive.org/web/20260410095156id_/https://www.odoo.com/odoo-13-release-notes"
item_count: 3
---

# Technical — Odoo 13.0

## Usability

Remove the "datas_fname" field from "ir.attachment", As is needed in forecast, the grid view now supports date time fields.

## Mass Mailing Campaign

The mass_mailing.campaign model was removed to only keep the utm.campaign model. This change implies that mass_mailing.tag and mass_mailing.stage move to the utm model.

## Create_uid Heuristics Improvements

Mail gateway runner user was used to create most documents through incoming emails. We now link document creation and update to users, using the email to make the matching.
