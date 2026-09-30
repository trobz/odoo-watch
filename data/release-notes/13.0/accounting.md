---
version: "13.0"
app: "Accounting"
app_slug: "accounting"
source_url: "http://web.archive.org/web/20260410095156id_/https://www.odoo.com/odoo-13-release-notes"
item_count: 36
---

# Accounting — Odoo 13.0

## Usability

Chatter is available on Journal & Journal Entry; Manual reconciliation for partners from aged balance and partner ledger. Move to check on accounting dashboard. Improved form, list views, dashboard, settings, ...

## Reconciliation

Reconcile a payment with both a receivable and a payable. Find easily reconciled entries (search, stat button). Find items from Sales Orders; bank reconciliation report improvement. Multiple taxes per line in write Off

## Journals

Default set of the journal to prevent error; Select several account journals in financial reports.

## Assets

New reports for assets; Manage assets through account; improved usability, automate journal entries for re-evaluations, sell & disposals.

## IBAN Compliance

New widget to know if the bank account number is a correct IBAN number.

## Taxes

Periodical closing with lock date; Configuration of taxes made easy; Only one tax per tax percentage; Type of taxes visible in tax mapping.

## Invoicing

Import in mass customer invoices in Odoo accounting. Select the invoice reference type by journal entries.

## Vendor Bills

Technical improvements and QR code vendor bill payment allowed for SEPA regions.

## SEPA

A Back Booking option has been added. It helps define how the debit should be handled, single consolidated debit or multiple debits.

## Accounting Engine

The models of customer invoice, vendor bill and journal entry have been merged, allowing more flexibility in the edition of those documents.

## Documents

Improvement of the layout of the PDF previewer.

## Intrastat

Prevent duplicate of partners based on VAT number.

## Follow Up

Send SMS Text Messages from your follow-up reports.

## Taxcloud

Easier configuration. Show tax amount rather than computed tax rates to the customer.

## Suspense Account for Bank Transactions

Easy match between suspense account entries and recorded bills, history on entries.

## Accounting Entries Security Modes

You can choose the Security level by journal (new lock posted entries by hash). By default you can modify entries as long as the period is not closed.

## Closed Tax Period

You can set the accounting date automatically to the first open day for new bill on tax locked periods. IE: It's now the 04/10 the invoice was on 26/09 but tax lock date was 30/09 Odoo will set accounting date to 01/10.

## Accrual

Allowing recognizing the expense/revenue in a different period keeping tax return in the invoice period.

## Deferral

Manage expenses as well as revenues; Automated deferred expense entries.

## Accounting Adjustements

AUtomatic transfers based on distribution rates (%) or analytic filters

## Refactoring

Better precision on currency rate. Fiscal position accepts char in zip range. Improved adjustements in tax wizard.

## Dynamic Journals & Ledgers

Browse your accounting data through Odoo generic search views and get the original document preview. (Available in: Journal, Sales, Purchase, Misc, Bank & Ledger, Partner ledger, General ledger)

## Payment Follow-up

Improved usability, automated level, filtering by levels & SMS integration.

## Invoices importation

If your invoicing is managed by another software than Odoo, you can import all your invoices easily.

## Manual Journal Entries

Improvement in manual encoding of entries, pre-filled fields, journal set by default.

## CODA & CAMT import improvements

You can now import multiples files all at once, new fields, better performance.

## Off Balance sheet

New account type: Off-Balance sheet accounts useful for annual reporting annexes.

## Payments

Split payment for partial allocation; QR code vendor bill payment allowed for SEPA countries.

## Manual Reconciliation

Manual reconciliation for a dedicated partner will always show all open entries allowing to easily make payable/receivable adjustments.

## Reconciliation Models

New fields allow more flexibility for automated rules. New rule to automate fee detection based on communication.

## Reporting

Improved layout, performance in Aged Balances. Improved cashflow statement performance. New bank statement report with more details.

## Single Liability Account

If the balance of VAT transactions shows a debt to the State at the end of the period, they are combined into a single liability account to help with deadlines and automate the accounting entries.

## Taxes Closing Entries

New lock date allowing preventing any changes related to a closed tax period. The type of tax (sales, purchase) is now visible in the tax mapping.

## Print Original Vendor Bills

You can now print the original vendor bills for as many bills as you want. You can choose between the Odoo bill or the original one.

## Arithmetic operations in fields

New widget to allow operations directly into fields (ie: =650*0.34).

## Winbooks import

You can now import a Winbooks database zip file
