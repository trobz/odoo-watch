---
version: "20.0"
app: "Localizations"
app_slug: "localizations"
source_url: "https://www.odoo.com/odoo-19-1-release-notes#table_of_content_heading_1_21"
item_count: 106
---

# Localizations — Odoo 20.0

## Argentina 🇦🇷

**Accounting:** The VAT Book PDF report has been adapted to remove extraneous headers and footers, facilitating compliance with the legal requirement to copy the report into official, pre-numbered ledger books.

## Belgium 🇧🇪

**Payroll:**

- The Dimona is now supported.
- The "Joint Committee" object and all associated data have been added.

## Brazil 🇧🇷

**Accounting:**

- Generate NF-e for exportation of goods in BRL.
- Generate NFS-e for exportation of services in BRL.
- Import NFS-e PDFs and digitize them with OCR technology.
- A text link has been added to payment QR codes to allow customers to copy/paste them to their banking app.
- Batch download NF-e and NFS-e XML files from the list view.
- NFS-e (Services): Specify the place of service using the customer's delivery address (available from 19.0).
- NF-e (Goods): Include the delivery address automatically when it differs from the customer's main address (available from 19.0).
- New fiscal fields have been added to the Operation Type for both the issuer and recipient to better handle complex, non-standard ICMS ST and tax credit scenarios in NF-e and goods tax calculation.
- A breakdown of taxes applied to individual products is available in the sales order's and invoice's chatter so it can be easily shared with customers.

## Colombia 🇨🇴

**Accounting:**

- Detailed expense accounts and asset models have been added and localized to improve the onboarding experience.
- Electronic invoicing of free samples and promotional items is supported.
- The layout of fiscal PDF documents has been improved, and the QR code is visible on all pages.
- Electronic invoicing is now exclusively handled via the free DIAN connection; Carvajal is no longer supported.
- Type 3 Contingency invoicing is now supported, enabling fiscal document generation during extended DIAN service outages.
- Withholding certification reports no longer display the DIAN compliance message to reduce confusion.

## Egypt 🇪🇬

**Payroll:** Payslips include end-of-year income tax adjustments.

## France 🇫🇷

**Accounting:** The association-specific chart of accounts and report have been added.

## Hong Kong 🇭🇰

**Payroll:**

- Define an Internet fee and apply it to all employee payslips.
- Set an average daily wage (ADW) for employees.
- Calculate pre-transition and post-transition offset amounts for SP/LSP payments.
- Generate monthly MPF reports, create payroll groups/member classes, and define contribution periods for each employee.
- Define the month for end-of-year payments. Calculations are based on the number of previously generated payslips.

## Jordan 🇯🇴

**Accounting:** Error handling for sending invoices to JoFotara has been improved, now including validations for the supplier's country and TIN.

## Lithuania 🇱🇹

**Payroll:** Existing fields and other inputs have been converted to the new salary input flow.

## Luxembourg 🇱🇺

**Payroll:** The Decsal and Decmal reports are supported.

## Malaysia 🇲🇾

**Accounting:** Consolidated invoices can now be issued within the invoicing and accounting workflow.

## Mexico 🇲🇽

**Accounting:**

- On Global Invoices, bimonthly periodicity is now available, and the month is now selectable, making invoicing past months' orders easier.
- A cancellation acknowledgment can now be generated for cancelled CFDIs.
- Invoices with the external trade complement can now include services as well (available from 19.0).
- Minimum wage, tax rates, and UMA have been updated.

## Pakistan 🇵🇰

**Payroll:** Payslips include end-of-year income tax adjustments.

## Saudi Arabia 🇸🇦

**Accounting:**

- Expense accounts have been reworked, and asset models have been added to improve the onboarding experience.
- The invoice date now serves as the official issuing date, replacing the confirmation date (available from 17.0).

**Payroll:**

- Track employees’ disciplinary actions linked to payslip deductions.
- Identify late attendance and apply salary deductions accordingly.
- Integrate with the GOSI platform to retrieve contribution portions.
- The EOS computation has been improved to better align with the QIWA and Ministry of Labor regulations.

## Sri Lanka 🇱🇰

**Accounting:** A new localization package is available for Sri Lanka, including the chart of accounts, taxes, balance sheet, profit and loss reports, VAT 001 report, and WHT 001 report.

## Taiwan 🇹🇼

