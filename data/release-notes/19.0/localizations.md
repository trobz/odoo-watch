---
version: "19.0"
app: "Localizations"
app_slug: "localizations"
source_url: "https://www.odoo.com/odoo-19-release-notes#table_of_content_heading_1_22"
item_count: 50
---

# Localizations — Odoo 19.0

## Argentina 🇦🇷

**Accounting:** Insert the legend "Operation subject to withholding" to invoices, credit notes, and debit notes PDFs of type A and M.
**Inventory:** A printed delivery guide (Remitos) and PDF adaptations to cover the digital delivery guide (Remitos Digitales) have been added.
**eCommerce:** Choose to show tax-excluded prices together with tax-included prices in eCommerce.

## Australia 🇦🇺

**Accounting:**

- Peppol PINT is supported.
- All types of BAS are supported.
- New taxes are available by default, including the luxury car tax, fuel tax credits, wine equalisation tax, PAYG income tax, and fringe benefit tax.
- BAS report sections are rounded down to the nearest dollar by default.
- The company's GST registration status is reflected in legal documents.

**Payroll:**

- Single Touch Payroll (Phase 2) and SuperStream are supported via a clearing house integration.
- All security requirements mandated by the ATO have been implemented.
- The 2025-2026 fiscal year tax rules were updated as of July 1, 2025.
- Varied withholding tax rates are supported (e.g., cents per km, laundry, domestic and overseas travel allowances, overtime meal allowance).
- Payroll taxes (W1 to W5) are included in the BAS report closing.
- Import YTD balances for an employee across multiple income stream types (e.g., "working holiday makers" and "salary & wages").
- Backpay and salary sacrifice any payments on a payslip.

## Bahrain 🇧🇭

**Accounting:** The base localization package has been added: chart of accounts, taxes, and two tax reports: full VAT return and simplified VAT return (available from 17.0).

## Belgium 🇧🇪

**Accounting:**

- A Belgian audit checklist is available.
- The annual statement is now available in XBRL format and is addressed to NBB.
- An integration has been added with CodaClean.
- Send Belgian VAT declaration to Intervat and MyMinFin via API.
- A non-deductible fiscal position is applied by default when creating a purchase receipt. This ensures that tax amounts on the receipt are treated as not deductible for the VAT declaration.
- A new activity type for the EC sales list and partner VAT listing has been added. An optional warning feature for users has been added and batch export from the "My Databases" page on odoo.com is supported.

**Payroll:**

- Automate multifunctional declarations (DMFA) and related changes through the secure file transfer protocol (SFTP) function directly in Odoo (available from 18.0).
- The Fiscal Voluntarism field can now be defined as a Euro amount, with a dedicated line in the salary rules.
- A new structure to manage salary advances has been added.
- The Dimona is now supported.

## Brazil 🇧🇷

**Accounting:**

- Add shipping information into the NF-e DANFE and XML.
- Electronic invoicing for goods sold to end consumers is supported via Avalara Brasil, with related PoS adaptations (available from 18.0).
- The operation type can be changed on any invoice or sales order line.
- The CNAE (National Classification of Economic Activities) code has been added within the NCM so different codes can be used on the invoice lines.
- Tax exception rules are supported, allowing configuration of tax rate reductions, special benefits, and similar cases.
- Goods electronic invoicing has been added for vendor bills and purchase refunds (credit notes).
- NFS-e (Services): Specify the place of service using the customer's delivery address.
- NF-e (Goods): Include the delivery address automatically when it differs from the customer's main address.

**Point of Sale:**

Send NFC-e in batch for PoS orders with Error AvaTax statuses. Export multiple NFC-e XML files from the PoS orders list view.

**Inventory:**

The CFOP field has been added to the operation types to provide more flexibility on customer invoices and vendor bills.

## Bulgaria 🇧🇬

**Accounting:** Sales and purchase ledgers are now downloadable from the tax report (available from 18.0).

## Cambodia 🇰🇭

**Accounting:** The base localization package has been added: chart of accounts, taxes, balance sheet, profit and loss report, T7 01 report, WT003 report, WT003 export, and generation of KHQR (available from 18.0).

