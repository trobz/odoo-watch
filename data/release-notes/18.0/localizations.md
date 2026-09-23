---
version: "18.0"
app: "Localizations"
app_slug: "localizations"
source_url: "https://www.odoo.com/odoo-18-release-notes#table_of_content_heading_1725624803512_19"
item_count: 49
---

# Localizations — Odoo 18.0

## Argentina 🇦🇷

**Accounting:** Allow multiple checks when registering a payment. Improved VAT summary with additional details on taxes. The computation of withholding taxes has been automated. Improved withholding support on payment creation.

## Australia 🇦🇺

**Accounting:** Australian taxes have been cleaned up to better suit the market. TPAR taxes are now archived by default. Importers can now manage deferred GST (DGST) entries and related monthly BAS closing easily. Added support for tracking deferred GST. Added new "W" payroll sections to the BAS report. Added new flow to support other amounts withheld (W3).

**Payroll:**Complete Payroll revamp: Combined all rules in a single salary structure. Updated the new 2024-2025 tax schedule rates. Added the necessary code to submit official compliance tests for STP Phase 2 and SuperStream [Compliance in process]. Completely revamped other input types and super contributions. Added the possibility to import YTD balances for employees transitioning to Odoo Payroll. Completed child support and Medicare levy variation flows. Batch payments directly from a payslip batch, and reconcile them easily. Payroll is linked to Expenses and Accounting for Australian businesses. Termination payments: the whole of tax schedule 7 (from the ATO) has been implemented for unused leaves. Withholding variation can also now also be applied to unused leaves as per variation notice. Added support for Ordinary Time Earnings. Manage both super guarantee and concessional super contributions. Manage workplace giving and director fees.

## Bangladesh 🇧🇩

**Accounting:** The chart of accounts, fiscal positions, taxes, tax report, corporate tax report, and a list of states have been added.

**Payroll:** New localization including salary rules calculations, income tax credit handling, and income tax slab calculations.

## Belgium 🇧🇪

**Accounting:** The Individual Accounts report was improved and displays more content.

**Payroll:** Export work entries to Group S, Partena, and UCM. The end of the notice period is computed more accurately. Automate multifunctional declarations (DMFA) and related changes through the secure file transfer protocol (SFTP) function directly in Odoo.

## Brazil 🇧🇷

**Accounting:**Added the Operation Type to be selected on the invoice or sales order to support more CFOP cases. Implemented e-Invoicing and tax computation for services using Avalara Brazil. Set a default CNAE code on a company or select a specific one on a contact or invoice. Added the PIX payment method to collect payments. The eCommerce module has been adapted to work with taxes and EDI invoice issuance. Create vendor bills from an NF-e XML import. Electronic invoicing for goods sold to end consumers is supported via Avalara Brasil, with related PoS adaptations.

## Bulgaria 🇧🇬

**Accounting:**Added Bulgaria National Bank as an available currency rate provider. Sales and purchase ledgers are now downloadable from the tax report.

## Canada 🇨🇦

**Accounting:** Generate batch payments to vendors (EFT) through a CPA005 file.

## China 🇨🇳

**Accounting:** Added chart of accounts for large businesses in China.

## Colombia 🇨🇴

**Accounting:** Implemented e-Invoicing with DIAN. The eCommerce checkout process has been updated to make it compatible with the DIAN requirements on electronic invoices. Banco de la Republica de Colombia was added as a currency rate provider.

## Cyprus 🇨🇾

**Accounting:** Added the base localization package (chart of accounts, taxes, fiscal positions, balance sheet, profit and loss, and tax report).

## DACH

**Accounting:** The DIN5008 report for the DACH region is implemented in XML instead of Python, increasing flexibility when editing.

## Ecuador 🇪🇨

**Accounting:** Integrated purchase reimbursement flow. Integrated EDI invoice management with the eCommerce workflow. Portal contact information is now editable. Select the withholding base account to be used. Global discounts and negative lines on electronic invoices are supported.

## Egypt 🇪🇬

**Payroll:** Added EOS rules as per the latest updates, tax brackets to include 27.5%, and the value for the minimum taxable amount. Also added a new master payroll report which allows the user to create a sum of the payroll for each month.

## Estonia 🇪🇪

**Accounting:** Updated VAT for Estonia.

## Guatemala 🇬🇹

**Accounting:** Added Bank of Guatemala as a currency rate provider. Support has been added for Factura Especial (FESP), enabling automatic withholding of 100% VAT and ISR, generation of mandatory legal phrases, and FEL certification for purchases where the supplier does not invoice.

## Hungary 🇭🇺

