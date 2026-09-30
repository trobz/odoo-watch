---
version: "19.0"
app: "Accounting"
app_slug: "accounting"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_21"
item_count: 44
---

# Accounting — Odoo 19.0

## Account selection

- Add descriptions on accounts to explain when to use each account.
- Default taxes on accounts are only applied on invoices and bills and not on miscellaneous entries.
- On invoices, income accounts are proposed first. On bills, expenses and fixed assets are proposed first. Both filters can be overridden if needed.

## Analytic budgets in One App Free

Use budgets without installing the Purchase app, for simple budgeting without committed amounts.

## Analytic subplans

The management of the hierarchy of analytic subplans in budgets and analytic reports has been improved.

## Annual statements composite report

A default Annual Statements composite report simplifies year-end reporting by combining the balance sheet, profit and loss, and trial balances so users can print them all at once.

## Audit reports

Create and export audit reports via Knowledge.

## Asset import templates

Import templates have been added for assets.

## Bank reconciliation

- The bank reconciliation interface has been simplified. Automated reconciliation models have been improved to enhance transaction recognition.
- Keyboard shortcuts are available on the bank reconciliation view.
- Draft entries can now be reconciled. Eventual automatic moves (like currency exchange or cash basis moves) are created in draft simultaneously with the reconciliation. When posting the original entry, the reconciliation is automatically confirmed as well.
- Fully reconcile or write off partially reconciled items.

## Bank statement OCR manual correction

After a statement has been processed through the OCR, manually correct the Starting Balance and Ending Balance of the statement by clicking on the fields and then on the appropriate number in the PDF.

## Bank transactions with PDF preview

Preview attached documents directly in the bank transaction list view whenever a document is linked to a statement.

## Cash discounts

The "Always (upon invoice)" option has been added for tax reduction on payment terms with a cash discount.

## Debit notes

The Debit note option in the Action menu has been replaced with a dedicated button.

## Default recipient bank account

On customer invoices, the "Recipient Bank Account" field is now populated using an improved selection algorithm. If a specific payment method is set on the partner of the invoice, Odoo will select any related bank accounts for the payment of the invoice. If no payment method is found, Odoo will select any bank account of the company whose currency matches the currency of the invoice. If nothing is found, the first available bank account will be set.

## Deferred miscellaneous entries

Start and end dates have been added to miscellaneous entries, allowing deferral of bills to receive and invoices to issue.

## Down payment account

The Down payment Account field has been moved from Product Category to Accounting Settings.

## Duplicate bill detection

When a potential duplicate bill is detected, the warning banner remains visible even after posting and the Reference field of affected bills is highlighted in the list view. Duplicate bills are excluded from automatic posting.

## Exclude from follow-up

Exclude specific moves from follow-ups. Excluded invoices are ignored in both the computation and report sent.

## Fiscal categories on accounts

Fiscal categories have been moved to accounts to allow different rates to be set for accounts in the same category (e.g., for fleet expenses in Belgium) without duplicating categories.

## Fiscal positions

- Tax mappings in fiscal positions have been removed. Instead, each tax declares in which fiscal position it is applicable (empty means all) and declares which taxes from other fiscal positions it replaces (e.g., a 0% export tax declares it replaces national sales taxes in the context of the Export fiscal position). Taxes are by default filtered on invoices based on the fiscal position, and on products based on the Domestic fiscal position (the first in the list).
- Fiscal positions are now always determined based on their sequence, with filters applied for applicability. Multiple localizations have been simplified to a single Domestic fiscal position.
- On invoices, taxes in the current fiscal position that are replaced by others are filtered out by default, with additional taxes still accessible through "Search More".

## Follow up via WhatsApp

Use WhatsApp messages on follow-up levels.

## Follow-up report

A new variant of the partner ledger, the follow-up report, has been introduced. It is clearly separated from the customer statement and serves a distinct purpose: highlighting overdue invoices separately from due ones. The report is accessible from the reporting section for streamlined follow-ups.