**Accounting:** The chart of accounts, balance sheet, and profit and loss statement have been updated (available from 19.0). **eCommerce:** ECPay integration is now supported to issue and submit Taiwanese e-invoices for eCommerce transactions (available from 18.0).

## Türkiye 🇹🇷

**Accounting:**

- Additional Invoice Scenarios (Basic, Export and Public), Invoice Types (Sales, Withholding, Tax Exempt, and Registered for Export), and Tax Offices have been added (available from 18.0).
- The street fields have been combined into a single address line when generating the e-Fatura, e-Arşiv, and e-Irsaliye XML (from 19.0).
- Nilvera XML generation has been improved to display hyperlinks in notes cleanly, without reference brackets (from 19.0).
- e-Invoices with an Error status can be cancelled (available from 19.0).
- CTSP validation has been restricted to invoices marked as "GİB Product Export Invoice" and the field label has been updated for clearer guidance.
- Commonly used Stamp Tax rates (0.948%, 0.189%, 0.759%) have been added and included in the Tax Report.

**Inventory:**

- Upload incoming e-despatch XML(s) from the Nilvera portal to create draft inventory receipts (available from 18.0).
- Tax office information has been added to the e-Dispatch XML to ensure compliance.

**Payroll:**

An advanced salary structure was introduced, supporting sick leaves, salary advances, and annual leave advance payments.

## United Arab Emirates 🇦🇪

**Accounting:** Expense accounts have been reworked, and asset models have been added to improve the onboarding experience. **Payroll:** The employee benefit contributions have been revised to better align with GPSSA & ADPF's regulations. Sick leaves are managed through a single salary rule and a single leave type.

## United States of America 🇺🇸

**Payroll:** Local taxes for New York City and Yonkers were added to the US Payroll localization.

## **Argentina 🇦🇷**

**Accounting:**

- The payment amount is automatically computed when using checks and withholdings on vendor payments (available from 18.0).
- Automatically sync with ARCA to fetch the official daily currency rate.
- The "Payment on Informed CBU" legend option has been added to comply with ARCA RG 5762/2025.
- Export the SICORE report file for Earning/Profit taxes.

## **Australia 🇦🇺**

**Accounting:** Bank synchronization now includes a new open banking integration through Basiq.

## **Belgium 🇧🇪**

**Payroll:**

- Add a maximum yearly remuneration to make an employee eligible for private car reimbursements.
- The Dimona flow has been automated.
- Automatically or manually add reorganization measures to working schedules based on content.
- Joint committees can now be part of a parent joint committee.

## **Brazil 🇧🇷**

**Point of Sale:** Cancel NFC-e from PoS orders.

**Accounting**: CST and calculation base amounts have been added to sales order and invoice lines in the tax details section.

## **Chile 🇨🇱**

**Accounting:**

- Detailed expense accounts and asset models have been added.
- The XML reader is now available for sales journals. Customer invoices can be imported via XML, for example, during go-live processes.
- Chilean commune data has been added, reducing manual entry errors when configuring addresses in the Contacts and eCommerce flows.

## **Colombia 🇨🇴**

**Accounting:**

- The user interface has been improved for a smoother experience and better error handling. Demo data has also been updated.
- Duplicate detection for vendor bills is now based on detecting CUFE duplicates.
- An example of the most common self-withholding tax and tax group has been added to the Colombian localization module. The default configuration now complies with DIAN requirements.
- The XML reader now supports withholding taxes and applies them as required on vendor bills.
- Generate exogenous information reports 1001, 1003, 1005, 1006, 1007, 1008, and 1009.

## **Ecuador 🇪🇨**

**Accounting:** Add a custom legend to the header of PDF reports for electronic documents for cases such as exporters and NGOs.

**Point of Sale:**The Point of Sale app now blocks sales above the legal limit when using the default "Consumidor Final" customer, requiring selection of a real customer for compliant invoicing.

## **Egypt 🇪🇬**

**Payroll**: Export formats for From 1 and Form 6 are available for the National Organization for Social Insurance (NOSI).

**Accounting:**Expense account descriptions have been added.

## **Guatemala 🇬🇹**

**Accounting:**Support has been added for Factura Especial (FESP), enabling automatic withholding of 100% VAT and ISR, generation of mandatory legal phrases, and FEL certification for purchases where the supplier does not invoice (available from 18.0).

