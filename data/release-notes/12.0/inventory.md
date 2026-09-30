---
version: "12.0"
app: "Inventory"
app_slug: "inventory"
source_url: "http://web.archive.org/web/20241213201014id_/https://www.odoo.com/odoo-12-release-notes"
item_count: 13
---

# Inventory — Odoo 12.0

## Dashboard View and KPIs

The new dashboard view gives an overview of your inventory management. Gives average cycle times and delays and includes information about value coming in and out of stock.

## Push and Pull Rules

Push and pull rules are merged into a single concept, easier to configure.

## Track POs

If the PO has been triggered by a reordering rule, show that reordering rule as source document on the PO (even in cases of multi-step receipts).

## Product Cost

Clearer descriptions of journal items, add more information on journal items created through a change of the cost of the product.

## PDF Reports

Improvement on the batch picking PDF to regroup products to pick per locations. Improvements to the delivery slip, traceability, picking operations, and the production order PDF reports to fit business.

## Visual Representation of Routes

Representation of the routes that apply to the product has been added, to ease configuration and debugging of push and pull rules.

## Carriers Connector

Full integration with BPost and Easypost to support 90 extra carriers.

## Unit of Weight

Define if you work with kilograms or pounds. Useful when working with carrier integrations.

## Transfer Date

Display the date at which the transfer was processed on done transfers. The default scheduled date on pickings is set to today’s date.

## Replenish

A new button appears on stockable products in order to easily replenish your stock.

## Putaway Strategy by Product

Putaway strategies can now be applied per product and not only per product category.

## Exceptions

When there are exceptions to manage, a next activity is logged on the affected document.

## Valuation

Accounting entries are posted automatically when an exchange rate has changed between the invoice and the receipt/delivery dates.
