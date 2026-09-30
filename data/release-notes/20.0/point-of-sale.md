---
version: "20.0"
app: "Point of Sale"
app_slug: "point-of-sale"
source_url: "https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_116"
item_count: 24
---

# Point of Sale — Odoo 20.0

## Base unit price on product label

Display the product reference price on product labels.

## Booking Kanban and pivot views

Bookings now have dedicated Kanban and pivot views.

## Convert order lines into a combo

The POS now recommends converting order lines into combos when possible to simplify menu orders for big tables.

## Employee access levels

Employee access levels have been renamed, and a new, highly restrictive "Supervised" access level has been added.

## End of session

At the end of the session, a global sale is generated to simplify the accounting entries and remove the miscellaneous entries. Payment journal entries are automatically generated at the time specified in the settings without needing to end the session.

## Expired product notification

Users are notified when they select expired products on the POS.

## GoFood delivery integration

Support has been added for GoFood orders and menu sync for Indonesia and Vietnam (available from 19.0).

## GrabFood delivery integration

Support has been added for GrabFood orders and menu sync for Cambodia, Indonesia, Malaysia, Myanmar, Philippines, Singapore, Thailand, and Vietnam (available from 19.0).

## Label printing

Any label printer can now be connected directly via USB proxy.

## Mercado Pago terminal

Mercado Pago terminal-based QR payments, refunds, and cancellations are now supported via the Orders API integration, enabling use by Chilean companies as well.

## Multiple currencies

Multiple currencies are now be supported at checkout in the same point of sale.

## Order search

In the "Orders" overview, search by invoice number or receipt number.

## Print preparation tickets per product

Use the "Split per product" feature to print one preparation ticket per product instead of one ticket grouping all products in the order.

## Printer management

Set up multiple printers linked to your point of sale, and then select on which printer to print, improving the workflow for big structures with several cash drawers.

## Receipt printing

A printer's paper size can now be configured manually in developer mode to ensure receipts are formatted correctly.

## Reorganizing products in POS interface

Drag and drop products in the POS interface to reorganize them.

## Self-ordering

- Customers using self-ordering can leave notes at checkout; these are visible on the kitchen display.
- Optional products are displayed when ordering from a mobile device or a kiosk.
- Generate and print an order-specific QR code, allowing customers to scan it to place their order and pay after their meal.

## Service fees

Add a service fee for Point of Sale orders and self-orders via presets, and display the amount on invoices.

## Simplified inventory management

Point of Sale can now work with simplified inventory management, without installing the Inventory app. A single on-hand quantity is displayed per product and there are no required transfers.

## Simplified receipts

Print a simplified receipt that displays the subtotals and taxes of the order without the order lines.

## Snooze products

Make products temporarily unavailable on the POS or self-ordering menu by snoozing them.

## Static QR code payment

Payment via static UPI QR codes is now supported.

## UrbanPiper integration

- Most settings related to UrbanPiper can now be managed directly from within the Point of Sale app.
- The following food delivery platforms are now supported via UrbanPiper: Didi Food, Enqueue, FoodZapp, InstaShop, Mandoob, RadYes , Smiles, Snoonu, Swiggy Bolt, Talabna, Zomato Express, Zyda.

## WhatsApp and SMS self-order receipt

Customers can now receive their receipt via WhatsApp or SMS when self-ordering.