**Point of Sale:**The Point of Sale app has been updated to comply with local electronic invoicing requirements, including mandatory validations and data needed for proper FEL/DTE issuance (available from 19.0).

## **Hong Kong 🇭🇰**

**Payroll:**

- Generate IR56B/E/F/G tax forms in XML and PDF format in compliance with the Inland Revenue Department (IRD) technical specifications.
- HSBC Autopay has been integrated directly into the standard reporting workflow. Select it as an export format and configure any Autopay account for any report.

## **Indonesia 🇮🇩**

**Accounting:** The chart of accounts and asset list have been updated to include detailed expense accounts and localized asset models.

## **Jordan 🇯🇴**

**Point of Sale:** Generate JoFotara-compliant receipts (available from 18.0).

## **Kazakhstan 🇰🇿**

**Accounting:** The National Bank of Kazakhstan has been added as a currency exchange rate provider (available from 19.0).

## **Mexico 🇲🇽**

**Accounting:** Factoring payments have been added in the bank reconciliation view.

**Payroll:** When a new payslip is generated, the email sent to the employee now also includes a link to the Comprobante Fiscal Digital por Internet (CFDI) in XML format (available from 19.0).

## **Pakistan 🇵🇰**

**Accounting:**Expense account descriptions have been added.

## **Peru 🇵🇪**

**Accounting:**

- Support has been added for 19 sub-books of the Peruvian Inventory and Balances Electronic Book, including Trial Balance, Cash Flow, and specialized account reporting for SUNAT compliance (available from 18.0).
- Support has been added for IGV Withholding (3%) on customer invoices. When an invoice includes this tax, the electronic invoice XML now automatically includes the required node with SUNAT code 62, allowing proper reconciliation with the customer's withholding document.

## **Philippines 🇵🇭**

**Accounting:** The format of the partner ledger report now complies with the Bureau of Internal Revenue (BIR) requirements. The Book of Accounts has been added for CBA and CAS compliance in the Philippines.

## **Romania 🇷🇴**

**Accounting:**

- Support has been added for CPV codes on products in eFactura (available from 17.0).
- The VAT rates and the VAT report have been updated (available from 17.0).
- When downloading an invoice from ANAF, if the XML doesn't include a PDF, Odoo will download the official ANAF-generated PDF and use it as the attachment (available from 18.0).
- Select a period when manually synchronizing invoices with ANAF.

## **Saudi Arabia 🇸🇦**

**Accounting:**

- Error handling during the ZATCA journal onboarding has been improved (available from 17.0).
- The Additional Identification Number field is now available for non-Saudi contacts, in compliance with the BR-KSA-81 ZATCA rule (available from 18.0).
- Identification Scheme and Identification Number are now also used to distinguish between a company (TIN, CRN, MOM, MLS, 700, SAG, OTH) and an individual contact (NAT, GCC, IQA, PAS) (available from 19.1).
- The "Is Retention" checkbox has been removed, and a negative sales tax is now automatically classified as a retention tax.
- Expense account descriptions have been added.
- States have been adapted to reflect the 13 subdivisions.
- Demo data has been improved.

**Point of Sale:**

Support for down payments has been enhanced (available from 18.3).

## **Taiwan 🇹🇼**

**Accounting:**Taxes and tax reports 401, 403, and 404 have been updated. ECPay e-invoicing details can now be specified directly on quotations and sales orders for B2C transactions, allowing information to be collected earlier in the sales flow.

## **Thailand 🇹🇭**

**Accounting:**

- The chart of accounts has been updated to comply with TFRS for NPAEs, introducing detailed expense accounts, asset models, and VAT accounts. Relevant default accounts, taxes, and tax groups have been updated accordingly (available from 19.0).
- The P.P.30 VAT return report can now be exported as a CSV file compatible with the Thai Revenue Department's RD Prep software for monthly filing.
- The Company ID label has been updated and repositioned to clarify its use as a branch code, alongside new input validation.
- Taxes, tax groups, and fiscal positions have been expanded, adding new withholding types and enabling cash basis by default for services. Related descriptions have also been translated.

## **Türkiye 🇹🇷**

**Accounting:**

