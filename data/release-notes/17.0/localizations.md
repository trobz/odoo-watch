---
version: "17.0"
app: "Localizations"
app_slug: "localizations"
source_url: "https://www.odoo.com/odoo-17-release-notes#table_of_content_heading_1707731490324_64"
item_count: 46
---

# Localizations — Odoo 17.0

## Algeria

Accounting: improved the base localization (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, and tax report).

## Argentina

Accounting: added electronic vendor bills and liquidity product direct sales (liquido producto), both with the possibility to create electronic vendor bills and non-electronic sales invoices. Added the check management module to manage your own and third-party checks, and track checks to prevent users from paying with the same third-party check twice. POS: invoice electronically from the POS, in compliance with the AFIP requirements.

## Australia

Added the payroll localization: manage compliant contracts, assign different types of salary structures, compute superannuation guarantee and manage super accounts, generate compliant payslips and pay employees using ABA files. Added the link between Australian payroll, accounting and time off. Added ABA payment method for batch payments to banks. Added EFTPOS payment method for PoS via Stripe, and Buy-Now-Pay-Later payment methods via Stripe and Asiapay for eCommerce. Added PEPPOL e-Invoicing format. Added two new reports for partners: customer statements to send monthly to customers, and remittance advice to send to suppliers.

## Belgium

Accounting: Download CODA and SODA files directly from Codabox. Added the ability to import CODA files for countries other than Belgium. Implemented National Bank of Belgium's official Balance Sheets and Profit and Loss reports. Payroll: export to SD Worx is now a dedicated module. Display more cost-related information for company cars on the salary configurator. Representation fees are set on the job position.

## Brazil

Accounting: added the Central Bank of Brazil as a currency rate provider. Use different document types when creating customer invoices and vendor bills. Add identification types (CPF, CNPJ, etc.) in the same field when creating contacts; alphanumeric CNPJs are supported. Compute Sales Tax on sales orders and invoices using Avatax.

## Chile

Accounting: added new fields on the partner form and extra steps in eCommerce to allow users to generate eInvoices and eBoletas based on SII requirements. POS: create electronic invoices and Boletas with all the required legal information thanks to the addition of fiscal information on the contact form, which is editable directly from the POS session. eCommerce: users can create electronic documents from eCommerce, allowing customers to complete their fiscal information and choose the type of document.

## Colombia

Accounting: updated financial reports and taxes.

## Denmark

Accounting: implemented the SAF-T report and the new chart of accounts, and updated taxes accordingly.

## Dominican Republic

Accounting: updated localization, added financial and tax reports.

## Ecuador

Accounting: added the balance sheet and profit and loss reports. New withholding taxes are available that are based on the Resolución NRO. NAC-DGERCGC26-00000009.

## Estonia

Accounting: added the base localization package: chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, tax report, and IC supply report.

## France

Accounting: fiscal roundings added to tax report.

## Greece

Accounting: added the base localization package (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, and tax report).

## Hong Kong

Accounting: add FPS QR codes to invoices. Payroll: added the Manulife MPF report, salary rules support (Cap. 57), HSBC AutoPay report, IRD56 (B, E, F, and G) reports.

## Ireland

Accounting: added the base localization package (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, and tax report).

## Japan

Accounting: added support for Peppol PINT Japan.

## Jordan

Accounting: non-Jordanian customer identification has been added to determine whether the customer is located in or outside Jordan. Improved JoFotara credit note synchronization by refining the line-matching logic. Support has been added for "Transit," "Foreign Trade," and "Free Zone Transfer" invoice types. Point of Sale: improved JoFotara credit note synchronization by refining the line-matching logic.

## Kazakhstan

Accounting: added the base localization package (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, tax report).

## Kenya

Accounting: added withholding taxes and default accounts for POS. Configured Inventory valuation. Payroll: added the NHIF and NSSF reports.

## Latvia

Accounting: added the base localization package (chart of accounts, taxes, fiscal positions, and VAT report).

