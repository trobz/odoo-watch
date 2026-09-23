---
version: "17.0"
app: "Accounting"
app_slug: "accounting"
source_url: "https://www.odoo.com/odoo-17-release-notes#table_of_content_heading_1707731490324_63"
item_count: 59
---

# Accounting — Odoo 17.0

## Accounting reports

Configure accounting reports more easily: move entire sections, define the parent line by dragging and dropping, and add indents to highlight the hierarchy.

## Allocation of invoice discounts

Separate sales and granted/received discounts on invoices by posting them on different accounts. The sales lines remain unaffected, but the discount is subtracted and moved to the specified account.

## Assets usability

Assets import usability was improved. It is now possible to post assets in bulk. The status of an asset can't be imported anymore.

## Auto extract PDFs only

Prioritize PDF attachments when using the 'create invoice on email' feature for sales and purchase journals.

## Auto-reconcile feature

Introduction of a new wizard for auto-reconciliation.

## Avalara geolocalization and sales tax

Using Avalara's address validation now populates geolocalization information on the partner. This information can be used to compute sales taxes.

## AvaTax: use warehouse address in ship from information

When computing taxes with AvaTax on an invoice linked to a sales order with deliveries and pickings, Odoo now uses the warehouse address where the goods are shipped from to compute the most precise tax possible.

## Bank reconciliation layout

The bank reconciliation system has a new, clearer widget layout. Edit, delete, and print bank statements from the widget. Dashboard links are improved, and audit features can be found in the journal items view.

## Bank statement PDF report layout

The layout of the bank statement PDF report has been cleaned up.

## Bills artificial intelligence

Tax and account prediction on vendor bill lines are now always activated. Product prediction can be activated in the settings.

## Branches management

Manage business units/branches thanks to multi-company hierarchies.

## Credit and debit note buttons

Simplified the invoice action buttons. Debit notes was moved to the action menu.

## Cross analytic

Input on multiple analytic plans to do analytic cross-reporting.

## Credit limit improvement

Confirmed and uninvoiced sales orders are included in a partner's total receivables. The credit limit warning considers this new computation.

## Deferred expense/revenue report

The Deferred Expense/Revenue report allows auditing any amount. The audit can differ from the reported amount, as those are theoretical computations. Any difference means there is a manual entry to generate.

## Deferred management

The management of deferred entries is now distinct from assets. Create deferred revenues and expenses without setting up deferred models in advance.

## Delivery date

The delivery date is now a standard field on invoices.

## Down payment and POS

The breakdown of taxes and accounts on down payment invoices remains consistent, irrespective of whether the invoice is initiated through the PoS or the Sales App.

## Down payments tax breakdown

On down payment invoices, the tax breakdown of the original sale order is now respected.

## Early discount

Improved display of due dates for early payment discounts and installments.

## EDI format

Added the EDI format and Peppol fields to the customers list view.

## Expense receipts in journal entry attachments

Expense receipts are now attached to their respective journal entries. They are also automatically included in the Datev export for the German localization.

## Express VAT in local currency on invoices

Tax computation appears in local currency on customer invoices made in foreign currency to comply with the 2010/45/EU directive.

## Filter blank lines

Added option to filter out lines at zero from fiscal reports.

## Fleet: impact vehicle without a bill

For Fleet and Accounting users, the bank reconciliation widget now allows you to specify the vehicle concerned on any manual operation.

## Follow-up reports: missing contact info

When mass processing follow-up reports, contacts with missing information are isolated and do not block the process for other contacts

## Import matching number

Matching numbers have been simplified and are displayed with colors. Partial matchings have been improved, specifying which moves are partially matched with a proper identifier. You can now add a matching_number to your CSV import of lines. Odoo waits for all related account moves to be posted and tries to reproduce the reconciliation when that happens. If it fails, the imported reconciliation is discarded.

## Improve settings for tax calculation display on invoices

Merged Line subtotals tax display and Rounding Method in Accounting settings.

## Improved printed reports

Printed versions of accounting reports have been improved.

