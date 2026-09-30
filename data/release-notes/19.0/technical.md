---
version: "19.0"
app: "Technical"
app_slug: "technical"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_19"
item_count: 10
---

# Technical — Odoo 19.0

## Cached data

Data fetched during browsing is stored in cache so that subsequent visits to the view load directly from the cache, improving navigation speed.

## Cached translations

Translations are stored in cache with the aim to speed up the display.

## Control panel display

The search, the view switcher, and all elements located at the top of the screen are directly available without waiting for the data load, allowing searches to be directly performed.

## Date format

Display abbreviated dates instead of numeric, i.e., Aug 1, 2025 instead of 08/01/2025.

## Dropdown formatting

Search dropdowns now include basic text formatting to improve readability.

## Import any file format

When importing files with the importer, any file format is allowed in binary fields (available from 18.0).

## Incremental mass edit

When numeric fields are edited en masse in a list, use the addition (+=), subtraction (-=) , multiplication (*=), and division (/=) assignment operators to increment or decrement all values. For example, select all products and type "*=1.1" to increase the prices by 10%.

## New partner autocomplete provider: Dun & Bradstreet

The partner autocomplete service has been revamped to use data from a new provider: Dun & Bradstreet. The functionality and pricing remain the same, but the quality of the data has been drastically improved thanks to the high quality database of D&B (especially for markets outside of Europe).

## Parent record change

When a record's parent record is changed, its property values are logged in the chatter.

## Tracking information for messages sent from list view

Get tracking information for messages sent from the list view.
