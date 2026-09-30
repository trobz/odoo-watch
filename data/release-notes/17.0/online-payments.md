---
version: "17.0"
app: "Online Payments"
app_slug: "online-payments"
source_url: "https://www.odoo.com/odoo-17-release-notes#table_of_content_heading_1707731490324_91"
item_count: 15
---

# Online Payments — Odoo 17.0

## Adyen partial payment capture

If you require customers to pay in advance or leave a guarantee, you can now capture part of the transaction amount and void the rest with the Adyen payment provider.

## Currency filter

Filter payment providers based on currency.

## Demo provider: express checkout

The Express checkout feature is now supported for the Demo provider.

## Demo provider: partial capture

The demo provider now supports the partial capture of payments.

## Fees currency

Define payment fees with a currency to guarantee the amount by converting it into the currency of the payment.

## Link payment methods with transactions

The payment method used by the customer is now saved on the payment transaction.

## Payment forms: payment methods display

Introduced the concept of payment methods in Odoo. Each payment provider is linked to a list of payment methods, which are displayed on payment forms.

## Payment link generation

The process of generating a payment link was simplified by using a single button to copy and generate the link.

## Public users payment with tokens

Allow users to pay with their saved payment methods without logging in.

## Razorpay: tokenization support

Razorpay now supports saving payment methods for future payments.

## Remove extra fees

Removed the extra fees feature (Paypal and Alipay).

## SEPA: pay once to create mandate

Ask customers to make a first payment to validate the SEPA mandate.

## Stripe

Customers can pay directly within the payment form (no redirection to Stripe). 26 new payments methods and Indian e-mandates are supported.

## Wire transfers: payment instructions

Add the possibility to regenerate the payment instructions with the available bank accounts for wire transfers.

## Xendit

Added the Xendit payment provider covering Indonesia and the Philippines.