## Chile 🇨🇱

**Accounting:** Add multiple cross-reference documents in a delivery guide and automatically add purchase order references from sales orders.

## China 🇨🇳

**Accounting:** The profit and loss and balance sheet reports have been updated (available from 18.0).

## Colombia 🇨🇴

**Accounting:**

- The DIAN module supports the generation of AIU Service invoices, providing the ability to invoice for administration and incidental costs and the contractor's expected profit according to legal requirements.
- Support has been added for RADIAN events, including sending and receiving Reception Acknowledgements, Receipts, Acceptances, and Claims.
- The DIAN's certification process is handled automatically, with required accepted documents generated and sent without manual configuration.

## Ecuador 🇪🇨

**Accounting:**

- The Sales and Subscriptions apps have been adapted to include the SRI Payment Method and automate the EDI flow from these apps.
- The EDI Dividends Withholding type of withholding can be recorded and sent to the government.
- Purchase withholdings are available for portal users. Generate a vendor bill by uploading the XML file of an invoice.

## Egypt 🇪🇬

**Accounting:** Expense accounts have been reworked and asset models have been added to improve user onboarding.
**Payroll:**

- The localization has been updated to include the calculations for annual leaves provision, sick leaves, unpaid leaves, remaining annual leave days compensation, out-of-contract days, and overtime.
- The tax exemption amounts and tax bracket percentages have been updated to match the Labor Law.
- Demo data has been added.

## European Union VAT

**Accounting:** A new EU VAT territory country group has been created to exclude some territories of Europe that are not subject to VAT (Canary Islands, Antilles) to improve the standard behaviour when invoicing to those territories.

## GCC countries

**Accounting:** The Gulf Cooperation Council modules have been revamped. Add Arabic as a secondary language on accounting documents, including POS receipts. Country-specific layouts have been updated and aligned with standard flows.

## Georgia 🇬🇪

**Accounting:**

- The National Bank of Georgia has been added as a currency exchange rate provider.
- State names and codes for Georgia have been added in compliance with the ISO 3166-2 standard.

## Germany 🇩🇪

**Accounting:** The structure of the German tax report has been improved.

## Hong Kong 🇭🇰

**Point of Sale:** A new payment terminal, QFPay, is available for Hong Kong.

## Hungary 🇭🇺

**Accounting:** Magyar Nemzeti Bank was added as a currency exchange rate provider. When sending a credit note to SPV that will fully revert an existing invoice, the credit note will be automatically sent as a Storno invoice.

## India 🇮🇳

**Accounting:**

- GST compliance has been improved with enhanced GSTR-1 reporting: supply types are locked on posting and stored on journal items, invoices can be filtered for reconciliation, and the mandatory reports have been updated.
- Generate a detailed TDS report with a single click, streamlining the preparation and filing of TDS returns.
- The GST return process has been simplified.
- TDS section and rate are now automatically detected, PAN records for multiple contacts are centralized, and real-time multi-company alerts are provided for missing PANs or threshold/exemption violations.
- Add the MSME number and the MSME type on the PAN Entity record.

**Payroll:**

The ESIC report has been added.

**Time Off:**

Flexi Leave is now fully supported with Optional Holidays, ensuring employees can only select from eligible days when using this leave type.

## Indonesia 🇮🇩

**Accounting:** eFakture templates are CSV instead of XML format. eFaktur ranges have been removed.

## Iraq 🇮🇶

**Accounting:** The base localization package has been added: chart of accounts and taxes (available from 17.0).

## Japan 🇯🇵

**Accounting:** Import batch payments and bank statements via Zengin.

## Jordan 🇯🇴

**Accounting:**

- An integration with JoFotara for e-invoicing has been added (available from 17.0).
- Non-Jordanian customer identification has been added to determine whether the customer is located in or outside Jordan (available from 17.0).
- A Demo mode has been introduced for internal validation testing (available from 17.0).
- Download the XML file for failed JoFotara submissions in developer mode.
- A restriction has been added to avoid deletion of the successfully submitted JoFotara PDF invoice. The error warning banner has also been improved.
- The tax report and taxes have been reworked.
- The import taxes are split into two taxes to account for the vendor base and customs VAT amount separately.
- Set the related invoice for an unlinked credit note for JoFotara submission.
- Support has been added for the Export and Development Area invoice types and the Cash payment method.

