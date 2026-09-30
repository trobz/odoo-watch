---
version: "19.0"
app: "Inventory"
app_slug: "inventory"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_45"
item_count: 26
---

# Inventory — Odoo 19.0

## Batches and dispatches

Batches and dispatches have been improved:

- Reorder deliveries from the map view to optimize your route.
- Set scheduled end dates to improve dispatch planning.

## Forecasted report: expired products

The forecasted report shows which products with expiration dates should be removed from stock and excludes non-consumable items from available and forecasted quantities.

## Inventory valuation

Inventory valuation has been simplified and new features have been added, including a new closing interface and support for transfer backdating.

## Late Availability filter

Use the Late Availability filter on transfers and manufacturing orders to view sales orders with products expected to arrive after the delivery date.

## Locations

The location configuration has been simplified and unnecessary virtual locations created by default have been removed.

## Lots and serial numbers

- Navigation from customer serial numbers and lots has been improved to provide direct access to the related information, and the Lot/Serial Number form view has been reworked.
- Define product-specific lot and serial numbers.

## Master Production Scheduler

- Calculate the forecasted demand for future periods using historical data or actual demand in the MPS.
- The Maximum to Replenish field in the Master Production Scheduler has been removed.
- The Master Production Schedule has been improved to:
  - separate direct and indirect demands;
  - easily identify situations where actual demand exceeds forecasts, using the Forecast Too Low filter;
  - handle early arrivals or production completion more accurately when actual replenishment exceeds the suggested amount, forecasted quantities are adjusted accordingly.

## Merge batches or waves

Merge batches or waves with the same operation type.

## Merge packaging with UoM

Product units and product packagings are merged into one simplified model. UoM categories have been removed.

## Multiple routes on sales order lines

Set multiple routes combined on a sales order line (i.e., MTO and Buy) to decide how to replenish the product for that sales order.

## Packages within packages

Create packages that contain other packages.

## Partner in traceability report

Vendor and customer names are displayed directly in the traceability report.

## Physical inventory

The Physical inventory view and its related features have been simplified and improved.

## Product route configuration

Product routes are set automatically when possible (i.e., Buy route for purchase products and Manufacture route for products with bills of materials).

## Products with missing vendors

When a vendor is missing for a product with an MTO route, the default warehouse route is now used to prevent blocking salespeople.

## Products' quantity on hand

Update a product's quantity on hand using a dedicated field on the product form.

## Reordering rules

- Reordering rules now include a horizon setting (set to 365 days by default), a new deadline field showing the latest date to reorder a product before hitting minimum stock, and data previews (e.g. order frequency, average stock) based on past demand and chosen min/max values.
- Reordering rules now use the unit defined on the vendor pricelist or on the bill of material as the default multiple to calculate the quantity to order. The quantity to order can now exceed the maximum quantity when using a multiple to avoid cases where not enough quantity would be ordered due to downward rounding.

## Replenish on Order (MTO) route

Activate the Replenish on Order (MTO) route using a new setting.

## Replenishment view

The replenishment view now displays default values in previously empty columns (e.g., Route, Vendor, etc.). This allows to filter by vendor to quickly identify rules that already use a specific vendor by default and rules that can be changed to use that vendor to fulfill an order.

## Report improvements

The Picking Operation and Delivery Slip reports have been improved.

## Reservation upon adjustment validation

The reservation process is triggered immediately after adjusting inventory to identify the next processable item.

## Suggested quantity to replenish in vendor catalog

Create purchase orders using suggested quantities to purchase from your vendors, based on sales and demand history of your products.

## Update quantity

It is possible to update the product quantity on hand directly from the form view of the product.

## UPS Connector signature required

Configure UPS integration in order to request a signature from the customer.

## Warehouse in traceability report

The warehouse short code is displayed in the traceability report.

## WhatsApp shipping notifications

Send shipping notifications through WhatsApp.
