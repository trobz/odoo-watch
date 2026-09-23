---
version: "18.0"
app: "Inventory"
app_slug: "inventory"
source_url: "https://www.odoo.com/odoo-18-release-notes#table_of_content_heading_1725624803512_33"
item_count: 18
---

# Inventory — Odoo 18.0

## Batch and wave picking improvements

Automate wave picking creation. When grouping transfers into waves/batches, the elements common to all transfers, such as contact or location, appear in the wave/batch's description.

## Create backorders in advance

Split pickings before validating, allowing deliveries at two different locations or dates.

## Cross-company lots/serials

Lots and serial numbers are now fully traceable through multiple companies. When doing an inter-company transfer, serial and lot numbers remain.

## Dashboard UX

Revamped the Inventory dashboard UX.

## Dispatch management system

Organize delivery rounds and manage shipments with your own fleet or third-party logistics.

## Eased return process

When creating a return, create a new transfer to send new products back.

## Editing a package's location

Change the location of a package without creating any transfer and move packages using the Kanban view.

## Editing layer values

Edit specific valuation layers for revaluation.

## Inventory reports UX

Inventory reporting menu revamp.

## Make to stock and order

When a rule is set as "Take from stock, if not available, trigger another rule", launch a procurement for only the quantity missing from the new move.

## Manual entry of barcodes

You can now enter barcode numbers manually.

## Next transfer button

A new smart button has been added to transfers to show the next linked transfers.

## Pull to push rules and flexible routes

Push rules are now triggered when a transfer is validated. Transfers are not created in advance, allowing more flexibility. Transfers waiting for another transfer are no longer polluting the space. All default multi-step routes have been redesigned to reflect this change.

## Putaway rules

Improved putaway rules put incoming products where other quantities of the same product are or have been.

## Tracking at delivery

To ease the transfer of tracked products that are not tracked at reception, they appear as non-tracked products in transfers.

## User rights: inventory adjustments

Users can now apply inventory adjustments.

## Valuation by lot/serial number

Each lot or serial number of the same product now has a separate valuation.

## View empty locations

See which locations are empty from the locations list view.
