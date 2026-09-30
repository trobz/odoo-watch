---
version: "20.0"
app: "Inventory"
app_slug: "inventory"
source_url: "https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_104"
item_count: 22
---

# Inventory — Odoo 20.0

## Allocation report

The allocation flow has been improved with the ability to allocate directly from the forecast report and a new design of the allocation report.

## CMR document

Download a CMR (Convention on the Contract for the International Carriage of Goods by Road) from deliveries that is prefilled based on information from the transfer.

## Company-specific customer lead times

Customer lead time for a product can now be different for each company.

## Intercompany flows

Intercompany flows have been improved:

- Use routes to resupply one company from another.
- Deliver a sales order from another company's warehouse (or use another company's pickup points).
- Valuation costs of transferred products are properly transferred between companies.
- Updates of linked sales and purchase orders (price, quantity, etc.) are properly communicated to the other company.

## Inventory at a past date

Use the new date picker in the stock report to consult an improved overview of inventory at a past date that preserves any filters and allows a precise timestamp.

## Inventory valuation: COGS update

When a product's cost changes after it has been delivered/used (for example, via a landed cost, because the bill price was different from the purchase price), the delivery's value (and the invoice cost, when using perpetual accounting) is updated retroactively.

## Landed costs for specific products

Add landed costs to individual products of a transfer.

## Location-specific push routes

Create push routes based on the specific destination of the product. For example, decide your product should follow route A if you receive it in WH/Input/A, and route B if you receive it in WH/Input/B.

## Picking notifications

Subscribe to notifications about a transfer's status.

## Preview Barcode instructions in operation type

Preview the Barcode instructions that are indicated to the operator based on the chosen configurations directly from the operation type.

## Product packaging barcodes

Access and manage product packaging barcodes more easily from the product form.

## Product replenishment

The "Order" and "Order to max" buttons have been consolidated into a single "Order" button in the replenishment dashboard. When reordering products in advance (i.e., selecting products without the "To reorder" filter), the order quantity is calculated as the max quantity minus the forecast quantity.

## Sendcloud: package reference

The package reference from Odoo is now sent to Sendcloud so it can be displayed on the labels of carriers that support package references.

## Sendcloud: pickup points

Pickup points proposed by Sendcloud carriers can now be selected directly from a sales order or a transfer. These can also be corrected after an eCommerce order has been placed.

## Simplified returns

The return wizard has been removed, and the returns process has been simplified.

## Stock aging report

Access a stock aging report from the "Moves Analysis" pivot view.

## Suggested stock levels for reordering rules

Minimum and maximum stock levels for reordering rules are now suggested based on demand history, desired minimum days of coverage, and order frequency.

## Traceability Report

The Traceability Report has been improved to display upstream and downstream lot/serial numbers in a single report. Final lot locations are highlighted, while intermediary locations are dimmed.

## Variant-specific HS codes

HS (harmonized system) codes are now set at the level of product variants.

## Variant-specific packagings

Different packagings can be added for specific variants.

## Vendor purchase reference

The vendor purchase reference now appears on receipt transfers to improve traceability and help warehouse operators identify the vendor from incoming transfers without having to refer to the related purchase order.

## ZPL location barcodes

Location barcode labels are now available in ZPL format.
