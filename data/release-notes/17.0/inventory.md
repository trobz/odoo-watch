---
version: "17.0"
app: "Inventory"
app_slug: "inventory"
source_url: "https://www.odoo.com/odoo-17-release-notes#table_of_content_heading_1707731490324_84"
item_count: 20
---

# Inventory — Odoo 17.0

## Autobatch

Autobatch only batches operations in the ready stage.

## FIFO product costs

The cost of FIFO products is now set to the average price of the remaining quantities.

## Flexible reservation

Edit reserved quantities and reserve specific quants.

## Forecast report reservation

Reserving and unreserving from the forecast report affects only the selected product instead of the entire operation.

## Incoterms

Incoterm and location are now included on the delivery slip.

## Lot/serial properties

Lot and serial number properties are displayed on their quants.

## Lots expiry and quantity mass entry

Updated mass entry of lots/serial numbers on receipts to allow expiration dates and quantities. This allows users to include these additional fields when pasting multiple lots/serial numbers for efficient data input.

## MTO/MTS

When the 'Make to Order' (MTO) process is interrupted, items can be reserved from the available stock to ensure the workflow continues.

## New removal strategy: least packages

Added the "Least Packages" force removal strategy that avoids reserving quantities in two packs when the demand is available in one larger pack.

## Operations menu

Find the right operation easily with the revamped operations menu.

## Packaging display on documents

The packaging is now displayed on purchase orders, sales orders, and transfer documents.

## Print at operation type

Print reports automatically at transfer validation. Define which report to print at the level of operation types. If no IoT printer is linked, the report is downloaded instead.

## Product quantity update

Update quantity quickly from the product form.

## Real-time inventory valuation

Default accounts are now pre-configurable from the Accounting app settings. Introduction of a new 'Cost of Production' account that improves production costing and better differentiates work center and employee costs.

## Reception report barcodes

Reception report now includes a barcode for the next step (ex., from pick to pack) to allow quick movements through a workflow with a barcode scanner.

## Replenishment improvements

Filter replenishments by vendor and select a list of products to be replenished to their maximum quantity.

## Reserve / unreserve button

The forecast report reserve / unreserve button now supports multistep routes.

## Revamp pickings

Eliminated the distinction between planned and immediate transfers. A new transfer starts in ready state and can be planned by setting it in draft. Detailed operations of transfer lines allow directly selecting the existing stock.

## Shipping-based routing

Specify shipping method on routes.

## Stock aging report

Monitor product quantity and time spent in inventory to assess dead stock using the new stock aging report.
