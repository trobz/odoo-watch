---
version: "18.0"
app: "Accounting"
app_slug: "accounting"
source_url: "https://www.odoo.com/odoo-18-release-notes#table_of_content_heading_1725624803512_52"
item_count: 55
---

# Accounting — Odoo 18.0

## Abnormal invoice alert

Added a statistics-based alert system to automatically identify abnormal amounts and dates in invoices.

## Allow email aliases on MISC journals

Use email aliases on miscellaneous journals to automatically create journal entries from email attachments.

## Analytic budgets

New budget management. No more dates on budget lines; no more budgetary positions.

## Annual sequence and staggered fiscal years

The fiscal year sequence on journals can differ from calendar years to handle staggered fiscal years.

## Ascending/descending report dates

Switch the order of your date columns (ascending/descending) when using date comparisons.

## Audit trail improvements

The audit trail has been improved, namely in the context of the GoBD certification in Germany.

## Autopost bills

Automatically post bills from chosen vendors.

## Bank reconciliation: simplified batch payment matching and statement form view

Batch payments are represented by a single folded line in the Bank reconciliation widget to simplify the matching process. The statement form view can be opened from the Kanban view and includes a chatter with quick navigation to linked transactions.

## Bank statement: import and OCR

Bank statements can be imported even when transactions are not sorted by date. Upload PDFs or image files of bank statements to have the OCR extract the transactions automatically.

## Bills payment wizard: QR codes

The vendor bills payment wizard integrates QR codes for outgoing payments.

## Catalog view in Invoicing

The Catalog view is now available on customer invoices and vendor bills.

## Charge bearer

Specify the charge bearer when generating batch payments for ISO20022 payment files.

## Check printing layout

Select check layouts in the bank journal settings.

## Combine analytic distribution models

Sequences are now available on analytic distribution models, allowing distribution according to multiple models provided that they are distributed on different plans.

## Configure layout wizard

The configure layout wizard shown when the user prints their first invoice was improved. The data of the actual invoice is used, the preview display is enhanced, and the QR code for SEPA payments is more easily added.

## Credit card journal

A new credit card journal type was added to register credit card payments, upload statements, and handle reconciliation.

## Currency exchange rate

The exchange rate is stored on invoices and displayed.

## Customized invoice templates

Invoice templates can now be customized with Studio and declared as compatible with the Send & Print flow on invoices.

## Date selector

The new date selector on reports enables users to navigate smoothly from one period to another.

## Duplicate bill detection

Improved Vendor Bill duplicate detection. Potential duplicates (using Bill references) both in draft and posted entries are looked for in the database before creating the new move. Smart links are available to directly navigate to the potential duplicate(s).

## Financial budgets

On the profit and loss report, display and compare the report's figures with financial budgets that are separate from analytic budgets.

## Follow-up report, customer statement, and partner ledger revamp

The Follow-up and Customer Statement views and modules were removed and merged. Follow-up reports can be configured to automatically add followers to the client chatter on execution. Miscellaneous entries impacting the client account will be excluded from the reports by default. The Partner Ledger includes additional options and is displayed similarly to a customer statement, with unnecessary columns hidden. It can also be sent directly to customers.

## Import matching numbers

Add a matching_number to your CSV import of lines. Odoo will wait for all related account moves to be posted and try to reproduce the reconciliation when that happens. If it fails, the imported reconciliation will be discarded.

## Installment payments

Registering a payment from the invoice form view considers installment amounts defined on the payment terms. The customer portal clearly displays what has already been paid.

## Intercompany transactions

Improve flexibility of managing intercompany transactions by using booleans instead of radio buttons.

## Invoice Analysis report

The Invoice Analysis report offers margin and a simple inventory valuation measure based on customer invoices and vendor bills without requiring the Inventory app.

## Journal email alias

If an email that contains no usable file is received on an email address set as a journal alias, an automatic response is sent to the sender informing them that no document was received.

## Journal report

The UI of the journal report has been simplified. Performance is prioritized over detailed transactions, but detailed transactions remain available for export.

## Legal notes on taxes

Specific legal notes can be added to taxes to be shown on documents when the tax is used. This enables covering more granular business cases than legal notes based on fiscal positions.

## Loan management

Manage acquired loans with automated adjustments based on your defined or imported amortization schedule.

## Lock dates wizard

Allow locking by journal type; add a hard lock date and exceptions management mechanism.

## Matching numbers

Matching numbers have been simplified and are displayed with colors. Partial matches have been improved and specify which moves are partially matched together with a proper identifier.

## Multi-ledger

Multi-ledger usability has been improved in multi-company settings for better grouping, default selection, and filtering.

## New documents layout

Three new document layouts were added for more customizations.

## New product widget

Products and descriptions are now combined in a single column in invoice line edition.

## OSS periodicity

OSS reports now follow their own periodic schedule, separate from the fiscal one. OSS sales reports are filed quarterly, while IOSS reports are filed monthly.

## Overdue invoices and online payments

Customers are shown overdue amounts on their portal. Smart links are provided both on the portal and in follow-up reports to proceed with quick online payment of overdue amounts.

## Partner payment method

Specify preferred payment methods per partner (incoming and outgoing). You can then filter and group invoices per payment method to create payments in mass more easily. When a payment for a specific partner is created, that partner's preferred payment method will be selected by default.

## Payment terms

Added a new payment term date calculation type: "Days end of month on the".

## Payments without accounting entries

Payments do not create an accounting move unless an outstanding account is set on the linked payment method.

## Peppol

Send invoices on the Peppol network while still receiving your bills in any other system.

## PO/Bill matching

Advanced PO matching: A new screen is available to manually match open purchase order lines and vendor bill lines together. You can also create completely new purchase orders directly from vendor bill lines and add lines as down payments on existing purchase orders.

## Preferred invoicing method

Define a preferred invoice-sending method and e-Invoice format for contacts to simplify the batch-sending process. Customers can then manage their preferences from the portal.

## Send & Print visibility

The visibility of the Send & Print feature has been improved.

## Reconciliation models: generate invoice/bill

New reconciliation model types to create a customer invoice or vendor bill directly from a bank transaction.

## Reconciliation wizard

The amount is editable when reconciling a single journal item through the reconciliation wizard, allowing for partial write-offs.

## Register payment on draft invoices

It is now possible to register payments on draft invoices and bills via the action menu.

## Sales taxes price included/excluded

All standard sales taxes now follow a new company setting defining them as price-included or price-excluded, making onboarding and database setup easier. Individual taxes can be forced as being price-included or price-excluded when needed, overriding the default company setting.

## SEPA Direct Debit (SDD)

The SEPA Direct Debit (SDD) flow and UX have been improved. Mandates can be sent through a Send & Print action. The pre-notification period is chosen on the mandate and determines when the mandatory notification will be sent to a debtor before a collection.

## SEPA ISO 20022

The SEPA module has been refactored to clearly distinguish between the ISO20022 and SEPA payment methods.

## Shared accounts between companies

The same account can now belong to multiple companies, and accounts from different companies can be merged.

## Split balance sheet horizontally

Balance sheet can now be presented in two halves next to each other to satisfy various regional display preferences.

## UBL invoice import

When importing a UBL (XML) invoice, Odoo will populate the bank account found in the XML on the partner if possible.

## Updating imported invoice lines

Add information (e.g., products and tax analytics) to invoice lines imported via electronic invoicing or OCR without impacting the imported information and amounts.

## Warning for potential duplicate invoices

A warning is displayed when editing a customer invoice if it is a suspected duplicate of another one by comparing the customer, the date of the invoice, and its amount.