- Synchronization with Nilvera has been improved to ensure all eligible invoices and bills are retrieved regardless of date or record limits (available from 19.0).
- Subscription e-Invoice handling has been improved. Document-level start and end dates are now automatically derived from subscription lines, allowing mixed invoices while preserving validation for conflicting periods.
- Return and withholding return invoice types are supported through credit notes.
- Reason code 702 on Registered for Export invoices is now supported, including Customer and Seller Line Codes per invoice line.
- The e-Dispatch integration has been enhanced by enabling the mapping of one or multiple related dispatch documents to an invoice, ensuring dispatch orders are reflected in the XML.
- Send and receive e-Dispatch documents via the existing Nilvera API connection thanks to improved e-Dispatch integration.

**Payroll:**

Calculate severance pay in line with Türkiye's labor laws.

## **United Arab Emirates 🇦🇪**

**Accounting:**

- Generate the Federal Tax Authority (FTA) VAT audit file from the general ledger (available from 19.0).
- Expense account descriptions have been added.

**Payroll:**

Treatment of DIFC Employee Workplace Savings (DEWS) contributions has been adapted to align with Dubai International Financial Centre (DIFC) regulations.

## **United States of America 🇺🇸**

**Accounting:** Each pre-configured asset model now has dedicated depreciation and expense accounts, replacing the previous use of shared generic ones.

**Payroll:** Support has been added for qualified overtime deduction rules under the "One Big Beautiful Bill", including a new salary rule and parameters to display capped overtime deduction information on employee payslips (available from 19.0).

## **Vietnam 🇻🇳**

**Accounting:**

- The chart of accounts and balance sheet have been updated following Circular 99/2025/TT-BTC on corporate accounting guidelines (available from 18.0).
- The Tax Declaration Form 01/GTGT report has been added to ensure compliance with local tax regulations.

## Argentina 🇦🇷

**Inventory:** Use batches and mass process Remitos Digitales.

## Bahrain 🇧🇭

**Accounting:** State codes have been updated to comply with the ISO 3166-2 standard.

## Belgium 🇧🇪

**Payroll:**

- The monthly salary structures have been merged into a single "Regular Pay" structure, with adapted rules for students and PFI.
- Remuneration for company directors is now supported.
- Temporarily dismisswarnings in the Payroll dashboard without discarding them permanently.
- New reporting has been added for meal voucher ordering.
- Configure the employee's contribution per meal voucher.
- Payslip computation for CP302 Flexi-Jobs (FLX) is now supported.
- The 7.67% holiday pay and the 28% employer contribution are automated.
- The annual earning caps (including 2026 updates) are monitored to trigger withholding taxes and ensure DMFA/Fiscal compliance.

## Brazil 🇧🇷

**Accounting:** "Customer Order Number" and "Customer Order Number ID" are now included on Avalara requests and sales orders.

## Canada 🇨🇦

**Accounting:** Detailed expense accounts have been added and asset models have been reworked and localized to improve user onboarding.

## Chile 🇨🇱

**Accounting:**The DTE email server and XML reader now support non-billable amounts on invoices.

## China 🇨🇳

**Accounting:**

- The chart of accounts, balance sheet, and profit and loss statement have been improved (available from 19.0).
- Asset models have been added according to China Corporate Income Tax Regulations Article 60 (available from 19.2).
- Parent accounts have been updated for maintaining parent-child account hierarchy.

## Colombia 🇨🇴

**Accounting:**Mandate invoices can now be created for goods as well as services. In addition, multiple principals are now allowed and are assigned correctly to journal items.

## Dominica Republic 🇩🇴

**Accounting:**Electronic invoicing is now supported (e-CF types 31-34), with XML generation and submission to DGII via Infile.

## Ecuador 🇪🇨

**Accounting:** New withholding taxes are available that are based on the Resolución NRO. NAC-DGERCGC26-00000009 (available from 17.0).

## Egypt 🇪🇬

**Accounting:**

- The abolished Helwan and 6th of October states have been removed and existing records have been migrated to Cairo and Giza to reflect the current administrative structure.
- Building Number and Street 2 are now visible on the Company and Contact forms, respectively.

**Payroll:**

- Calculations for overtime have been improved.
- Support has been added for exporting NOSI Form 2 (social insurance declaration) and ETA Form 2 (payroll tax reporting) in compliance with Egyptian regulatory requirements.

## Georgia 🇬🇪

**Accounting:** The National Bank of Georgia has been added as a currency exchange rate provider (available from 19.0).

## Guatemala 🇬🇹

**Accounting:**FEL documents can now be cancelled directly via Infile. The cancellation reason is recorded and the document is marked as "Anulado" in SAT.

