---
version: "15.0"
app: "Accounting"
app_slug: "accounting"
source_url: "http://web.archive.org/web/20250810140306id_/https://www.odoo.com/odoo-15-release-notes"
item_count: 14
---

# Accounting — Odoo 15.0

## Chart of Accounts

Revamped account form view. Track history of changes in a chatter.

## Aged Reports

Get amount in currency, explicit column labels. Export Amounts and Currency in two distinct columns.

## Entries

Set a “Default account” in settings for automatic entries such as: currency exchange rate differences from payments, bank suspense accounts from bank sync, internal transfer accounts etc. Button added to easily set an entry as checked (be it a customer invoice, a vendor bill, or any journal entry). The changes are logged in the chatter.

## Currencies

See conversion rate and its reverse in a revamped currency form view. Prevent confusion in currency by getting the company currency on the form.

## Financial Reports

“Control Domains” on Financial Report Lines are added as a debug feature to find accounts erroneously counted multiple times (or even missing ones).

## Follow Up

Personalize the follow-up email template subject line.

## Fiscal Year

Gave the Lock Dates Wizard an updated design; Lock Date types are more easily differentiated from one another with tooltips.

## VAT

Odoo supports companies that must charge foreign VAT, and declare VAT in foreign countries.

## Payments

Navigate and distinguish Journal Entries from the related payments or bank statement lines. Record payments in list views to make their total accurate. Automatic reconciliation for both payments of internal transfer; Transfer payment from every partner category. Exclude partners from the aged reports thanks to a checkbox on account. Batch payments are more intuitive with new fields, filters and screens optimization. Prevent user to select draft payments in the batch.

## Journals

Payment methods management on bank/cash journal improved, manage several manual methods to allow filtering by payment card owner. Optionally specify outstanding accounts for each payment method.

## Reconciliation

Revamped reconciliation tool. By default, Odoo will partially reconcile invoices/bills. Fully reconcile invoices/bills in case of underpayments thanks to payment tolerance mechanism and specify the counterpart accounts for the difference.

## Invoicing

Accrued entries, such as Invoices to be Issued/Received, can get easily generated from purchase orders & sales order actions.

## Taxes

Carry over amounts from one period to the next on tax reports and audit those in debug mode. Break down tax groups on invoice to display intermediate subtotal (in case of discount or to manage withholding taxes.

## Vendor Bill

The “Accounting Date” is the end of the month following the tax lock date or creation date.