**Payroll:**

Calculations have been introduced for sick leaves, unused leave compensation, overtime, end of service, and related provisions. Demo data has been added.

## Kazakhstan 🇰🇿

**Accounting:** The National Bank of Kazakhstan has been added as a currency exchange rate provider.

## Kenya 🇰🇪

**Point of Sale:** Point of Sale is now compatible with eTIMS in Kenya.

## Korea 🇰🇷

**Accounting:** Added taxes, the chart of accounts, and base accounting reports for the Republic of Korea, including profit and loss, balance sheet, and tax report (simplified and general taxpayer).

## Lebanon 🇱🇧

**Accounting:** The base localization package has been added: chart of accounts, taxes, and fiscal positions (available from 17.0).

## Luxembourg 🇱🇺

**Payroll:** Support for CIM credit has been added (available from 18.0). The Other Benefit in Kind field has been added, along with its associated salary rules.

## Malaysia 🇲🇾

**Accounting:**

- Integration with Malaysia's LHDN MyInvois platform has been added (available from 17.0).
- Tax reporting has been improved. The existing SST-02 report now includes filters for custom and service codes, and the new SST-02A report is available.
- A QR code leading to MyInvois is embedded on invoice PDFs. Self-billing is now possible, including self-invoices, self-credit notes, and self-debit notes.

**Point of Sale:**

Submit e-invoices directly from PoS sessions. Generate, manage, and submit consolidated e-invoice for PoS orders not e-invoiced during the session (available from 18.0).

## Mexico 🇲🇽

**Accounting:**

- The 2025 version of the DIOT report is available to all databases, including new columns and tax classifications (available from 16.0).
- Accounts are set by default on tax groups to simplify monthly tax closing.
- Select the IEPS tax breakdown per customer to optionally include it in the XML. All eight tax objects are now supported and can be assigned to individual invoice lines.
- A default account for credit notes and re-invoicing of old orders can now be selected for clearer accounting. Customs numbers are added into lots and invoice lines are split accordingly.
- The payment policy (PUE/PPD) is now selectable per invoice.
- Add fiscal complements into the CFDI XML directly by upgrading the Addendas module into Addendas & Complements.
- Add pro-forma (pre-invoice) functionality for previewing invoices before they are created.
- Payment complements receipts can now be printed directly on the invoice, regardless of whether the payment was applied during a bank reconciliation or as a direct payment.

**Payroll:**

CFDI generation is supported, allowing XML files for employees to be created and validated by the government.

**Fleet:**

Carta Porte vehicles are now handled directly from Fleet and the PDF has been revamped.

## Netherlands 🇳🇱

**Accounting:** It is now possible to generate a corrective settlement XML file.

## New Zealand 🇳🇿

**Accounting:** Peppol PINT is supported.

## Oman 🇴🇲

**Accounting:** The base localization package has been added: chart of accounts, taxes, VAT return, and fiscal positions (available from 18.0). The import tax was split into two taxes to separately account for the vendor base and customs VAT amount (available from 18.0).

## Pakistan 🇵🇰

**Accounting:** Expense accounts have been reworked and asset models have been added to improve user onboarding. **Payroll:** Demo data has been added.

## Peru 🇵🇪

**Accounting:**

- Global and line-level discounts are now supported in UBL 2.1 XML electronic invoices, in line with the SUNAT guidelines.
- Support has been added for IGV Withholding (3%) on customer invoices. When an invoice includes this tax, the electronic invoice XML now automatically includes the required node with SUNAT code 62, allowing proper reconciliation with the customer's withholding document.

**Point of Sale:** SUNAT-compliant thermal printing has been added for Peruvian POS electronic invoices and receipts, generating legal electronic document representations (Factura/Boleta/Notas de Crédito) directly on 58/80 mm printers.

## Philippines 🇵🇭

**Accounting:**