## Lithuania

Accounting: produce your Standard Accounting Data File (SAF-T).

## Malaysia

Accounting: improved chart of accounts and taxes. Added the SST-02 tax report.

## Mexico

Accounting: added the Month 13 Trial Balance variant and factura global. Improved the fiscal regime management of customers. Transformed the DIOT report into a tax report variant. Additional required fields for CFDI Invoices are now available on the eCommerce portal during order validation. Added a new step to the eCommerce order flow to let customers supply the required information for e-invoicing. Implemented the four cancellation reasons for CFDI invoices. Added support for Global Invoice sending, generated from the PoS orders or invoices list views. Added standard IEPS taxes. Set Usage and Payment Way fields on sales orders or set default values on partners to improve invoicing automation. Payroll: added monthly pay computation.

## Morocco

Accounting: improved the base localization (chart of accounts, taxes, fiscal positions, and financial reports). Payroll: added monthly pay computation.

## Mozambique

Accounting: added the base localization (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, and tax report).

## Netherlands

Payroll: added monthly pay computation.

## New Zealand

Accounting: added PEPPOL e-Invoicing format for Australia. Added two new reports for partners: customer statements to send monthly to customers, and remittance advice to send to suppliers.

## Peru

Accounting: added new reports (balance sheet, profit and loss report, sales book, purchase book, exportation purchase book, general ledger, partner general ledger, chart of accounts - in compliance with SUNAT requirements).

## Philippines

Accounting: updated the chart of accounts and taxes. Added the ability to export BIR 2307 reporting entries from vendor bills and payments.

## Poland

Accounting: implemented the tax report.

## Romania

Accounting: added balance sheet, profit and loss, and SAF-T (D.406 declaration) reports. Implemented eFactura (UBL with CIUS-RO). eTransport declarations based on deliveries have been implemented. The VAT rates and the VAT report have been updated. Support has been added for CPV codes on products in eFactura. Error handling during the ZATCA journal onboarding has been improved.

Payroll: added monthly pay computation.

## Serbia

Accounting: translated the chart of accounts and reports. Activated Storno accounting by default.

## Singapore

Accounting: added PayNow QR codes to invoices.

## Slovakia

Payroll: added monthly pay computation.

## SODA file import: account mappings

SODA import has been improved with an account mapping wizard that allows the user to register the mapping between the accounts provided in the SODA file and the accounts of the user's chart of accounts. Non-mapped accounts are created automatically. The mapping is saved for future imports.

## Spain

Accounting: added Factura-e invoice generation and signing. Implemented TicketBAI e-invoicing. If given, the company ID will be printed on invoices. This can be used to add a non-VAT customer reference on invoices (e.g., for intracommunity invoices to customers who do not have a VAT number). Export the VAT record books (Libros de IVA) files from the general tax report. Modelo 390 is available in the tax reports. Import Factura-e XML invoices in Odoo. Updated Exento taxes and added reporting compatibility (SII).

## Sweden

Accounting: import SIE Audit files.

## Switzerland

Payroll: added monthly computation, reports, insurances and canton rules.

## SYSCOHADA

Accounting: improved the base localization by revising the chart of accounts and financial reports.

## Thailand

Accounting: added PromptPay QR codes to invoices, tax invoice printout, purchase and sales tax report export, and PND3 and PND53 tax reports export as CSV for eFilling purpose.

## Tunisia

Accounting: added the base localization (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, and tax report).

## Türkiye

Accounting: Support has been added for additional UNECE codes as Units of Measures for e-Fatura and e-Arşiv.

## United Kingdom

Accounting: tax names were updated. The BACS file format is now supported for payments.

## United States

Accounting: added support for New York State taxes. Payroll: Added the Payroll localization. Form W-2 is supported.

## Venezuela

Accounting: implemented VAT validation on the Venezuelan TIN format.

## Vietnam

Accounting: added VietQR code to invoices.
