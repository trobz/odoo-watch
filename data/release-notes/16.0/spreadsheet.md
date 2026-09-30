---
version: "16.0"
app: "Spreadsheet"
app_slug: "spreadsheet"
source_url: "https://www.odoo.com/odoo-16-release-notes#table_of_content_heading_1713360697742_49"
item_count: 50
---

# Spreadsheet — Odoo 16.0

## Open Source

The Spreadsheet library has been open sourced in LGPL.

## XLSX Files Conversion

Convert an uploaded XLSX file to Odoo Spreadsheet for edition.

## Freeze Panes

Freeze rows and columns for better readability.

## Records on List()

See records on list() function.

## Absolute Cell References Keyboard Shortcut

Update absolute cell references by using the F4 keyboard shortcut.

## Accounting Functions

Added a new set of functions to get accounting measures (e.g., balance, credit, and debit).

## Auto-expanding Leaf Groupbys Removal

The Leaf Expanding Groupbys were removed.

## Automatic Currency Formatting

The currency formatting is automatically applied to monetary values on pivots and lists.

## Charts

A chart's default font color is now based on the chart's background color to maximize readability. Added global filtering for charts. Empty rows are now skipped when plotting charts.

## Charts/Figures Context Menu

Right-clicking on a chart/figure opens the context menu.

## Clear Formatting

Added 'Clear formatting' option on the Format menu.

## Color Picker

Improved the color picker's default colors and added the possibility to create custom ones.

## Conditional Formatting Rules Priority

Manage the priority of conditional formatting rules.

## Copy, Cut, Paste Charts

Cut, copy, and paste charts to move them across sheets.

## Ctrl+A Shortcut

Select the current range with Ctrl+A.

## Currency Conversion Function

Implemented a currency conversion function ('currency.rate()') based on the res.currency.rate model.

## Custom Currency Formats

Create custom currency formats.

## Dashboard Mode

Introduced a read-only mode to use spreadsheets as dashboards.

## Data Filters

Set up filters on a range of cells.

## Data Source Insertion

When using the Insert in Spreadsheet button, previews of existing spreadsheets are displayed to provide more context.

## Date Filter Offset

Match data to date filters with an offset.

## Date Formatting

All dates are now stored as integers.

## Date Global Filters

Select any year as a global filter.

## Default Date Filter

Improved the default date filter to select a period relative to the current one.

## Delete Lists/Pivots

Remove a pivot or a list from a spreadsheet.

## Dynamic Formula Format

Dynamic format management was introduced: create formulas whose final result's format depends on the inputs of the formula.

## End Content Keyboard Shortcuts

Jump to the end content in any direction with the 'Control + Arrow key' keyboard shortcuts.

## Financial Functions

Added 30+ financial functions.

## Formula Brackets/Strings Readability

Increased the color contrast of formulas highlights to improve their readability.

## Full Column/Row Range

Added support to the full column/row range.

## Gauge Chart

Added a Gauge chart type to display KPIs in Dashboards.

## Global Filters from Pivot Header

Set global filters from pivot header cells.

## Hide Sheet

Added the possibility to hide (and show) sheets.

## Insert Graphs

Insert graphs in Spreadsheet with the 'Insert in Spreadsheet' button.

## Large Numbers Format

Added a new format to display large numbers as shorted strings, e.g., 100,000 is shortened to 100k.

## Legend: None Option

Remove chart legends with the 'None' option.

## Link Charts to Odoo Menus

Link any chart to an Odoo menu to access it from the chart.

## Link Popover on Mouseover

The link popover now opens on mouseover.

## NA(), ISERR() and ISNA() Functions

Implemented the NA(), ISERR() and ISNA() functions for XLXS support.

## Odoo Functions Prefix

Odoo functions are now prefixed with 'ODOO' to distinguish and retrieve them easily

## Percent Symbol Handling

Improved the handling of the percent symbol (%) in formulas.

## Pivot Domain Edition

Edit the domain of a pivot from the Pivot Properties tab.

## Pivot Insertion Sorting

When inserting a pivot, the sorting used on the pivot view is now preserved in the spreadsheet.

## Pivot Names

Name and rename pivot tables.

## Pivot Position Function

Extended the support of the pivot position function to all spreadsheets and not only templates.

## Pivot/List Contextual Information

When inserted, additional contextual information is provided in the pivot/list name.

## Relative Date Filter

Added a new "Relative period" (last x days) time range to the date filter configuration.

## Return Date Format

When the pivot header function returns a date as a day, its numerical value is returned and, the day date format is set on it.

## Scale Charts on Time Series/Numbers

When the labels of a chart are formatted as dates or numbers, the chart displays data as Time Series and scale accordingly.

## Scorecard Chart

Added a Scorecard chart type to display key KPIs in Dashboards.