**eCommerce:**Added support for electronic invoicing, including issuer phrases and allowing invoices to be issued to final consumers (CF).

## Hong Kong 🇭🇰

**Payroll:**

- A new "Rentals" system has been introduced to manage the end-to-end rental process. Employees can submit rental requests and monthly proofs of payment directly via the Employees app, replacing manual forms and external spreadsheets. The system supports various Hong-Kong specific scenarios, including direct employer payments and employee-led contributions, while centralizing all compliance documentation for HR review.
- Define a minimum duration of consecutive leave (e.g., 4 days for paid sick leave) to automate eligibility for the 80% ADW leave types and prevent invalid requests.
- Daily, weekly, bi-weekly, and semi-monthly pay schedules have been added. Salary rules for MPF and fixed allowances automatically scale to the selected period, ensuring compliance with Hong Kong statutory thresholds for non-monthly earners.
- A new salary structure is available for casual employees in the catering and construction industries, supporting specific MPF Industry Scheme rates.

## Iraq 🇮🇶

**Payroll:** The base payroll localization has been added, including monthly pay salary structure, social insurance, leaves setup, end of service benefit calculation, and overtime rates calculations.

## Jordan 🇯🇴

**Accounting:** Improved JoFotara credit note synchronization by refining the line-matching logic (available from 17.0).

**Point of Sale:** Improved JoFotara credit note synchronization by refining the line-matching logic (available from 17.0).

## Kuwait 🇰🇼

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard.

## Lebanon 🇱🇧

**Accounting:** State codes have been updated to comply with the ISO 3166-2 standard and duplicate state entries have been removed.

## Malaysia 🇲🇾

**Point of Sale:**Self-service e-invoicing via MyInvois is now possible.

## Mexico 🇲🇽

**Accounting:**

- A new localized balance sheet report has been added based on the NIF B-6.
- A new localized profit and loss report has been added based on the NIF B-3.
- Complementary trial balance XML reports can now be generated.

**Inventory:**

The driver for a bill of lading can now be selected directly in the delivery order, allowing for easier driver switch.

## Oman 🇴🇲

**Accounting:** State codes have been updated to comply with the ISO 3166-2 standard.

## Pakistan 🇵🇰

**Accounting:**State names and codes have been updated to comply with the ISO 3166-2 standard.

## Peru 🇵🇪

**Point of Sale:**SUNAT-compliant thermal printing has been added for Peruvian POS electronic invoices and receipts, generating legal electronic document representations (Factura/Boleta/Notas de Crédito) directly on 58/80 mm printers (available from 19.0).

## Qatar 🇶🇦

**Accounting:**State names and codes have been added in compliance with the ISO 3166-2 standard.

## Romania 🇷🇴

**Accounting:** Generate the SAF-T with Stock variant from the general ledger report (available from 18.0).

## Saudi Arabia 🇸🇦

**Accounting:**

- ZATCA synchronization has been integrated into the "Send" wizard, with pre-check validations shown in a banner; synchronization history is recorded in a new ZATCA tab upon sending. Batch processing through the list view is now supported.
- Invoice reports have been updated to include a line-level "Discount Amount" column, and the "Amount Due" label has been changed to "Invoice Total Payable Amount."

**Payroll:**

- Issue advance salary payments when an employee takes annual leave.
- Sync attendance records with the ZKTeco BioTime Cloud integration.
- Calculations for annual leave and end of service provisions have been improved.
- Calculations for overtime have been improved.

**Point of Sale:**

The ZATCA PDF is no longer generated during order validation, avoiding unnecessary waiting time. It can be generated on demand when the invoice is first viewed or downloaded (available from 18.0).

## Singapore 🇸🇬

**Accounting:** GST taxes have been refined to align with current governmental requirements and to prepare for future GST InvoiceNow document compliance (available from 19.0).

## Türkiye 🇹🇷

**Accounting:**

- Tooltips have been added to Nilvera e-Invoice fields to improve clarity.
- State codes have been updated to comply with the ISO 3166-2 standard.
- The 351 code exemption reason has been added as default on sales invoices when 0% VAT is applied on an invoice line.
- 35 new accounts have been added and account types 27 and 28 have been updated to Fixed Assets.
- Parent accounts have been introduced and linked to corresponding sub-accounts in accordance with GIB’s 7/A chart of accounts.
- A new synchronize button in journal entries allows the Nilvera status to be updated for each invoice.