## Inter-company transactions - Attach a copy of the invoice PDF to the vendor bill

A copy of the invoice is now added to the bill attachment of the counterpart company in the scope of inter-company transactions.

## Invoice date visibility

The invoice date was added to journal items, journal entries, and some reports.

## Invoice layout overhaul

The invoice layout is clearer. To satisfy the legal requirements of several countries, you can display the total amount in letters.

## Invoice upload harmonization

Harmonized invoice uploads in both Accounting and Documents. Draft credit notes can be changed to invoices. Factur-X documents detect the move type (invoice or credit note) from the Factur-X data.

## Manual matching: partner creation

Improved partner creation on manual matching by prefilling both the partner name and VAT number.

## Manual reconciliation

The manual reconciliation widget was removed. Lines are silently reconciled unless a write-off entry is required, which launches a new reconciliation wizard.

## Mass download documents

Use the "send and print" download option to grab all documents from a selection of invoices. The download option on a single invoice now returns a zip file with all documents (PDFs and electronic invoices).

## Mass 'send and print': invoice banners

When an invoice is included in an asynchronous mass 'send and print' job, a banner is displayed on the relevant invoices to inform users that the job is in progress.

## Matching numbers rework

Matching numbers are color-coded in the Journal Items view. Partial matchings are uniquely identified to see which lines are part of the same partial matching.

## Miscellaneous operations on bank journals

Miscellaneous operations involving a bank account are highlighted on the Accounting Dashboard to improve auditability.

## OCR usability improvements

Document upload has been optimized: automatic digitization is now synchronous and five times faster. Error messages and warnings were improved.

## OCR: credit notes and refunds

Credit notes and refunds are automatically detected by the OCR and created as such.

## Payment scamming protection

To prevent users from sending money to potential scammers, vendor bank account numbers must be marked as trusted before they can be used to make an outgoing payment.

## Peppol global location identifiers

Add GLN (global location identifiers) to partners' delivery contacts for use with Peppol.

## Peppol onboarding

Easily send and receive invoices, bills, and credit notes by registering on the Peppol network.

## Ponto onboarding

The Ponto onboarding has been improved.

## Report loading speed

Introduced a new prefix group mechanism to improve the loading speed of accounting reports on large databases.

## Report sections

Reports can now be grouped on the user interface and in the exports.

## Reports rebirth

The interface design of accounting reports has been drastically improved and technically overhauled.

## Revamped send and print wizard

Users can select the relevant documents to be generated and the approvals to be requested from the "Send and Print" wizard. The electronic invoicing format is now configured on the customer.

## SAF-T: remove blocking errors

Warnings are displayed on the general ledger rather than when clicking the SAF-T export button.

## SEPA Direct Debit (pain.008.001.08)

Added support for the pain.008.001.08 format for SEPA Direct Debit.

## SEPA non-latin characters

SEPA characters mapping extended to cater to all European languages.

## Tax taxonomy

All localizations' taxes now use codes in their names to improve their display and usage in Odoo forms. Tax codes can be searched using shortcuts. The new Tax Description field contains longer descriptions of the taxes.

## Taxes: modification restriction and logging

Some fields on the Taxes model are now unmodifiable once the tax is used. Modifications done on some fields are tracked in the chatter.

## UBL/CII: handle payment terms

Improved UBL import with Cash Discounts and fixed taxes.

## User portal: invoices

Downloading an invoice from the portal downloads all available formats, including electronic invoices.

## User-friendly bank synchronization

Bank synchronization flows have been simplified. Buttons and alerts are displayed on the dashboard. Email notifications are sent to the account holder.

## Vendor bills import and purchase orders matching

When importing vendor bills from electronic invoicing systems supported by Odoo (e.g., UBL 3.0 invoices), Odoo now does partial purchase order lines matching and bill autocomplete for matching lines based on unit price and product name. The remaining non-matched lines are added separately on the vendor bill.

## VIES check

The output of the VIES check is displayed on the partner and can be overridden when necessary. For eCommerce flows, the check can be restrictive, preventing the client from obtaining an invoice on which the reverse charge has been applied.
