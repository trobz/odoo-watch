---
version: "20.0"
app: "Manufacturing"
app_slug: "manufacturing"
source_url: "https://www.odoo.com/odoo-19-1-release-notes#table_of_content_heading_1_36"
item_count: 17
---

# Manufacturing — Odoo 20.0

## Generate lots and serials when closing manufacturing orders

Lots and serial numbers are always automatically generated when closing manufacturing orders.

## Manufacturing orders planned ASAP

Manufacturing orders are now planned as soon as possible by default. When multiple orders are planned, their sequence in the list determines scheduling priority.

## Split manufacturing orders

Split ongoing manufacturing orders to produce the remaining amount later.

## **Bill of materials overview forecast**

The Status and Availability columns in the bill of materials overview forecast have been merged to improve clarity.

## **Flexible consumption**

The flexible consumption setting on bills of materials has been removed. All manufacturing orders use flexible consumption by default, regardless of whether or not a bill of materials is selected.

## **Work and manufacturing order reporting**

The reporting of work orders and manufacturing orders has been improved, with key metrics updated.

## **Work order Kanban view**

Visualize and adapt work order planning with the new work order Kanban view.

## **Work order planning improvements**

The new Gantt views allow the planning of work orders using drag-and-drop, with enhanced color coding and the ability to view planning by employee. The work center overview has also been updated, featuring quick links to work orders and maintenance planning.

## Component replacement

The "Used In" smart button on the product form now displays respective bill of materials component lines, simplifying component replacements and other changes. The action to display component lines is also available from the bill of materials list and form views.

## Manufacturing order Kanban view

The manufacturing order Kanban view has been redesigned. Cards are now grouped by scheduled date in weeks and display information such as component status, active work center, deadline, and remaining time. The total remaining time for all manufacturing orders is displayed in all "Group By" searches.

## Bill of materials comparison

Compare bills of materials based on the product quantities used.

## Continuous production

Produced quantities can now be recorded on work orders. If "Continuous Production" is enabled on the bill of materials, subsequent operations start as soon as some quantities are ready.

## Draft versus confirmed manufacturing orders

On the "Manufacturing" operation type, choose whether procurement creates draft or confirmed manufacturing orders.

## Produce button

The separate "Produce" and "Produce All" buttons have been replaced by a single "Produce" button in Manufacturing, Shop Floor, and Barcode.

## Subcontracting available quantities

Bill of material overviews now display the free to use and on hand quantities both in your warehouses and at the subcontractor's location.

## Traceability report expiration dates

Expiration dates have been added to the traceability report.

## Work orders Gantt view

Completed work orders are now displayed by default in the "Work Orders Planning" Gantt view.
