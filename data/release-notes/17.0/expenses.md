---
version: "17.0"
app: "Expenses"
app_slug: "expenses"
source_url: "https://www.odoo.com/odoo-17-release-notes#table_of_content_heading_1707731490324_79"
item_count: 6
---

# Expenses — Odoo 17.0

## Accounting flow revamp

The accounting flow of expenses reports posting has been modified. An expenses report paid by an employee generates a vendor bill, and an expenses report paid by a company generates a payment instead of a purchase receipt. The synchronization between the Accounting and the Expense app has also been improved. The payment method used can now be specified for the expenses paid by the company.

## Default category

Specify a default category for automatically generated expenses.

## Expense report: payments

Expense reports paid by the company now generate as many payments as there are expenses in order to ease the reconciliation process.

## Expense report: improved PDF

The expense report PDF has been improved, and receipts are now attached.

## Forced amount in company currency

For expenses made in foreign currencies, employees can manually enter the amount they spent in company currency independently of Odoo exchange rates to match their real spendings perfectly

## Improve status consistency

Improved the pipeline stages of expenses and expense reports with consistent terminology. Clarified "to submit" versus "to report" and added tooltips to the expense dashboard.
