---
version: "19.0"
app: "Purchase"
app_slug: "purchase"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_58"
item_count: 11
---

# Purchase — Odoo 19.0

## Alternative RFQs

Create multiple alternative RFQs at once using the correct vendor currency and copied analytic distribution from the original RFQ.

## Cancel and delete purchase orders

It is now possible to cancel and delete purchase orders in order to allow the creation of fake orders during testing.

## Forecast-based purchasing

Purchase required quantities from the product catalog based on forecasted demand for upcoming days.

## Group RFQs for vendors

Define for each vendor whether RFQs should be grouped based on the expected arrival date.

## Improved RFQ dashboard and UX

The UX and the Request for Quotation dashboard have been improved.

## Purchase and product units

When purchasing in a unit or packaging that differs from the product unit, the cost in the product unit is displayed beside the cost in the purchase unit in the product catalog.

## Purchase catalog

The Purchase catalog is now more dynamic: it displays suggested quantities on product cards and allows to view forecasted quantities for a specific date range.

## Purchase orders from sales orders

Create purchase orders from sales orders coming from another Odoo database using a dedicated button on the customer portal.

## Remove locked status

The "Done" status of purchase orders has been replaced by a boolean field to lock/unlock a purchase order.

## Unit price smart update

The unit price of order lines will not recompute automatically after being edited manually.

## Upload bill

The purchase team can directly upload a vendor bill from the purchase order regardless of the control policy of the products.
