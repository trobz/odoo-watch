---
version: "20.0"
app: "Barcode"
app_slug: "barcode"
source_url: "https://www.odoo.com/odoo-19-3-release-notes#table_of_content_heading_1_27"
item_count: 6
---

# Barcode — Odoo 20.0

## Manufacturing operations

Improvements have been made for manufacturing, including removing irrelevant settings and correcting behavior to ensure that reserved lot/serial numbers of components are shown only if the related setting is active, and that mandatory scans do not prevent editing of by-products.

## Packages: pre-encoded contents

Packages and their contents communicated by the vendor can now be pre-encoded in the backend. When receiving the package, users can scan the package to mark the package and its contents as received.

## Packages: untracked goods

If a package contains untracked goods registered in a previous step, they are included in the contents of the package when it gets scanned in Barcode in later steps.

## Backorders

Choose whether or not to create a backorder from the Barcode app.

## Fixed button positions

Barcode buttons now stay in the same position on the screen, regardless of the entered quantity, to improve usability and reduce errors.

## Inventory count

When doing an inventory count from Barcode, click the pen to manually enter the total counted quantity for a selected product.