**Accounting:** Implemented e-Invoicing (starting from 17 onwards). Synchronize received vendor bills directly from the NAV API; Odoo automatically fetches and updates received invoices based on the info in NAV.

## India 🇮🇳

**Accounting:** The ENet Payment CSV generator module allows to generate CSV files for vendor payments. Fetch vendor bills, credit notes, and debit notes from the GST portal.

**Payroll:** Rework of reports. Departments are now available on payslips.

**Time Off:** Set a time-off type as sandwich leave.

## Indonesia 🇮🇩

**Accounting:** Added Bank Indonesia as currency rate provider. The payment status via QRIS in the portal is now fetched. Added QRIS QR code to invoices on the portal. Improved e-Faktur range and document management.

**Payroll:** The localization has been added.

**Point of Sale:** Payment statuses for Bank QR QRIS transactions are fetched.

## Jordan 🇯🇴

**Accounting:** Added the base localization package: chart of accounts, taxes, tax report, and the list of states.

**Payroll:** New localization including basic salary calculations, tax income brackets, national contribution tax, and social security.

**Point of Sale:** Generate JoFotara-compliant receipts.

## Kenya 🇰🇪

**Accounting:** Now compliant with the new Kenyan ETIMS system, including the OSCU checklist.

**Payroll:** The master report has been added.

## Korea 🇰🇷

**Accounting:**The list of provinces and metropolitan cities has been added.

## Kuwait 🇰🇼

**Accounting:** The chart of accounts has been added.

## Luxembourg 🇱🇺

**Payroll:** Rework of the localization, improving monthly computation and gratification. Support for CIM credit has been added.

## Malaysia 🇲🇾

**Accounting:** Implemented e-Invoicing with Peppol PINT Malaysia. Added the statement of account report. Added Bank Negara Malaysia as a currency rate provider.

## Mauritius 🇲🇺

**Accounting:** The base localization package was added: taxes, fiscal positions, and tax report.

## Mexico 🇲🇽

**Accounting:** Improved XML invoice import: withholding taxes support, improved bill duplicate detection using the Folio Fiscal ID, invoices are marked as "to check" when a potential problem occurs during the import (such as bad tax detection). Simplified Addenda management. Implemented delivery guide update 3.1 (available from Odoo 15). You can edit the payment way to declare in the CFDI payment complement directly on a bank transaction (without needing a payment in between). Cuenta Predial values added on products are included in the products' CFDIs. Configure and add local taxes in the CFDIs generated in Odoo. The RegimenFiscal, if specific to a branch, is taken into account when emitting a CFDI, even if the certificate and the RFC number belong to the main company. The Complemento de Pago payment cancellation flow with replacement has been improved. Added the Complemento de pago generation for generic customers.

## Morocco 🇲🇦

