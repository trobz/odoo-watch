---
version: "19.0"
app: "Expenses"
app_slug: "expenses"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_41"
item_count: 4
---

# Expenses — Odoo 19.0

## Disallowed expenses: reverse amount percentage

Disallowed Expenses now use an “allowed percentage” instead of a “disallowed percentage" to account for potential >100% deductibility for expenses (which is now the case in Belgium). The Disallowed Expense Report now shows both amounts in those cases.

## Expense reports removed

Expense reports have been removed to better align with common usage, where most reports contained only a single expense. Users can still submit, approve, and post multiple expenses at once from the list view by selecting several expenses at once. For employee-paid expenses, posting multiple expenses at once will generate a single bill per employee.

## Partial bill deductibility

Configure purchase journals to register mixed expenses on a specific account (where part of the expense is made for private reasons and needs to be deducted from the company expenses). On purchase invoice lines, you can then change the Professional percentage at which that expense can be registered (the default is 100%).

## Physical expense cards

Physical expense cards issued through Mastercard and Stripe Issuing are now supported. All transactions made with these cards are automatically synchronized and recorded, ensuring accurate, real-time expense tracking and simplified reconciliation.