## United Arab Emirates 🇦🇪

**Accounting:**The chart of accounts has been redesigned to comply with IFRS and UAE Commercial Companies Law. It features a scalable 6-digit numbering system and reverse-liquidity sequencing, and includes statutory equity reserves, essential technical accounts (WIP, Goods in Transit), and parent account groups.

**Payroll:**

- A new "Emiratization Compliance" report has been introduced to track Emiratization percentages in line with MoHRE regulations.
- Non‑salary employer cost items (e.g., insurance, work permits, visa processing fees) are now supported, improving labour cost visibility.
- The WPS export has been enhanced to better align with MoHRE regulations (available from 19.0).
- Calculations for annual leave and end of service provisions have been improved (available from 19.0).
- Calculations for overtime have been improved.
- The plane tickets benefit calculation has been added to the salary rules.

## United States 🇺🇸

**Accounting:** A new integration method for AvaTax is available: "Avalara Included." This integration offers a more affordable option for small and medium-sized businesses, while maintaining full tax computation capabilities for the United States and Canada.
**Payroll:**Support for Tennessee, Iowa, Georgia, Mississippi, and New Jersey has been added, including state-specific tax rules and payroll configurations.

## Uzbekistan 🇺🇿

**Accounting:**

- The base localization package has been added, including a localized chart of accounts, taxes (VAT 12%, Export 0%, Exempt 0%), and standard financial reports: balance sheet and profit and loss (available from 19.0).
- The Central Bank of Uzbekistan has been added as a currency exchange rate provider (available from 19.0).

## Vietnam 🇻🇳

**Accounting:**

- Electronic Internal Transfer Notes can now be issued via SInvoice.
- Parent accounts can now be used to structure the chart of accounts, allowing child accounts to be grouped for reporting and visualization.
- Appendix 142 has been added to Tax Declaration Form 01/GTGT to ensure compliance with local tax regulations.

**Point of Sale:**

- E-invoices can now be issued via SInvoice for POS orders, ensuring compliance with local tax regulations (available from 18.0).

## Argentina 🇦🇷

**Accounting:** When a "Pre-Printed Journal" is selected for printing, a warning message clarifies that headers and footers are intentionally omitted from the printed PDF; such documents are typically printed on corporate stationery.
**Inventory:** The vendor's Remito (Delivery Guide) number can now be entered manually on receipts.

## Belgium 🇧🇪

**Payroll:** End-of-year bonus computation for CP302 is now supported.

## Brazil 🇧🇷

**Accounting:**

- Avalara's CST classification for ICMS, PIS, COFINS, and IPI can now be manually overwritten, if needed.
- Alphanumeric CNPJs are now supported, in line with the 2026 tax reform (available from 17.0).
- The "cClassTrib" field has been added to the Taxes Settings tab of operation types, allowing users to override the default Avalara tax classification code when submitting electronic invoices.

## Chile 🇨🇱

**Inventory:** Copies of the delivery guide for yielding purposes are now supported, complying with the SII layout requirements.

## Colombia 🇨🇴

**Accounting:**

- XML generation of invoices that include global discounts and loyalty features (i.e., negative lines) is now supported.
- Vendor bills can now be imported to purchase journals using the official ZIP file.

## Ecuador 🇪🇨

**Accounting:**

- The chart of accounts has been improved by removing duplicate account names and types for a cleaner and more accurate financial structure.
- The display of the address and customer information on the invoice PDF has been improved.

## Egypt 🇪🇬

**Accounting:**

- Obsolete schedule taxes and other taxes have been removed and the related reports deleted.
- The VAT return and withholding reports have been updated to ensure ETA compliance.
- Withholding taxes can now be managed using the new "Deducted Withholding" and "Gross Withholding" (gross-up) flows to handle both standard deductions and net-of-tax agreements.
- The standard chart of accounts has been updated to implement a scalable 6-digit structure and group parent accounts based on reverse liquidity sequencing. Default account mappings have been improved for deferred revenue, deferred expenses, and expense accounts, while account names have been updated to align with standard Egyptian market terminology.
- The unit of measure codes have been updated to match the latest ETA regulations.
- The "Street" and "Street 2" fields of partner addresses are concatenated into a single payload string to ensure all address details are included during ETA synchronization.

**Payroll:**