## Follow-up/partner ledger access to Invoicing and banks

Invoicing in Enterprise now grants access to the account report module and activates partner reports by default, allowing both Invoicing users and Accounting users with only "Invoicing & Banks" access rights.

## Improved duplicate detection

Invoice duplicate detection has been improved with two levels of warnings for invoices and bills: red invoices that are highly likely to be duplicates that should be corrected and yellow potential duplicates that should be investigated before posting. After posting, only red warnings will remain.

## Invoice email attachments

When sending an invoice by email, documents from the Documents app can now be easily added as email attachments.

## Invoice analysis

The total amount (i.e., the total amount of the invoice converted in the company currency) is available as a measure in the Invoice analysis report.

## ISO20022

- Define the charge bearer on individual payments when generating batch payments for ISO20022 payment files.
- The priority instruction can be specified on payments for the ISO20022 paymenth method and its variants.
- Outgoing ISO20022 payments now include the End-to-End identifier to simplify reconciliation.

## KYC payment verification

The KYC verification has been improved for payment initiation from Odoo.

## Light audit trail

The non-restrictive audit trail has been made available by default for everyone.

## Menu and form organization and layout

- A new journal creation wizard has been added to the dashboard; it includes bank and credit card account synchronization.
- The Journal and Reconciliation models' form views have been revamped.
- The invoice line display settings are now stored separately for customer invoices and bills, allowing different configurations for incoming and outgoing invoices.

## Miscellaneous journals dashboard link

On the dashboard, miscellaneous journals have a link showing the draft entries to validate manually. This link also shows entries that have been imported automatically (i.e., with an email alias).

## OCR manual correction

After a document has been digitized, select any portion(s) of text to fill in any field present on the form view, including custom fields and fields in one2many lines. Automatically create multiple lines at once by selecting multiple amounts in the document at the same time.

## Open on date

The Open On Date feature allows checking the status of amounts still outstanding after a company's financial year-end to ensure the accuracy of the financial statements.

## Payment communication generation

Payment communication formats are made explicit with examples. The European standard has been improved. A new "numbers only" format has been added to handle countries where payment references including special characters are not supported.

## Payment withholding tax

The option to apply a withholding tax directly on the payment has been added (available from 18.0).

## Print & Send

Improved the layout and usability of the Send & Print wizard, the accessibility of the Print menu options, and the customizability of action reports and templates via Studio.

## Professional percentage for receipts

The "Professional" percentage column that was available for vendor bills is now also available for purchase receipts.

## Purchase and sales receipts

Purchase and sales receipts have been merged with invoices and bills. Purchase receipts are always available: change between bill or receipt on the vendor bill form. Sales receipts can be activated in the settings. Localizations can be set to override default taxes depending on the local requirements.

## Purchase order matching

When importing vendor bills (via XML or OCR), Odoo will look for purchase order references everywhere in the imported bill (including on line descriptions) to match with existing purchase orders.

## Report annotations

Annotations made on reports are visible in the report's chatter.

## Reset invoices/bills to draft

Resetting an invoice/bill detaches the invoice already generated (available from 18.0).

## Review invoices

Accounting users with only invoicing access rights (Invoicing or Invoicing & Banks) are allowed to post moves like invoices, but they are automatically flagged as "To review" for accountants (users with Bookkeeper or Administrator access rights). Once a posted move has been reviewed by accountants, it cannot be reset by Invoicing users anymore.

## Tax report: tax tag signs

The + and - signs have been removed from tax tags on tax reports; inversions are now handled directly on the report lines.

## Tax return

A new tax return feature has been introduced, supporting fiscal return obligations and deadlines and automated validation checks to ensure accurate filings. The feature is customizable to meet localization needs across different regions.

## Taxable supply date

The taxable supply date is activated in countries that require it.

## Updated action names

The menu item action names have been revised to provide readable URLs.
