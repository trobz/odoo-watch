---
version: "18.0"
app: "Spreadsheet"
app_slug: "spreadsheet"
source_url: "https://www.odoo.com/odoo-18-release-notes#table_of_content_heading_1725624803512_48"
item_count: 46
---

# Spreadsheet — Odoo 18.0

## Pivots: measures

Edit and add measures in pivot tables. Select the way measure values are displayed in the pivot table. Measures can also be renamed in pivot tables. Pivots can use the same measure multiple times with different aggregators.

## Pivots: dimensions

Edit rows' and columns' dimensions when using pivot tables.

## Dynamic pivots

Pivot tables are now inserted as dynamic pivots in a spreadsheet, and an option to switch from a dynamic to a static pivot has been added. You can also define the number of columns to display in a dynamic pivot.

## Pivot measures and groups

Measures and groups can now be customized on pivot tables.

## Pivot creation

Create pivot tables from scratch in a spreadsheet.

## Copy/paste pivot table cells

Copy-pasting a cell or a range of cells from a dynamic pivot will now paste the static pivot formula for each copied cell(s).

## Pivots: dates

Refer to a date in a pivot formula, regardless of the date format. The date format expected in the formula will be inferred automatically.

## Pivots: calculated fields

Create calculated fields. Add extra dynamic measures by adding calculations (i.e., calculation between fields from the pivot, between values located elsewhere in the spreadsheet, or a mix of both). Functions can also be used in those extra measures.

## Pivots: increased date granularity

Added day of the week, hour of the day, minutes, and seconds as options for date granularity.

## Tables for array formulas

A dynamic table adapts to the formula's output, allowing handling complex datasets.

## New functions

The SEQUENCE, INDIRECT, OFFSET, CONVERT, and CELL functions have been added.

## PIVOT formula

ODOO.PIVOT formulas are renamed PIVOT.

## Vectorization on formulas

It is now possible to use a range of cells in formulas that request a single argument. The returned value will then be an array of cells.

## Paste values, preserve format

Number formatting is now preserved when pasting values.

## Plain text format

Added plain text format.

## Remove source spreadsheet when adding to dashboard

The original spreadsheet of a Dashboard is now send to Trash in Documents.

## Insert list selection

Insert a selection of records from a list to a spreadsheet.

## Unused data sources

Unused data sources are flagged in the Data menu.

## Find and Replace feature

Added search granularity (all sheets, current sheet or specific range) to the Find and Replace feature.

## Data tables

Data tables allow quick sorting, styling, and filtering of data as well as adding new records.

## Cell comments and tags

Insert comments and tag someone on cells.

## Tables autofill

Adding a formula in a new column autofills the whole column.

## Partial VLOOKUP

Support of partial match in VLOOKUP formulas.

## Import/export groups

Groups are now included when importing or exporting data.

## Automatic expansion

Multi-cell formulas now adjust range for results.

## Enhanced gauges

Improved gauge charts visuals.

## Checkbox and dropdown

Insert checkboxes and dropdown lists.

## Version history

Restore a previous version from the version history panel.

## Chart customization

Added design features in the chart editor.

## New chart types

New chart types have been added (area, combination, horizontal bar, doughnut, population pyramid, scatter, radar, and waterfall).

## Pie charts

Pie charts exclude negative numbers.

## Chart data values

Choose to hide or display data values on charts.

## Scorecards design and readability

When the baseline description is too long, its font is reduced to fit on one line.

## Custom formats detection

When a specific format (date, currency, etc.) is detected it appears on the top bar.

## Date formatting: quarter

Dates can be formatted as quarters by using the "more date formats" menu. The quarter recognition has also been improved in pivot tables so that any dates can be used in pivot formulas.

## Highlight and hover

Related cells are highlighted when editing or hovering over pivot/list data sources.

## Accounting format

The Accounting format has been added.

## Conditional formatting: Data bar and formulas

The Data bar conditional rule format has been added. Use a formula as a condition for formatting cells.

## Copying data to another spreadsheet

Values can be copied and pasted from one spreadsheet to another (excluding Pivot and List formulas).

## Custom table style

Create custom table styles.

## Global filters: domain edition

Define a domain to restrict the list of values.

## List sorting

Modify the list sorting from the side panel.

## Sheet tab colors

Assign colors to sheet tabs.

## Spreadsheet quote calculator

Link a spreadsheet template to a quotation template and access your calculator from a sales order. Calculated values in the spreadsheet can overwrite the initial values in the sale order.

## Viewing records from charts

A "See records" option is available when right-clicking a data series. The "Link to Odoo menu" has also been removed.

## Table resizing

Adjust the size of the table using a button.