A calendar-day working schedule has been added to support payroll and leave calculations based on calendar days.

## France 🇫🇷

**Accounting:** The VAT submission screen has been enhanced to offer a better user experience.

## Georgia 🇬🇪

**Accounting:**State names and codes for Georgia have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Hong Kong 🇭🇰

**Accounting:** The chart of accounts and the profit and loss and balance sheet reports have been updated to ensure full compliance with the HKFRS for Private Entities (PEs).
**Payroll:**

- The IR56M report is now available, as well as a new salary structure for non-employees such as contractors, freelancers, artists, etc.
- IR56 reports now support adding a different postal address to the employee's private address.
- A warning for the new "468 Rule" is shown when employees on non-continuous contracts approach or meet continuous contract thresholds.
- Customized salary rules are now automatically mapped with IRD reports (IR56B, IR56E, IR56F, IR56G, and IR56M) through the use of pre-defined categories.

## Hungary 🇭🇺

**Accounting:**

- Generate an A60 statement, the Hungarian-specific EC sales list (available from 19.1).
- Synchronize received vendor bills directly from the NAV API. Odoo automatically fetches and updates received invoices based on the info in NAV (available from 18.0).

## Indonesia 🇮🇩

**Accounting:**

- Multiple improvements have been made to the contact form, including removing the "Is PKP" field and merging the "NIK" and "NPWP" fields.
- A new tax and tax group have been added for compliance with the PPN Dipungut mechanism.

**Payroll:**

- Default accounts are now set for standard payroll rules.
- Overtime calculation (PP No. 35/2021) - overtime components are now excluded from the basic salary calculation and are instead processed under a separate rule.

## Jordan 🇯🇴

**Accounting:** Support has been added for "Transit," "Foreign Trade," and "Free Zone Transfer" invoice types (available from 17.0).

## Kuwait 🇰🇼

**Payroll:** The base localization package has been added, including regular pay, social insurance calculations, end-of-service and provision calculations, and leaves setup.

## Malaysia 🇲🇾

**Accounting:** MyInvois is now supported across branches, with improved handling for sole proprietorships.

## Oman 🇴🇲

**Payroll:**

- The base localization package has been added, including regular pay, social insurance, end-of-service and provision calculations, leaves setup, overtime rules, and employer net cost calculations.
- Support for generating Wage Protection System (WPS) files has been added to facilitate salary payments and reporting in compliance with Omani legal requirements.

## Pakistan 🇵🇰

**Accounting:**

- The standard chart of accounts has been updated with parent groups to ensure automatic account roll-ups, enable section-by-section trial balance reporting, and simplify compliance with the Companies Act 2017.
- The balance sheet and profit and loss statement are now generated dynamically using chart of accounts prefixes, rather than using legacy prefix mapping.
- The chart of accounts has been updated and outdated VAT and withholding reports have been removed to prepare for upcoming FBR Form-7 compliant reporting.
- Tax configurations have been streamlined by consolidating obsolete taxes into statutory sales tax, further tax, and withholding tax pillars to align with the Sales Tax Act.

## Peru 🇵🇪

**Accounting:**

- A GRE can now be generated natively for internal transfers, with the operation type field visible and set to "11 - Transfer Between Warehouses" by default.
- Electronic vendor withholding documents can now be created with their corresponding XML, CDR, and PDF files.

## Philippines 🇵🇭

**Accounting:**

- Generate and download official PDF certificates for specific partners and date ranges using newly added report variants for BIR 2306 (Final Withholding Tax) and BIR 2307 (Expanded Withholding Tax).
- Differentiate between individuals and companies with the "Entity type" field. An information banner appears on Philippine reports that include a contact without a set entity type.
- Generate BIR 2306 and BIR 2307 withholding tax certificates on vendor bills.
- A new disbursement voucher has been added for internal company use.

**Payroll:**

- The basic Philippines payroll package is available with mandatory calculations for basic pay, benefits, taxes, overtime, etc.
- Support has been added for Form 1601-C items for BIR monthly payroll reporting.
- The yearly BIR Form 2316 tax report has been added.

## Romania 🇷🇴

**Accounting:**

- Generate the D300 VAT report in XML format for submission to the tax authorities (available from 19.0).
- If an invoice is rejected by the SPV, it can now be reset to draft, corrected, and sent again (available from 18.0).

## Saudi Arabia 🇸🇦

**Accounting:**