**Accounting:** Export the tax report in XML format. The ICE (Identifiant Commun de l'Entreprise) is now displayed on invoices to ensure compliance with Moroccan regulations.

## New Zealand 🇳🇿

**Accounting:** You can now pay NZ suppliers faster by downloading batch payments in the EFT Batch Transfers format for the following banks: Westpac, BNZ, 8ANZ, ASB. Added Remittance Advice Report. Configure a start date for the fiscal period that is different from January 1st.

**Payroll:** The Employment Hero integration is now available in New Zealand.

## Nigeria 🇳🇬

**Accounting:** The base localization package was added: taxes, fiscal positions, tax report, and withholding tax report.

## Pakistan 🇵🇰

**Accounting:** The existing withholding taxes have been improved and new ones introduced. Two new tax reports are also available and the list of states has been added.

**Payroll:** New localization including basic salary calculations, tax brackets, and tax deductions.

## Peru 🇵🇪

**Accounting:** Added the detraction amount to the invoice's PDF report. Integrated EDI management with the Point of Sale order and eCommerce order workflows. The PLE 12.1 and PLE 13.1 inventory reports have been added for detailed inventory tracking. The PLE 1.1 and 1.2 reports have been added to track all cash transactions and current account operations, including inflows, outflows, deposits, withdrawals, and transfers. Support has been added for 19 sub-books of the Peruvian Inventory and Balances Electronic Book, including Trial Balance, Cash Flow, and specialized account reporting for SUNAT compliance.

## Philippines 🇵🇭

**Accounting:** Added new 2550Q (2023 version) tax report and SLSP report. The new standard check print layout has been implemented (available from 17.0). Withholding taxes and support for SAWT and QAP reports have been added.

## Qatar 🇶🇦

**Accounting:** The chart of accounts has been added.

## Romania 🇷🇴

**Accounting:** Implemented the E-factura sending to SPV, as well as the flow required to get Access Tokens from ANAF to use the web services. When downloading an invoice from ANAF, if the XML does not include a PDF, Odoo will download the official ANAF-generated PDF and use it as the attachment. Generate the SAF-T with Stock variant from the general ledger report. If an invoice is rejected by the SPV, it can now be reset to draft, corrected, and sent again.

## Rwanda 🇷🇼

**Accounting:** The base localization package was added: chart of accounts, taxes, fiscal positions, balance sheet, profit and loss report, and tax report.

## Saudi Arabia 🇸🇦

**Payroll:** Added a new master payroll report which allows the user to create a sum of the payroll for each month. The end-of-service calculations have been improved, and the GOSI calculations have been updated. Generate the SIF file as part of the Wages Protection System payroll process.

**Point of Sale:**The ZATCA PDF is no longer generated during order validation, avoiding unnecessary waiting time. It can be generated on demand when the invoice is first viewed or downloaded.

## Singapore 🇸🇬

Synchronize your journal entries to Odoo from Employment Hero (previously KeyPay).

## Spain 🇪🇸

**Accounting:** Added the possibility of filling in Invoicing Periods and changing Payment Means on invoices for Factura-e. Send vendor bills to the Batuz Tax Agency. Added new contact types on contacts for Factura-e Administrative Centers support. Added AEAT modelo 130. The Modelo 303 has been updated with the Q3 2024 changes from the AEAT. The TicketBAI implementation has been updated and is triggered on Send&Print. Point of Sale: TicketBAI allows to send Factura Simplificadas directly from sales orders without having to create separate account moves.

## SYSCOHADA

**Accounting:** Each of the 17 member countries of SYSCOHADA now has its own localization module. They all have their own taxes and tax report configured while having the common OHADA chart of accounts. The new NPFE-specific chart of accounts and industry-dependent reports have been implemented based on the SYCEBNL referential.

**Payroll:** New localization supporting basic calculation, tax income brackets, national contribution tax, and social security.

## Tanzania 🇹🇿

**Accounting:**The base localization package was added: chart of accounts, taxes, fiscal positions, tax report, balance sheet, and profit and loss report.

## Thailand 🇹🇭

**Accounting:** The Bank of Thailand has been added as a currency rate provider.

## Turkey 🇹🇷

**Accounting:** A default return from sales account is now defined in the sales journal and product form. New taxes and a new tax report have been introduced.

**Payroll:** New localization including social security premium/insurance calculations for employment and unemployment added to the salary rules; income tax calculations added, as well as stamp tax deductions for more accurate taxation results.

## Uganda 🇺🇬

**Accounting:** The base localization package was added: chart of accounts, taxes, fiscal positions, and tax report.

## United Arab Emirates 🇦🇪

**Accounting:** The corporate tax report has been added. Configure a start date for the fiscal period that is different from January 1st.

**Payroll:** A new master payroll report has been added. It allows calculating a sum of the payroll for each month. Generate the SIF file as part of the Wages Protection System payroll process. The salary rules have been updated to include provisions, social insurance, DEWS, out-of-contract days, remaining leaves balance payments, other inputs for bonuses, arrears, and other allowances. The EOS calculation has also been updated to take into consideration the free zones' calculations. The payslip printout formats have been updated, and the end-of-service printout format has been introduced.

## United Kingdom 🇬🇧

**Accounting:** Configure a start date for the fiscal period that is different from January 1st.

## United States 🇺🇸

**Accounting:** Companies can print their checks on blank check paper directly from Odoo without relying on a third party to pre-print their format. The tax created using the Avatax module features shorter tags and uses tax groups to improve the display. Added a compatibility module between the Amazon module and the Avalara tax computation.

**Payroll:** Display the accrued time in the payslip period on the printed payslip. Alabama, Nevada, Washington, and Colorado are now covered, including the workers' compensation for Washington State. Generate a CSV file with an overview of the hours worked and time off to import into ADP.

## Uruguay 🇺🇾

**Accounting:** Base localization package configuration updated (chart of accounts, LATAM module dependencies added). The DGI e-Invoicing via Uruware was implemented.

## Vietnam 🇻🇳

**Accounting:** The tax report has been updated. Integration with SInvoice for e-Invoicing has been implemented. The chart of accounts and balance sheet have been updated following Circular 99/2025/TT-BTC on corporate accounting guidelines.

**Point of Sale:**E-invoices can now be issued via SInvoice for POS orders, ensuring compliance with local tax regulations.

## Zambia 🇿🇲

**Accounting:** The base localization package was added: chart of accounts, taxes, fiscal positions, balance sheet, and profit and loss report.