- Form 2550Q (Quarterly VAT Return) has been revamped to align with the latest BIR regulations.
- Improvements have been made to the SLSP, QAP, and SAWT reports.
- Reports can now be generated in the official BIR format.
- Direct export of .dat files is now supported for SLSP, QAP, and SAWT. The exported files are compatible with the latest release of BIR's Alphalist and ReLiEf modules.
- Generate disbursement vouchers that include a section for signature and check number for improved payment tracking.

## Romania 🇷🇴

**Accounting:**

- eTransport declarations based on deliveries have been implemented (available from 17.0).
- A full synchronization with ANAF has been implemented.
- Invoices can be downloaded directly from the tax reports.
- Generate the D300 VAT report in XML format for submission to the tax authorities.

## Saudi Arabia 🇸🇦

**Accounting:**

- Documents rejected by ZATCA with a 400 status code are handled correctly (available from 16.0).
- Documents with a 409 or 208 status code from ZATCA are handled as successfully sent (available from 16.0).
- The common name used in the certificate signing request during journal onboarding has been reviewed (available from 16.0).
- The PDF/A-3 format is supported for ZATCA PDF documents (available from 16.0).
- The Issue Date and Invoice Date are clearly distinguished in the invoice PDF (available from 16.0).
- Onboarding branches with ZATCA are supported (available from 17.0).
- The private key and API mode of a parent company are no longer inherited by its branches, improving flexibility and ensuring compliance with ZATCA requirements (available from 17.0).
- Deletion of invoice PDFs generated via Send & Print is now restricted to comply with ZATCA auditability rules (available from 18.0).
- The Certificate Signing Request generation for ZATCA now includes both the major and minor versions for improved compliance (available from 18.0).
- The VAT and Withholding returns were overhauled to use the new reporting engine.
- Chart of accounts, taxes, and tax groups were reviewed and reworked.
- Complete support for the gross and deducted withholding taxes was added.
- The ZATCA integration UX has been improved with clearer error messages, updated API validations, and backend handling of journal serial numbers. Sandbox and simulation documents can now be sent.
- Choose a ZATCA compliant reason when issuing a credit or debit note.
- Invoices affected due to a timeout in ZATCA are automatically added to the synchronous chain once the blocked invoice is processed.
- Less common taxes such as 15% PH PE HS, 0% Not Subject to VAT, 0% IT G, and 0% QT have been removed to prevent selection errors. The base tax grids have been updated for 0% PE and 0% PH taxes to improve reporting compliance.

**Payroll:**

- Loan management and advanced salary payroll structure have been added. New rules have been added for sick leaves, unused leave compensation, exit/re-entry, and other employee costs.
- Support for attendance-based contracts has been improved, and salary rule management has been streamlined.
- Demo data has been added.

**Point of Sale:**

- The ZATCA Phase 2 QR code has been added on receipts to ensure compliance and error handling has been improved for failure scenarios (available from 18.0).
- The refund issuing flows has been improved.

## Singapore 🇸🇬

**Accounting:**

- Peppol PINT is supported.
- GST taxes have been refined to align with current governmental requirements and to prepare for future GST InvoiceNow document compliance.

## Slovenia 🇸🇮

**Accounting:** Bank of Slovenia has been added as a supported currency provider. Support has been added for Slovenian Payment Communication Standard SI 01; this is automatically set as the default on newly created Sales journals in a company using the Slovenian localization (available from 18.0).

## Spain 🇪🇸

**Accounting:**

- Modelo 140 Bizkaia and support for the SII cancellation workflow have been added (available from 16.0).
- The Libro Diario export was added to the general ledger and is now available via the journal audit report.
- The base localization package has been improved with additional default purchase accounts for common, everyday purchases, along with suggested default taxes.
- A new report dedicated to the Libro de IVA has been added.
- The Modelo 390 tax report was updated to the latest version published by the AEAT.
- Tax grids were updated for some taxes.
- The chart of accounts, taxes, and fiscal positions have been improved, including requirements specific to the Canary Islands.

## Sri Lanka 🇱🇰

**Accounting:** A new localization package is available for Sri Lanka, including the chart of accounts, taxes, balance sheet, profit and loss reports, VAT 001 report, and WHT 001 report.

## Switzerland 🇨🇭

