---
version: "13.0"
app: "Inventory"
app_slug: "inventory"
source_url: "http://web.archive.org/web/20260410095156id_/https://www.odoo.com/odoo-13-release-notes"
item_count: 13
---

# Inventory — Odoo 13.0

## Route

Rename the Make to Order route to Replenish on Order for more clarity (as we do not always "make" the product, but we sometimes buy it instead.

## Account

Prevent users from improperly configuring its product categories by raising a warning when the Stock Received/Delivered accounts are the same than the Stock Valuation Account.

## Multi-Company

Add a field company_id on the stock move lines to only show the product moves of the company of the user.

## Product

The description of the product is now visible on the transfers. The description can be adapted based on the type of transfer (delivery, internal or receipt).

## Picking

Assign users to pickings. It can be done picking per picking or in a group (from a list of pickings).

## Delivery

Charge the estimated or the real cost to your customer; Print return labels for DHL, Easypost, UPS, FedEx, and Bpost; warn on delivery if addresses have changed in sale order

## Lot/Serial Number

Add additional information on serial or lot numbers through the new note field: show the serial/lot number on invoice; mass assign through automatic generation or cc from spreadsheet.

## Valuation

The valuation of the stock is, now, represented by valuation layers. It allows users to have a clear view of how the stock is valued.

## Rules

Propagate changes in scheduled date to the next moves or not; If a product is available in stock, it will be taken from stock. If not, the MTO applies and it will be automatically reordered.

## Inventory Adjustments

Easily edit the quantity of a product without the need of creating an inventory adjustment.

## Notification

Inform the user via a next activity if a delivery cannot be fulfilled on time; Send automated emails from your delivery orders, at validation: send SMS.

## Forecast

Easily retrieve your forecasted inventory thanks to the new graph and grid views.

## Landed Costs

Landed costs can now be linked with vendor bills. Apply landed costs on products valued in AVCO.
