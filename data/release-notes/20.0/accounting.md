---
version: "20.0"
app: "Accounting"
app_slug: "accounting"
source_url: "https://www.odoo.com/odoo-19-2-release-notes#table_of_content_heading_1_20"
item_count: 32
---

# Accounting — Odoo 20.0

## **Conversion rates**

Conversion rates are now clearly displayed when registering payments in a foreign currency.

## **Exchange entries**

Exchange gains and losses are now consolidated into a single line per invoice, which can be expanded to view the calculation details.

## **Intuitive payment status**

Payment statuses have been renamed from "In Process" to "Paid" and from "Paid" to "Reconciled" to clarify the flow. The manual "Mark as Reconciled" button has been moved to the gear menu to encourage linking payments with real bank entries via the bank matching menu.

## **Multi-ledger consolidation**

Journals are now included instead of excluded in multi-ledger consolidation.

## **New currency: Caribbean Guilder**

The Caribbean Guilder (XCG) has been added to the list of supported currencies and is set as the default currency for Curaçao and Sint-Maarten (available from 18.0).

## **Peppol global location identifiers**

Add GLN (global location identifiers) to partners' delivery contacts for use with Peppol (available from 17.0).

## **Prevent double payments in the payment wizard**

To prevent double payments, the payment wizard now detects pending ("Paid") payments, automatically deducts them from the amount due, and sorts outstanding payments by date for a clearer timeline.

## **Simplification of asset models**

Asset models have been replaced by depreciation models, focusing specifically on the calculation logic of fixed assets. Furthermore, asset-related configurations and tracking have been consolidated: essential information and automated behaviors are located on asset accounts themselves.

## **Taxes in fiscal positions**

Taxes are only allowed in their respective fiscal positions, meaning that if a default tax on a product or account does not belong to the fiscal position set on an invoice, the tax is removed, even if there is no replacement.

## Accounting Firms mode settings

The "Accounting Firms mode" settings have been updated to increase their flexibility.

## Analytic distribution for write-offs

Define an analytic distribution when creating a write-off during reconciliation.

## Asset depreciation

Rates and float numbers can now be used when depreciating assets.

## Bill options display

Options added on a bill such as depreciation models, vehicles, and deferred payments are stacked vertically under the account instead of being displayed horizontally.

## Cumulative Translation Adjustment (CTA)

An auditable "Cumulative Translation Adjustment (CTA)" line has been added to the balance sheet, trial balance, and general ledger to automatically balance discrepancies caused by different exchange rate types (e.g., historical vs. closing) across account categories.

## Customer invoice reminders

Send customer invoice follow-ups manually via the invoice list view or via the "Send" button on the invoice form view. Automatic invoice reminders can be enabled and managed in the Accounting settings.

## Intercompany purchase order matching

When synchronizing sales orders, purchase orders, and invoices between companies, synchronized vendor bills are now automatically matched with synchronized purchase orders.

## Invoice email attachments

When sending an invoice by email, documents previously added to the chatter can now be easily added as email attachments.

## Manual reconciliation

Manual reconciliation can now be performed on any account. The "Allow Reconciliation" checkbox has been renamed "Payment Reconciliation;" this checkbox allows open items in that account to be suggested in the bank reconciliation view and determines if "Exchange Rate Difference" journal entries are expected upon reconciliation.

## Parent accounts

Account groups have been replaced by parent accounts as the method of structuring charts of accounts. Account codes are now optional.

## Pay bills from Odoo

Pay bills (individually or in batches) with a single signature directly from Odoo via the new PISP (payment initiation service providers) interface.

## Reset to Draft action in list views

In any list view, reset entries to draft in batch using the new "Reset to Draft" action.

## Annual report layout

Annual reports now use the company's document layout.

## Bill line prediction

When encoding a bill (manually or via import), Odoo suggests line elements based on the bill history and the label. The product, account, tax, analytic distribution and the vehicle will be automatically pre-encoded based on the best matches. Manually encoded values on existing lines are still preserved.

## Download invoice attachments

Download a zip file from the invoice list view with all the attachments that were generated for the selected invoices (PDF, XML, etc.).

## Improved duplicate detection

Invoice duplicate detection has been improved with two levels of warnings for invoices and bills: red invoices that are highly likely to be duplicates that should be corrected and yellow potential duplicates that should be investigated before posting. After posting, only red warnings will remain (available from 19.0).

## Invoice email attachments

When sending an invoice by email, documents from the Documents app can now be easily added as email attachments (available from 19.0).

## PAIN version setting

The PAIN version setting for outgoing payments has been moved from the journal level to the payment method level to offer more flexibility.

## Professional percentage for receipts

The "Professional" percentage column that was available for vendor bills is now also available for purchase receipts (available from 19.0).

## Purchase order matching

Vendor bill and purchase order matching has been improved, including the "Auto-Complete" option checking for matching bill lines before creating new ones; a clear summary of what has been matched and a warning if the price and quantity are different than expected; and the possibility to unmatch a vendor bill and purchase order.

## Run Auto Reconciliation

Manually retrigger the automatic bank reconciliation with the "Run Auto Reconciliation" option.

## Split items on invoices

Open an invoice's journal items from the smart button and select one or more lines to split. This improves handling of multiple quantities and asset creation, as well as splitting an amount across different accounts.

## Withholding tax on payment improvements

On bills that involve a withholding tax, the due amount is broken down to show the "Amount Due," "Withhold Due," and "Net Due." Additionally, a radio button in the payment wizard allows you to pay only the withholding amount, only the payment amount, or the total amount.
