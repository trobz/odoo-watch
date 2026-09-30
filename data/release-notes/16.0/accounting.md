---
version: "16.0"
app: "Accounting"
app_slug: "accounting"
source_url: "https://www.odoo.com/odoo-16-release-notes#table_of_content_heading_1713360697707_8"
item_count: 50
---

# Accounting — Odoo 16.0

## Analytics

Added a new analytic widget on invoices to ease analytic distribution, analytic plans (replacing groups), and analytic distribution models. Break financial reports down. Analyze financial reports according to analytic accounts and/or plans. Mass edition of analytics allowed on List views.

## Bank Reconciliation Widget

Improved the bank reconciliation widget's navigation, interface, and readability.

## Usability and Navigation

Updated the navigation throughout the Accounting app to avoid technical views and allow for an easier transition between different screens.

## Journal Audits

Various Journal Audits improvements: increased overall readability, removed repeated information, empty journals are now ignored, and tax applied details are included.

## Account Reports

Account Reports were completely reworked to improve their performance, UI, definition, and audit.

## Accounting Firms Mode

Activate the Accounting Firms mode to access a Quick Total field and manual sequence editing to encode invoices quickly.

## Accounting Menu

Reduced the number of menu items to help users find the right menu depending on the operation type.

## Asset Cancellation

It is now possible to cancel an asset.

## Asset Models

Asset models created from any account automatically use the related account as the default Fixed Asset Account.

## Asset Wizards

UI cleaned by grouping several asset modification wizards in one single button.

## Assets: Negative and Depreciation

Added negative assets management and the possibility to compute depreciations based on the effective number of days in each period. Any asset modification now results in a depreciation entry covering the period since the last depreciation entry was posted. The computation board and assests import were improved.

## Assets: Non-Deductible Tax

An asset's original value is now increased by the non-deductible portion of the tax (if any).

## Batch Payments: Chatter and Activities

The chatter and activities scheduling are now available for batch payments.

## Batch Payments: Rejection Management

Improved reconciliation flow of batch payments containing refused payments: users are now prompted to choose between canceling the original payment or leaving it open.

## Cash Discounts

Added a new separate definition in the Payment Terms supporting different taxes legislations (included or excluded). Receivable lines are not split anymore, improving the readability of accounting and follow-up reports. The Register Payment wizard suggests using the reduced amount if available. The reconciliation suggests using a computed early payment discount write-off if possible.

## Credit Limit by Partner

Setup a credit limit per company and/or partner. When the total amount of open invoices for that partner reaches the specified limit, a warning on sale orders or customer invoices is displayed.

## Currencies

Currencies display reworked on Journal Entries form views and Accounting Journals list views.

## Currency Conversion Rate: Invoice/Bill Date

The invoice or bill date is now used to set the currency conversion rate instead of the accounting date.

## Cut-off Entries Label

Improved cut-off entries label to improve ledgers readability.

## Data Import

Added a new guide, templates and functionalities to import the following accounting data: contacts, chart of accounts, and journal items.

## Disallowed Expenses Categories

Assign a Disallowed Expenses Category and Rate to an account from the Disallowed Expenses Categories' list view.

## Drag and Drop Upload

Import files by draging and dropping them on the Accounting Dashboard cards (invoices, bills, miscellaneous, bank) or the journals List views.

## Financial Reports Debug

Use the Finanial Reports' debug tool to analyze which accounts are potentially missing in the report definition.

## Follow-up Reports

Assign different follow-up contacts to a partner. Exclude a partner from automatic follow-ups. Manually set follow-up levels on a partner. Enhanced wizard to manually create follow-ups. Improved interface: follow-up list, individual report, follow-up levels definition. Filter follow-up reports on follow-up level.

## Intrastat Commodity Codes Renewal

Intrastat commodity codes have been renewed, and the default transaction code was updated to the two-digit one applicable since January 1st, 2022.

## Invoices and Bills Payment Widget

The payment information widget on invoices and bills was improved for multi-currencies transactions: the exchange difference entries are highlighted (if any), and, in the info-bullet, amounts are now expressed in both the company currency and the origin currency.

## Journal Entries and Items Quick Search

Quick searches on journal entries and items were improved.

## Journal Groups Naming

Journal Groups names are now unique to improve the readability of financial reports.

## Journals Audit Report

Revamped the Journals Audit report.

## Lock Dates Tracking

Changes to lock dates are tracked in a chatter on the company's form view.

## Non Trade Accounts Entries

Journal items on Non Trade accounts are now excluded from Aged reports; a filter is available to add them back in. Entries from Non Trade accounts now appear in the Miscellaneous tab of the Reconciliation widget.

## Non-continuous Sequence Alert

Smart alerts are displayed on the dashboard when a sales or purchase journal's sequence is not continuous.

## OCR Background Validation

Uploaded invoices and expenses are validated in the background by the OCR to make the interface more responsive.

## OCR Field Mapping

The manual field matching interface on invoices was improved.

## OCR: Bills and Invoices Settings

Activate the digitization of vendor bills and customer invoices separately.

## OCR: Partner Identification

Enhanced the partner detection on Invoices using bank account numbers and partner auto-complete information.

## Optional Bank Statements

Bank transactions can now stand alone: bank statements have been made optional.

## Partners Bank Account Management

Bank account management on partners was improved: all changes are logged in the chatter; a manual validation process was introduced for automatically added accounts before they can be used for outgoing payments.

## Partners Bank Account Numbers

Assign the same bank account number to different partners.

## Payment Terms

New payment terms definition screen. Added due date computation methods and dynamic examples.

## Payments: Total Amounts

Total amounts are displayed when grouping items on the Payments List view.

## Reconciliation: Foreign Currency

An exchange difference journal entry gets created directly at each partial payment to ensure the rate between the residual ammount currency and the residual amount. When reconciling two lines, one with a foreign currency and one expressed in the company currency, the reconciliation is made using the foreign currency.

## Recurring Account Moves Management

Recurring account moves for invoices and bills were simplified: an entry can be posted automatically at different frequencies.

## Reports Readability

Improved the design and readability of accounting reports.

## Reports: Foldable Records

All tax and financial reports use an improved way of declaring data thanks to foldable parent-children records in editors.

## Sales and Purchase Journals Alerts

Get an alert on the dashboard when a Sales or Purchase Journal's sequence is not continuous.

## SEPA Rejection Management

Improved SEPA rejection management: when canceling a payment belonging to a batch, the payment is deleted if no lock date is violated.

## SEPA: Non-Latin Characters Mapping

SEPA extended to support non-latin characters of all local European languages.

## Storno Accounting

Use negative debits and credits to reverse original accounting entries by activating the Storno Accounting setting.

## Vehicle Assets

All depreciation entries can be linked to the vehicle. A "Vehicle split" filter was added to the Disallowed Expenses report.