**Payroll:** The BFS are directly fetched from the postal code (available from 17.0).

## Taiwan 🇹🇼

**Accounting:** An integration with the ECPay platform has been added for the issuance and official government submission of Taiwanese e-invoices (available from 18.0).

## Thailand 🇹🇭

**Accounting:** The sales and purchase tax reports have been reworked. The chart of accounts has been updated to comply with TFRS for NPAEs, introducing detailed expense accounts, asset models, and VAT accounts. Relevant default accounts, taxes, and tax groups have been updated accordingly.

## Türkiye 🇹🇷

**Accounting:**

- Support has been added for additional UNECE codes as Units of Measures for e-Fatura and e-Arşiv (available from 17.0).
- e-Fatura and e-Arşiv integration are now available via Nilvera (available from 17.0).
- Support has been added for currencies other than TRY for e-Fatura and e-Arşiv (available from 17.0).
- Deferred products can be used in subscription invoices, with support for e-Fatura and e-Arşiv (available from 17.0).
- Export e-Irsaliye XML from delivery orders and upload it to the Nilvera platform to generate GİB-compliant records (available from 17.0).
- The General Ledger can be exported in .csv format to generate the e-Ledger in Nilvera (available from 17.0).
- The total discount amount and exchange rate are displayed when sending electronic documents via Nilvera (available from 17.0).
- Documents sent via Nilvera now include additional company identifiers to ensure GIB compliance (available from 17.0).
- Invoice synchronization for the Nilvera integration has been improved.
- The Profit and Loss report has been improved to match the official format and the 700 series accounts are included for real-time financial reporting.
- The chart of account types has been updated and 7B accounts have been depecrated to ensure better GİB compliance.
- Verify the Nilvera status of multiple partners at once directly from the contacts list view.
- Pre-validation checks and other user experience improvements have been made to the Send wizard in the Nilvera integration for e-Fatura and e-Arşiv.
- The street fields have been combined into a single address line when generating the e-Fatura, e-Arşiv, and e-Irsaliye XML.
- Nilvera XML generation has been improved to display hyperlinks in notes cleanly, without reference brackets.
- e-Invoices with an Error status can be cancelled.

**Payroll:**

- Gross-to-net calculation has been improved to better fit market needs.
- Print certificates of employment.
- A new net-to-gross salary computation mechanism has been introduced.
- Demo data has been added.

**Inventory:**

- A warning has been added, and e-Dispatch generation is hidden if the delivery address isn't set on the delivery order. (available from 17.0).
- The Customs ZIP is now always applied when the delivery customer and address are outside Türkiye.

## United Arab Emirates 🇦🇪

**Accounting:**

- The amount in the company's currency has been added to the invoice PDF for foreign currency invoices to comply with FTA Article 59 (available from 16.0).
- The VAT201 form has been completely overhauled to use the new reporting engine with updated taxes and tax groups.
- The corporate tax report has been refactored to make it more intuitive and support the use cases of being under the 375,000 AED threshold or having a net loss.
- The import tax calculation has been updated to account only for the customs VAT amount.

**Payroll:**

- Salary computation has been added for attendance and planning-based contracts (available from 18.0).
- Instant payment structure has been added for advanced salaries, penalties, and bonuses that are paid on an off-cycle basis.
- Unpaid leave deductions are calculated based on working days, excluding public holidays.
- Generate employee salary certificates.
- The WPS export has been enhanced to better align with MoHRE regulations.
- Calculations for annual leave and end of service provisions have been improved.

## United States of America 🇺🇸

**Payroll:** The 940 and 941 forms are supported. Support has been added for qualified overtime deduction rules under the "One Big Beautiful Bill," including a new salary rule and parameters to display capped overtime deduction information on employee payslips.

## Uzbekistan 🇺🇿

**Accounting:**

- The base localization package has been added, including a localized chart of accounts, taxes (VAT 12%, Export 0%, Exempt 0%), and standard financial reports: balance sheet and profit and loss.
- The Central Bank of Uzbekistan has been added as a currency exchange rate provider.

## Vietnam 🇻🇳

**Accounting:** The balance sheet and profit and loss report were added (available from 18.0).