- Less common taxes such as 15% PH PE HS, 0% Not Subject to VAT, 0% IT G, and 0% QT have been removed to prevent selection errors. The base tax grids have been updated for 0% PE and 0% PH taxes to improve reporting compliance (available from 19.0).
- Add multiple partner identifiers, including Saudi-specific Identification Schemes like the Saudi national ID number, Iqama number, or GCC ID number, using the multi-ID feature on a partner's contact form.
- Define invoice types ("Tax" or "Simplified") and transaction types ("Export," "Summary," or "Nominal") directly on the invoice form to explicitly control API routing (B2B versus B2C).
- A new "Supply End Date" field has been added to generate simplified nominal invoices and to record continuous supplies and multiple deliveries.
- Configure tax exemption reasons using standard UBL tax category fields to simplify and declutter tax setup. Support has been added for free-text exemption reasons when recording services outside the scope of tax (VATEX-SA-OOS).
- ZATCA address compliance has been improved by restricting the "Building Number" and newly renamed "Secondary Number" (formerly "Plot Identification") fields to exactly four numerical digits, preventing XML validation errors (BR-KSA-37) during submission.
- The duplicate "Supply Date" field has been removed from the invoice form header to avoid confusion, keeping it accessible only within the "Other Info" tab.

**Payroll:**

- The calculation for end of service provisions has been updated to better support termination cases under Article 77 of the labor law.
- Compute the total end-of-service benefit liability for one or more employees at any point in time using the End-of-Service Benefit report.
- A calendar-day working schedule has been added to support payroll and leave calculations based on calendar days.

## Singapore 🇸🇬

**Accounting:** Tax invoice, credit note, and customer accounting PDF reports have been added to comply with the Inland Revenue Authority of Singapore (IRAS) GST requirements.

## Sri Lanka 🇱🇰

**Accounting:** The format of the VAT report has been improved to display data more clearly.

## Thailand 🇹🇭

**Accounting:**

- The official 50 Tawi withholding tax certificate can now be generated and downloaded in PDF format.
- The PND 3 and PND 53 CSV export files have been reworked to ensure full compliance with the RD Prep application requirements.
- Tax grids have been updated to have more intuitive and user-friendly names.
- The Withholding Tax Summary Report has been added to provide a detailed breakdown of all taxes withheld, simplifying ledger reconciliation before final government submission.

## Türkiye 🇹🇷

**Accounting:**

- The user experience has been improved with enhanced Nilvera setup and validation, automatic invoice setup configuration, official e-invoice PDF printing, and streamlined e-invoice and e-dispatch workflows.
- Support has been added for commercial invoices, including acceptance and rejection workflows, and canceled invoice PDF retrieval.
- Partner identifiers, such as MERSIS numbers, are no longer managed using tags, but instead via the multi-ID feature on a partner's contact form.
- The e-Dispatch API integration has been expanded to receive incoming e-Dispatch receipts from Nilvera and link them to receipts in Odoo.
- For public sector e-invoices, the tax IDs of both the public institution and the public spending unit can be added to an invoice.
- The tax office model and its related partner field have been moved to the `l10n_tr module`​ to make fiscal identity data accessible across all business processes without requiring an e-invoicing dependency.

**Payroll:**

- The Wage-Related Withholding and Premium Service Declaration (1003B) has been added to report employee payroll tax and social security contribution information.

## United Arab Emirates 🇦🇪

**Payroll:**

- A calendar-day working schedule has been added to support payroll and leave calculations based on calendar days.
- Compute the total end-of-service benefit liability for one or more employees at any point in time using the End-of-Service Benefit report.

## United States 🇺🇸

**Accounting:** UX improvements to the Avalara Included service.
**Time Off:**The default US leave types have been expanded and improved to better align with standard workplace policies.

## Uruguay 🇺🇾

**Accounting:** A DGI lookup action has been added for Uruguay partners, allowing users to fetch and update official taxpayer data from Uruware directly from the identification number.

## Uzbekistan 🇺🇿

**Accounting:** The Uzbekistani Som (UZS) currency symbol has been updated to "so'm," which is used by the Central Bank of Uzbekistan.

## Vietnam 🇻🇳

**Accounting:**

- Export the 01/GTGT report and Appendix 142 in XML format for easy import into HTKK software or direct submission via the tax portal.
- Tax tags have been updated to offer more intuitive and user-friendly naming.
