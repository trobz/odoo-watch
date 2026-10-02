---
version: "20.0"
app: "Manufacturing"
app_slug: "manufacturing"
source_url: "https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_108"
item_count: 25
---

# Manufacturing — Odoo 20.0

## Backorder planning

Backorders of planned productions are now also planned automatically upon their creation.

## Bill of materials

- Compare bills of materials based on the product quantities used.
- The "Status" and "Availability" columns in the bill of materials overview forecast have been merged to improve clarity.
- Register extra costs for a manufacturing order using the dedicated field on the bill of materials form.
- View and manage a bill of materials' components and sub-assemblies directly from the bill of materials form.

## Component replacement

The "Used In" smart button on the product form now displays respective bill of materials component lines, simplifying component replacements and other changes. The action to display component lines is also available from the bill of materials list and form views.

## Continuous production

Produced quantities can now be recorded on work orders. If "Continuous Production" is enabled on the bill of materials, subsequent operations start as soon as some quantities are ready.

## Draft versus confirmed manufacturing orders

On the "Manufacturing" operation type, choose whether procurement creates draft or confirmed manufacturing orders.

## Flexible consumption

The flexible consumption setting on bills of materials has been removed. All manufacturing orders use flexible consumption by default, regardless of whether or not a bill of materials is selected.

## Generate lots and serials when closing manufacturing orders

Lots and serial numbers are always automatically generated when closing manufacturing orders.

## Lot/serial number transfers

The "Transfers" smart button on lots and serial numbers shows delivery move lines instead of the entire transfer, allowing for more precise recalls.

## Manufacturing order Kanban view

The manufacturing order Kanban view has been redesigned. Cards are now grouped by scheduled date in weeks and display information such as component status, active work center, deadline, and remaining time. The total remaining time for all manufacturing orders is displayed in all "Group By" searches.

## Manufacturing orders planned ASAP

Manufacturing orders are now planned as soon as possible by default. When multiple orders are planned, their sequence in the list determines scheduling priority.

## MO cost

- The "MO Cost" field on an MO overview now shows the provisional cost when the manufacturing order is in progress and real cost when the manufacturing order is complete.
- The cost of subcontracted product replenishments in the MO overview takes into account component costs.

## Produce button

The separate "Produce" and "Produce All" buttons have been replaced by a single "Produce" button in Manufacturing, Shop Floor, and Barcode.

## Put in pack from MO

If a destination package is specified on the manufacturing order, the final product is automatically added to it upon production.

## Reset MO to draft

Reset validated or canceled manufacturing orders to draft.

## Shop Floor demo sheet

Download a Shop Floor demo sheet to quickly test the app's barcode capabilities.

## Split manufacturing orders

Split ongoing manufacturing orders to produce the remaining amount later.

## Subcontracting MO

The "Component Status" and MO overview are now also available for subcontracting production. Check what components are missing and order them directly.

## Subcontracting reception valuation

If no purchase order is linked, the subcontractor cost is assigned at the product's reception based on the vendor pricelist.

## To Replenish filter

A "To Replenish" filter has been added to the MO Overview.

## Traceability report expiration dates

Expiration dates have been added to the traceability report.

## Visualize and confirm work orders

Confirm work orders from the Work Order Planning Gantt view, even if they contain draft work orders.

## Work and manufacturing order reporting

The reporting of work orders and manufacturing orders has been improved, with key metrics updated.

## Work order views

- Visualize and adapt work order planning with the new work order Kanban view.
- The new Gantt view allows the planning of work orders using drag-and-drop, with enhanced color coding and the ability to view planning by employee.
- Completed work orders are now displayed by default in the Gantt view.

## Work center overview

The work center overview has also been updated, featuring quick links to work orders and maintenance planning.

## Work orders in blocked work centers

It is now possible to process work orders in blocked work centers.
