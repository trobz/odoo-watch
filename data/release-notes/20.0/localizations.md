---
version: "20.0"
app: "Localizations"
app_slug: "localizations"
source_url: "https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_80"
item_count: 55
---

# Localizations — Odoo 20.0

## Argentina 🇦🇷

**Accounting:**

- The VAT Book PDF report has been adapted to remove extraneous headers and footers, facilitating compliance with the legal requirement to copy the report into official, pre-numbered ledger books.
- The payment amount is automatically computed when using checks and withholdings on vendor payments (available from 18.0).
- Automatically sync with ARCA to fetch the official daily currency rate.
- The "Payment on Informed CBU" legend option has been added to comply with ARCA RG 5762/2025.
- Export the SICORE report file for Earning/Profit taxes.
- When a "Pre-Printed Journal" is selected for printing, a warning message clarifies that headers and footers are intentionally omitted from the printed PDF; such documents are typically printed on corporate stationery.
- Management of third-party checks has been improved. Inter-branch transfers are now allowed, operations are ordered chronologically rather than by check ID, and payment validations and UI labels have been refined.
- Support has been added for withholding from payments in foreign currencies and standalone withholdings with no payment.
- Export the daily book (libro diario) in Excel format from the general ledger.

**Inventory:**

- Use batches to mass-process Remitos Digitales.
- The vendor's Remito (Delivery Guide) number can now be entered manually on receipts.

## Armenia 🇦🇲

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Australia 🇦🇺

**Accounting:** Bank synchronization now includes a new open banking integration through Basiq.

## Azerbaijan 🇦🇿

**Accounting:** The state names and codes have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Bahrain 🇧🇭

**Accounting:** State codes have been updated in compliance with the ISO 3166-2 standard.

## Bangladesh 🇧🇩

**Accounting:**

- The outdated tax report has been removed, and tax rates have been updated to comply with the 2026 Finance Act.
- Tax groups have been restructured by their nature rather than percentage, classifying them into three primary legal pillars: Value Added Tax, Tax Deducted at Source, and VAT Deducted at Source.
- The standard chart of accounts has been updated with parent groups to ensure automatic account roll-ups and enable section-wise trial balance reporting.

## Belgium 🇧🇪

**Payroll:**

- The Dimona flow is now supported (available from 19.0) and has been automated.
- The "Joint Committee" object and all associated data have been added.
- Joint committees can now be part of a parent joint committee.
- Add a maximum yearly remuneration to make an employee eligible for private car reimbursements.
- Automatically or manually add reorganization measures to working schedules based on content.
- The monthly salary structures have been merged into a single "Regular Pay" structure, with adapted rules for students and PFI.
- Remuneration for company directors is now supported.
- Temporarily dismiss warnings in the Payroll dashboard without discarding them permanently.
- New reporting has been added for meal voucher ordering.
- Configure the employee's contribution per meal voucher.
- Payslip computation for CP302 Flexi-Jobs (FLX) is now supported.
- The 7.67% holiday pay and the 28% employer contribution are automated.
- The annual earning caps (including 2026 updates) are monitored to trigger withholding taxes and ensure DMFA/Fiscal compliance.
- End-of-year bonus computation for CP302 is now supported.
- The Profit Sharing Bonus is now supported.

## Brazil 🇧🇷

**Accounting:**

- Generate NF-e for exportation of goods in BRL.
- Generate NFS-e for exportation of services in BRL.
- NFS-e (Services): Specify the place of service using the customer's delivery address (available from 19.0).
- NF-e (Goods): Include the delivery address automatically when it differs from the customer's main address (available from 19.0).
- Import NFS-e PDFs and digitize them with OCR technology.
- Batch download NF-e and NFS-e XML files from the list view.
- New fiscal fields have been added to the Operation Type for both the issuer and recipient to better handle complex, non-standard ICMS ST and tax credit scenarios in NF-e and goods tax calculation.
- A text link has been added to payment QR codes to allow customers to copy/paste them to their banking app.
- A breakdown of taxes applied to individual products is available in the sales order's and invoice's chatter so it can be easily shared with customers.
- CST and calculation base amounts have been added to sales order and invoice lines in the tax details section.
- "Customer Order Number" and "Customer Order Number ID" are now included on Avalara requests and sales orders.
- Avalara's CST classification for ICMS, PIS, COFINS, and IPI can now be manually overwritten, if needed.
- Alphanumeric CNPJs are now supported, in line with the 2026 tax reform (available from 17.0).
- The "cClassTrib" field has been added to the "Taxes Settings" tab of operation types, allowing users to override the default Avalara tax classification code when submitting electronic invoices.
- The "CBS Presumed Credit" and "IBS Presumed Credit" fields are only visible when the "Tax Regime" field is set to "Simplified". The deprecated "CBS/IBS Taxpayer" setting has been removed.
- Fiscal workflows have been streamlined with reorganized fiscal fields, improved fiscal code searching, and better error handling.

**Inventory:**

- The "Purpose of Use," "SPED Fiscal Product Type," "Source of Origin," and "IS Taxable" fields have been added to operation types to satisfy more use cases. The setup of these fiscal fields for customer transactions has been improved.
- NF-e information is shared when using Correios and creating shipping labels with Envia.

**Point of Sale:** Cancel NFC-e from PoS orders.

## Canada 🇨🇦

**Accounting:**

- Detailed expense accounts have been added and asset models have been reworked and localized to improve user onboarding.
- Process customer invoice payments in batches through CPA 005 Pre-Authorized Debit (PAD) files.

## Chile 🇨🇱

**Accounting:**

- Detailed expense accounts and asset models have been added.
- The XML reader is now available for sales journals. Customer invoices can be imported via XML, for example, during go-live processes.
- Chilean commune data has been added, reducing manual entry errors when configuring addresses in the Contacts and eCommerce flows.
- The DTE email server and XML reader now support non-billable amounts on invoices.
- Configure branches to share CAF files, assign them to specific branches, and redirect vendor bills using internal codes.
- The F29 tax report now uses Odoo's tax calculations account tags and follows Chilean standards for easier recording in the SII portal.

**Inventory:** Copies of the delivery guide for yielding purposes are now supported, complying with the SII layout requirements.

## China 🇨🇳

**Accounting:**

- The chart of accounts, balance sheet, and profit and loss statement have been improved (available from 19.0).
- Asset models have been added according to China Corporate Income Tax Regulations Article 60.
- Parent accounts have been updated for maintaining parent-child account hierarchy.
- The voucher template has been improved, and batch printing is now supported.
- The handling of value-added tax has been improved, and the VAT and Surcharges Return for General Taxpayers is now available.
- When applying VAT differential taxation, deductible amounts cannow be entered directly on invoice lines, and output VAT offset entries are automatically posted.

## Colombia 🇨🇴

**Accounting:**

- Detailed expense accounts and asset models have been added and localized to improve the onboarding experience.
- Electronic invoicing of free samples and promotional items is supported.
- The layout of fiscal PDF documents has been improved, and the QR code is visible on all pages.
- Electronic invoicing is now exclusively handled via the free DIAN connection; Carvajal is no longer supported.
- Type 3 Contingency invoicing is now supported, enabling fiscal document generation during extended DIAN service outages.
- Withholding certification reports no longer displays the DIAN compliance message to reduce confusion.
- The user interface has been improved for a smoother experience and better error handling. Demo data has also been updated.
- Duplicate detection for vendor bills is now based on detecting CUFE duplicates.
- An example of the most common self-withholding tax and tax group has been added to the Colombian localization module. The default configuration now complies with DIAN requirements.
- The XML reader now supports withholding taxes and applies them as required on vendor bills.
- Generate exogenous information reports 1001, 1003, 1005, 1006, 1007, 1008, and 1009.
- Mandate invoices can now be created for goods as well as services. In addition, multiple principals are now allowed and are assigned correctly to journal items.
- XML generation of invoices that include global discounts and loyalty features (i.e., negative lines) is now supported.
- Vendor bills can now be imported to purchase journals using the official ZIP file.

## Dominican Republic 🇩🇴

**Accounting:**

- Electronic invoicing is now supported (e-CF types 31–34), with XML generation and submission to DGII via Infile.
- Export the 606 purchase report as a TXT file.
- Tax grids and reporting rules have been updated for the IT-1 (ITBIS declaration) report.
- Use the national identification number (cédula de identidad) alongside the RNC (registro nacional de contribuyentes) number, which enables automatic electronic invoicing directly from the eCommerce flow.

## Ecuador 🇪🇨

**Accounting:**

- Add a custom legend to the header of PDF reports for electronic documents for cases such as exporters and NGOs.
- The chart of accounts has been improved by removing duplicate account names and types for a cleaner and more accurate financial structure.
- The display of the address and customer information on the invoice PDF has been improved.
- New withholding taxes are available that are based on the Resolución NRO. NAC-DGERCGC26-00000009 (available from 17.0).
- The electronic invoice provider's RUC is added to electronic documents and printed representations (RIDE) to comply with the SRI Resolution NAC-DGERCGC26-00000027 (available from 17.0).

**Point of Sale:** The Point of Sale app now blocks sales above the legal limit when using the default "Consumidor Final" customer, requiring selection of a real customer for compliant invoicing.

## Egypt 🇪🇬

**Accounting:**

- ETA synchronization is integrated into the "Send" wizard, with pre-check validation banners, and trackable submission history. A "Demo Mode" has been added to internally test the workflow without any credentials.
- Batch fetch ETA PDFs from the list view.
- The chart of accounts has been updated to implement a scalable 6-digit structure and group parent accounts. Default account mappings have been improved for deferred revenue/expenses, and expense accounts.
- Select a branch's activity type by its code and Arabic description to align with activity types on the Egyptian Tax Authority's (ETA) portal.
- Obsolete schedule taxes and other taxes have been removed and the related reports have been deleted.
- The VAT return and withholding reports have been updated to ensure ETA compliance.
- Withholding taxes can now be managed using the new "Deducted Withholding" and "Gross Withholding" (gross-up) flows to handle both standard deductions and net-of-tax agreements.
- The ETA Code field visibility has been restricted to only the "Sales" type taxes.
- Additional units of measure (square meter, milliliter, tonne, minute, millimeter, kilowatt-hour, square foot) are now mapped to their Egyptian Tax Authority (ETA) unit codes.
- Set a product's item code per company.
- Helwan and 6th of October states have been removed and existing records have been migrated to Cairo and Giza.
- "Building Number" is now visible on the Company and Contact forms.
- The "Street" and "Street 2" fields of partner addresses are concatenated into a single payload string to ensure address details are included during ETA synchronization.

**Payroll:**

- A calendar-day working schedule has been added to support payroll and leave calculations based on calendar days.
- Calculations for overtime have been improved.
- Payslips include end-of-year income tax adjustments.
- Export formats for Form 1, Form 2, and Form 6 are available for the National Organization for Social Insurance (NOSI) and Form 2 for the Egyptian Tax Authority (ETA).
- The management of attendance-based employees and salary rules has been improved to better align with labor laws and handle edge cases.

**Point of Sale:** Sales and refund receipts are submitted to the Egyptian Tax Authority (ETA) as e-receipts.

## France 🇫🇷

**Accounting:**

- Pre-configured annual report templates (plaquettes) compliant with official PCG standards have been added, featuring auto-populated financial sections, customizable layouts, and help textto simplify mandatory financial disclosures.
- The endpoints in the annuaire that match the SIREN entered in the FRCTC field are now detected automatically and are available for selection if multiple ones exist.

## Georgia 🇬🇪

**Accounting:**

- The base localization package has been added, including a localized chart of accounts, taxes, and VATreport (available from 19.0).
- State names and codes for Georgia have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Guatemala 🇬🇹

**Accounting:**

- Support has been added for Factura Especial (FESP), enabling automatic withholding of 100% VAT and ISR, generation of mandatory legal phrases, and FEL certification for purchases where the supplier does not invoice (available from 18.0).
- FEL documents can now be canceled directly via Infile. The cancellation reason is recorded and the document is marked as "Anulado" in SAT.
- The IDP fuel tax calculation for regular gasoline has been updated to account for the 10% alcohol content of E10 fuel.
- Official VAT Sales and Purchase reports (Libros de IVA) have been added in SAT-compliant formats.

**eCommerce:** Support has been added for electronic invoicing, including issuer phrases and allowing invoices to be issued to final consumers (CF).

**Point of Sale:** The Point of Sale app has been updated to comply with local electronic invoicing requirements, including mandatory validations and data needed for proper FEL/DTE issuance (available from 19.0).

## Hong Kong 🇭🇰

**Accounting:** The chart of accounts and the profit and loss and balance sheet reports have been updated to ensure full compliance with the HKFRS for Private Entities (PEs).

**Payroll:**

- Define an Internet fee and apply it to all employee payslips.
- Set an average daily wage (ADW) for employees.
- Calculate pre-transition and post-transition offset amounts for SP/LSP payments.
- Generate monthly MPF reports, create payroll groups/member classes, and define contribution periods for each employee.
- Define the month for end-of-year payments. Calculations are based on the number of previously generated payslips.
- Generate IR56B/E/F/G tax forms in XML and PDF format in compliance with the Inland Revenue Department (IRD) technical specifications.
- HSBC Autopay has been integrated directly into the standard reporting workflow. Select it as an export format and configure any Autopay account for any report.
- A new "Rentals" system has been introduced to manage the end-to-end rental process. Employees can submit rental requests and monthly proofs of payment directly via the Employees app, replacing manual forms and external spreadsheets. The system supports various Hong-Kong specific scenarios, including direct employer payments and employee-led contributions, while centralizing all compliance documentation for HR review.
- Define a minimum duration of consecutive leave (e.g., 4 days for paid sick leave) to automate eligibility for the 80% ADW leave types and prevent invalid requests.
- Daily, weekly, bi-weekly, and semi-monthly pay schedules have been added. Salary rules for MPF and fixed allowances automatically scale to the selected period, ensuring compliance with Hong Kong statutory thresholds for non-monthly earners.
- A new salary structure is available for casual employees in the catering and construction industries, supporting specific MPF Industry Scheme rates.
- The IR56M report is now available, as well as a new salary structure for non-employees such as contractors, freelancers, artists, etc.
- IR56 reports now support adding a different postal address to the employee's private address.
- A warning for the new "468 Rule" is shown when employees on non-continuous contracts approach or meet continuous contract thresholds.
- Customized salary rules are now automatically mapped with IRD reports (IR56B, IR56E, IR56F, IR56G, and IR56M) through the use of pre-defined categories.
- IR56 employer tax forms are now approved for submission to the Hong Kong Inland Revenue Department (IRD).
- XML exports of the IR56 form automatically group original and non-original submissions (A/R/S), in accordance with IRD requirements.
- Sick leave related to work injuries is now supported, in accordance with the Employees' Compensation Ordinance (Cap. 282).
- Support for the BOC banking report for FPS Non-Payment Type has been added.
- Different termination structures (Payment in Lieu of Notice, Severance Payment, and Long Service Payment) have been merged into salary rules within employee pay structures.

## Hungary 🇭🇺

**Accounting:**

- Generate an A60 statement, the Hungarian-specific EC sales list.
- Synchronize received vendor bills directly from the NAV API. Odoo automatically fetches and updates received invoices based on the info in NAV (available from 18.0).

## India 🇮🇳

**Accounting:**

- Issue credit notes for price adjustments.
- A new bill of entry flow for imported goods simplifies the recording of import customs duty and ensures the duty amount is included in inventory costing through landed costs.
- Apply TDS more flexibly with support for TDS & Payment, TDS Only, or Payment Only, giving you more control over tax deduction and payment processing.
- GST compliance has been extended to Composition Taxpayers, with dedicated support for the Composition Scheme and its statutory returns, CMP-08 and GSTR-4.
- Prepare financial statements with the prescribed presentation, classification, and disclosures as required under Schedule III, Division I of the Companies Act.

**Payroll:**

- Employees can now generate and print their TDS declarations from their employee profile.
- A new Gratuity Calculation Report provides a clear and accurate view of employees’ gratuity eligibility and, if relevant, the payable amount based on the applicable statutory regulations.
- Flexible sandwich leave options allow "Weekends and Company holidays," Weekends Only," or "Company holidays Only" to be included when calculating leaves taken across non-working days.
- A new EPF Summary report provides a comprehensive overview of employees' EPF contributions and balances for each employee.
- In the "End of collaboration" wizard, a new "Notice Period" tab has been added. In addition, when the dismissal date and actual departure date are the same, the Full and Final Settlement (FNF) payslip can be generated directly.
- TDS challans can now be generated monthly to record and deposit TDS deducted from employees’ salaries. Form 138 can be generated quarterly to report the TDS deducted and deposited with the Income Tax Department.
- A salary configurator is now available, allowing applicants to select benefits while signing the offer.
- Generate an HDFC eNET file from individual payslips or a pay run and upload the file to the HDFC bank portal to streamline the payroll process and speed up salary payment.

## Indonesia 🇮🇩

**Accounting:**

- The chart of accounts and asset list have been updated to include detailed expense accounts and localized asset models.
- Multiple improvements have been made to the contact form, including removing the "Is PKP" field and merging the "NIK" and "NPWP" fields.
- A new tax and tax group have been added for compliance with the PPN Dipungut mechanism.

**Payroll:**

- Default accounts are now set for standard payroll rules.
- Overtime calculation (PP No. 35/2021) - overtime components are now excluded from the basic salary calculation and are instead processed under a separate rule.

**Point of Sale:** QRIS is now available as the kiosk QR payment option.

## Iraq 🇮🇶

**Payroll:** The base payroll localization has been added, including monthly pay salary structure, social insurance, leaves setup, end-of-service benefit calculation, and overtime rates calculations.

## Italy 🇮🇹

**Accounting:** Add notes (causale) and attachments (allegati) directly to electronic invoices.

## Japan 🇯🇵

**Accounting:**

- The balance sheet and profit and loss statement are now compliant with Chusho Kaikei Yoryou.
- The chart of accounts has been updated to cover major business cases and to comply with Chusho Kaikei Yoryou and the e-Tax coding system.
- A consumption tax section has been added to the tax return for general and simple taxpayers, covering variants such as accumulation, deduction, and itemized methods.

## Jordan 🇯🇴

**Accounting:**

- Error handling for sending invoices to JoFotara has been improved, now including validations for the supplier's country and TIN.
- The JoFotara credit note synchronization has been improved by refining the line-matching logic (available from 17.0).
- Support has been added for "Transit," "Foreign Trade," and "Free Zone Transfer" invoice types (available from 17.0).
- The UX of the JoFotara EDI has been improved: Related fields are grouped under the "Other Info" tab on the invoice, and errors are now directly handled in the "Send" wizard.
- Multiple JoFotara submission scenarios are supported for invoices and POS receipts.

**Point of Sale:**

- The JoFotara refund synchronization has been improved by refining the line-matching logic (available from 17.0).
- Generate JoFotara-compliant receipts (available from 18.0).

## Kazakhstan 🇰🇿

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Korea 🇰🇷

**Accounting:**

- The Korean VAT reports for General and Simplified Taxpayers have been improved.
- The new "Issuance Type" field on invoices routes tax data directly to specific report lines, replacing the need for multiple redundant tax configurations.

## Kuwait 🇰🇼

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard.

**Payroll:** The base localization package has been added, including regular pay, social insurance calculations, end-of-service and provision calculations, and leaves setup.

## Kyrgyzstan 🇰🇬

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Lebanon 🇱🇧

**Accounting:** State codes have been updated in compliance with the ISO 3166-2 standard and duplicate state entries have been removed.

## Lithuania 🇱🇹

**Payroll:** Existing fields and other inputs have been converted to the new salary input flow.

## Luxembourg 🇱🇺

**Payroll:** The Decsal and Decmal reports are supported.

## Malaysia 🇲🇾

**Accounting:**

- Consolidated invoices can now be issued within the invoicing and accounting workflow.
- MyInvois is now supported across branches, with improved handling for sole proprietorships.

**Point of Sale:** Self-service e-invoicing via MyInvois is now possible.

## Mexico 🇲🇽

**Accounting:**

- On Global Invoices, bimonthly periodicity is now available, and the month is now selectable, making invoicing past months' orders easier.
- A cancellation acknowledgment can now be generated for canceled CFDIs.
- Invoices with the external trade complement can now include services as well (available from 19.0).
- Minimum wage, tax rates, and UMA have been updated.
- Factoring payments have been added in the bank reconciliation view.
- A new localized balance sheet report has been added based on the NIF B-6.
- A new localized profit and loss report has been added based on the NIF B-3.
- Complementary trial balance XML reports can now be generated.
- Upload a FIEL to automatically download missing vendor bills via the SAT integration.
- The XML reader now identifies the goods purchased, suggests the account, offers smarter product matching, and validates the amounts in Odoo against the XML to detect discrepancies.

**Inventory:** The driver for a bill of lading can now be selected directly in the delivery order, allowing for easier driver switching.

**Payroll:** When a new payslip is generated, the email sent to the employee now also includes a link to the Comprobante Fiscal Digital por Internet (CFDI) in XML format (available from 19.0).

## Oman 🇴🇲

**Accounting:** State codes have been updated in compliance with the ISO 3166-2 standard.

**Payroll:**

- The base localization package has been added, including regular pay, social insurance, end-of-service and provision calculations, leaves setup, overtime rules, and employer net cost calculations.
- Support for generating Wage Protection System (WPS) files has been added to facilitate salary payments and reporting in compliance with Omani legal requirements.

## Pakistan 🇵🇰

**Accounting:**

- Expense account descriptions have been added.
- State names and codes have been updated in compliance with the ISO 3166-2 standard.
- The chart of accounts has been updated with parent groups to ensure automatic account roll-ups, enable section-by-section trial balance reporting, and simplify compliance with the Companies Act 2017.
- The chart of accounts has been updated and outdated VAT and withholding reports have been removed to prepare for upcoming FBR Form-7 compliant reporting.
- The balance sheet and profit and loss statement are now generated dynamically using chart of accounts prefixes, rather than using legacy prefix mapping.
- Tax configurations have been streamlined by consolidating obsolete taxes into statutory sales tax, further tax, and withholding tax pillars to align with the Sales Tax Act.
- The Pakistani Rupee (PKR) currency symbol is displayed before the amount to align with standard market practices (available from 19.0).
- Accounting demo data has been updated.
- Maximum retail price tax calculations are supported.
- The 18% Third Schedule tax formula has been updated to handle tax-inclusive calculations.
- The "NTN" field on the contact form has been renamed to "Business Identification Number," which accepts both NTN and CNIC to classify a contact as a business.
- A new "Consumer Identification" field has been added to classify a contact as an individual customer, ensuring a clear distinction between the two.
- An integration with the Federal Board of Revenue (FBR) e-invoicing system has been added for registered businesses to ensure compliance with S.R.O. 1852(I)/2025.

**Payroll:** Payslips include end-of-year income tax adjustments.

**Point of Sale:** An integration with the Federal Board of Revenue's (FBR) computerized system is now available to ensure real-time reporting of point-of-sale orders, which is mandatory for all Tier-1 retailers in Pakistan.

## Peru 🇵🇪

**Accounting:**

- Support has been added for 19 sub-books of the Peruvian Inventory and Balances Electronic Book, including Trial Balance, Cash Flow, and specialized account reporting for SUNAT compliance (available from 18.0).
- A GRE can now be generated natively for internal transfers, with the operation type field visible and set to "11 - Transfer Between Warehouses" by default.
- Electronic vendor withholding documents can now be created with their corresponding XML, CDR, and PDF files.
- Support has been added for the Fixed Amount ISC (System Type 02) for electronic invoices.

**Point of Sale:** SUNAT-compliant thermal printing has been added for Peruvian POS electronic invoices and receipts, generating legal electronic document representations (Factura/Boleta/Notas de Crédito) directly on 58/80 mm printers (available from 19.0).

## Philippines 🇵🇭

**Accounting:**

- The format of the partner ledger report now complies with the Bureau of Internal Revenue (BIR) requirements. The Book of Accounts has been added for CBA and CAS compliance in the Philippines.
- Generate and download official PDF certificates for specific partners and date ranges using newly added report variants for BIR 2306 (Final Withholding Tax) and BIR 2307 (Expanded Withholding Tax).
- Differentiate between individuals and companies with the "Entity type" field. An information banner appears on Philippine reports that include a contact without a set entity type.
- Generate BIR 2306 and BIR 2307 withholding tax certificates on vendor bills.
- A new disbursement voucher has been added for internal company use.
- The BIR1600VT report has been implemented for final withholding VAT transactions.
- Send BIR 2306 and BIR 2307 withholding certificates directly to the vendor, if requested, when a vendor bill is paid.
- Invoices are now BIR- and CAS-compliant.
- Statutory discounts for senior citizens and people with disabilities are now supported on invoices and credit notes.
- The 2551Q report is now available for non-VAT registered companies.
- Names are now auto-separated into "First Name," "Middle Name," and "Last Name" to ensure the correct format for BIR reports.

**Payroll:**

- The basic Philippines payroll package is available with mandatory calculations for basic pay, benefits, taxes, overtime, etc.
- Support has been added for Form 1601-C items for BIR monthly payroll reporting.
- The yearly BIR Form 2316 tax report has been added.
- Support has been added for auto loan deduction rules for SSS Salary loans, SSS Calamity loans, Pag-IBIG Multi-Purpose loans, Pag-IBIG Calamity loans, and Pag-IBIG Housing loans.
- Annual tax annualization reporting has been added with auto-generated BIR Form 1604-C summary worksheets and validated Alphalist DAT file exports compliant with BIR eSubmission standards.

## Qatar 🇶🇦

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard.

## Romania 🇷🇴

**Accounting:**

- Support has been added for CPV codes on products in eFactura (available from 17.0).
- The VAT rates and the VAT report have been updated (available from 17.0).
- When downloading an invoice from ANAF, if the XML doesn't include a PDF, Odoo will download the official ANAF-generated PDF and use it as the attachment (available from 18.0).
- Select a period when manually synchronizing invoices with ANAF.
- Generate the SAF-T with Stock variant from the general ledger report (available from 18.0).
- Generate the D300 VAT report in XML format for submission to the tax authorities (available from 19.0).
- If an invoice is rejected by the SPV, it can now be reset to draft, corrected, and sent again (available from 18.0).

## Saudi Arabia 🇸🇦

**Accounting:**

- Expense accounts have been reworked, and asset models have been added to improve the onboarding experience.
- The invoice date now serves as the official ZATCA issuing date, replacing the confirmation date (available from 17.0).
- The Additional Identification Number field is now available for non-Saudi contacts, in compliance with the BR-KSA-81 ZATCA rule (available from 18.0).
- Identification Scheme and Identification Number are now also used to distinguish between a company (TIN, CRN, MOM, MLS, 700, SAG, OTH) and an individual contact (NAT, GCC, IQA, PAS).
- The "Is Retention" checkbox has been removed, and a negative sales tax is now automatically classified as a retention tax.
- States have been adapted to reflect the 13 subdivisions.
- Demo data has been improved.
- ZATCA synchronization has been integrated into the "Send" wizard, with pre-check validations shown in a banner; synchronization history is recorded in a new ZATCA tab upon sending. Batch processing through the list view is now supported.
- Invoice reports have been updated to include a line-level "Discount Amount" column, and the "Amount Due" label has been changed to "Invoice Total Payable Amount."
- Add multiple partner identifiers, including Saudi-specific identifiers like the Saudi national ID number, Iqama number, or GCC ID number, using the multi-ID feature on a partner's contact form.
- Define invoice types ("Tax" or "Simplified") and transaction types ("Export," "Summary," or "Nominal") directly on the invoice form to explicitly control API routing (B2B versus B2C).
- A new "Supply End Date" field has been added under the "Other Info" tab to generate simplified nominal invoices and to record continuous supplies and multiple deliveries.
- Configure tax exemption reasons using standard UBL tax category fields to simplify and declutter tax setup. Support has been added for free-text exemption reasons when recording services outside the scope of tax (VATEX-SA-OOS).
- ZATCA address compliance has been improved by restricting the "Building Number" and newly renamed "Secondary Number" (formerly "Plot Identification") fields to exactly four numerical digits, preventing XML validation errors (BR-KSA-37) during submission.
- The duplicate "Supply Date" field has been removed from the invoice form header to avoid confusion, keeping it accessible only within the "Other Info" tab.
- The standard chart of accounts has been updated to include a scalable 6-digit structure and to group parent accounts based on reverse liquidity sequencing.
- The default account mappings have been improved for deferred revenue, deferred expenses, and expense accounts.
- Invoices being sent to ZATCA after a timeout or a ZATCA server outage are no longer blocked.
- The "Rounding Method" setting is now fixed to document-level rounding to improve ZATCA compliance.
- Support for e-invoicing in ecommerce transactions has been added (available from 19.0).

**Payroll:**

- Track employees’ disciplinary actions linked to payslip deductions.
- Identify late attendance and apply salary deductions accordingly.
- Integrate with the GOSI platform to retrieve contribution portions.
- The end-of-service computation has been improved to better align with the QIWA and Ministry of Labor regulations.
- Issue advance salary payments when an employee takes annual leave.
- Automatically generate the GOSI Wages Update Sheet to easily update the contribution base on the GOSI portal whenever employee salaries change.
- Compute the total end-of-service benefit liability for one or more employees at any point in time using the End-of-Service Benefit report.
- A calendar-day working schedule has been added to support payroll and leave calculations based on calendar days.
- Automate sick leave deduction calculations based on the employee's year-to-date consumed balance to ensure alignment with labor laws.
- The calculation for end-of-service provisions has been updated to better support termination cases under Article 77 of the labor law.
- A "Month (30 days)" scheduled pay option has been added to calculate wages and unpaid leave deductions strictly on a 30-day basis, managing varying calendar months in compliance with labor laws.

**Point of Sale:**

- Support for down payments has been enhanced.
- The ZATCA PDF is no longer generated during order validation, avoiding unnecessary waiting time. It can be generated on demand when the invoice is first viewed or downloaded (available from 18.0).

## Singapore 🇸🇬

**Accounting:**

- GST taxes have been refined to align with current governmental requirements and to prepare for future GST InvoiceNow document compliance (available from 19.0).
- Tax invoice, credit note, and customer accounting PDF reports have been added to comply with the Inland Revenue Authority of Singapore (IRAS) GST requirements.
- The chart of accounts, balance sheet, and profit and loss statement have been improved to comply with Singapore Financial Reporting Standards (SFRS).

## Sri Lanka 🇱🇰

**Accounting:**

- A new localization package is available for Sri Lanka, including the chart of accounts, taxes, balance sheet, profit and loss reports, VAT 001 report, and WHT 001 report.
- The format of the VAT report has been improved to display data more clearly.
- The sequence format and layout of tax invoices now comply with the requirements outlined in Gazette No. 2481/22 (available from 19.0).

## Taiwan 🇹🇼

**Accounting:**

- The chart of accounts, balance sheet, and profit and loss statement have been updated (available from 19.0).
- Taxes and tax reports 401, 403, and 404 have been updated.
- ECPay e-invoicing details can now be specified directly on quotations and sales orders for B2C transactions, allowing information to be collected earlier in the sales flow.

**eCommerce:** ECPay integration is now supported to issue and submit Taiwanese e-invoices for eCommerce transactions (available from 18.0).

**Point of Sale:** Issue e-invoices for Point of Sale, and submit them to the official government portal via integration with ECPay (available from 19.0).

## Tajikistan 🇹🇯

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## Thailand 🇹🇭

**Accounting:**

- The chart of accounts has been updated to comply with TFRS for NPAEs, introducing detailed expense accounts, asset models, and VAT accounts. Relevant default accounts, taxes, and tax groups have been updated accordingly (available from 19.0).
- The P.P.30 VAT return report can now be exported as a CSV file compatible with the Thai Revenue Department's RD Prep software for monthly filing.
- The Company ID label has been updated and repositioned to clarify its use as a branch code, alongside new input validation.
- Taxes, tax groups, and fiscal positions have been expanded, adding new withholding types and enabling cash basis by default for services. Related descriptions have also been translated.
- The official 50 Tawi withholding tax certificate can now be generated and downloaded in PDF format.
- The PND 3 and PND 53 CSV export files have been reworked to ensure full compliance with the RD Prep application requirements.
- Tax grids have been updated to have more intuitive and user-friendly names.
- The Withholding Tax Summary Report has been added to provide a detailed breakdown of all taxes withheld, simplifying ledger reconciliation before final government submission.
- Tax invoices can now be generated independently from commercial invoices, with their own numbering sequence. Combined receipt/tax invoices are also fully supported.
- Debit and credit note PDF reports have been updated to fully comply with Thai regulations.

## Türkiye 🇹🇷

**Accounting:**

- Additional Invoice Scenarios (Basic, Export and Public), Invoice Types (Sales, Withholding, Tax Exempt, and Registered for Export), and Tax Offices have been added (available from 18.0).
- Return and withholding return invoice types are supported through credit notes.
- Support has been added for commercial invoice scenarios and sending export invoices as draft including PDF previews, approval, acceptance, rejection, and cancellation.
- Reason code 702 on Registered for Export invoices is now supported, including Customer and Seller Line Codes per invoice line.
- The street fields have been combined into a single address line when generating the XMLs (available from 19.0).
- The Nilvera e-invoice experience has been improved with clearer field guidance and validation, automatic contact matching and PDF retrieval, streamlined setup, and invoice status synchronization.
- E-invoices with an Error status can be canceled (available from 19.0).
- CTSP validation has been restricted to invoices marked as "GİB Product Export Invoice" and the field label has been updated for clearer guidance.
- Commonly used Stamp Tax rates (0.948%, 0.189%, 0.759%) have been added and included in the Tax Report.
- State codes have been updated to comply with the ISO 3166-2 standard.
- Exemption reason 351 has been added by default for sales invoices with 0% VAT.
- 35 new accounts have been added and account types 27 and 28 have been updated to "Fixed Assets".
- Parent accounts have been introduced and linked to corresponding sub-accounts in accordance with GIB’s 7/A chart of accounts.
- Partner identifiers, such as MERSIS numbers, are no longer managed using tags, but instead via the multi-ID feature on a partner's contact form.
- For public sector e-invoices, the tax IDs of both the public institution and the public spending unit can be added to an invoice.
- Tax office information has been added to the "Türkiye - Accounting" module for ease of use across business processes.
- Support has been added for multiple invoice sequences per journal based on invoice characteristics.
- The General Ledger CSV export has been fixed to maintain a continuous sequence of journal entries throughout the fiscal period (available from 17.0).
- Reconciliation letters have been added with a localized customer statement layout.
- Credit notes created from customer invoices use the journal's "Default Return from Sales Account" (available from 18.0).
- The accuracy of automatic exchange rate updates has been improved by using selling rates for currency conversions (available from 17.0).
- Synchronization with Nilvera has been improved to ensure all eligible invoices and bills are retrieved regardless of date or record limits (available from 19.0).
- Subscription e-invoice handling has been improved for mixed invoices by deriving document dates from subscription lines.
- Support has been added for fetching buying and selling rates and the option to choose rates per transaction.
- Rounding issues affecting foreign currency amounts in words on e-invoices have been fixed (available from 17.0).
- The Nilvera e-Invoicing integration is now only available with Odoo Enterprise.
- Support has beed added for issuing e-invoices to customers through government-approved dummy Tax IDs and to e-invoice customers for export invoices.
- Support has beed added for cancelling e-Archive invoices directly from Odoo.
- Support has beed added for website sales channel on e-Archive invoices.
- Automatically derive the 3-character e-Dispatch prefix from the delivery order sequence.
- The withholding tax configuration has been simplified by moving the withholding reason selection to the invoice level and reducing the number of predefined taxes.

**Inventory:**

- The Nilvera e-Dispatch integration has been expanded to send, receive, and fetch e-Dispatch documents and PDFs directly from Odoo.
- The Nilvera e-Dispatch integration has been expanded to send e-Dispatch responses directly from receipt records, allowing users to accept or reject dispatched goods.
- Upload incoming e-despatch XML files from the Nilvera portal to create draft inventory receipts (available from 18.0).
- Tax office information has been added to the e-Dispatch XML.
- The Nilvera e-Dispatch integration has been enhanced by enabling the mapping of one or multiple related dispatch documents to an invoice, ensuring dispatch orders are reflected in the XML.
- An "Invoice Serves as e-Dispatch" option has been added, allowing e-Archive invoices to serve as the dispatch document while tracking inventory operations.

**Payroll:**

- An advanced salary structure was introduced, supporting sick leaves, salary advances, and annual leave advance payments.
- Calculate severance pay in line with Türkiye's labor laws.
- The Wage-Related Withholding and Premium Service Declaration (1003B) has been added to report employee payroll tax and social security contribution information.
- Support has been added for R&D and design center incentives to automatically calculate stamp tax exemptions and education-based income tax reductions.
- Support has been added for self-insured (4b) employees, ensuring accurate salary calculations in compliance with labor laws.

## Turkmenistan 🇹🇲

**Accounting:** State names and codes have been added in compliance with the ISO 3166-2 standard (available from 19.0).

## United Arab Emirates 🇦🇪

**Accounting:**

- Expense accounts have been reworked, and asset models have been added to improve the onboarding experience.
- Generate the Federal Tax Authority (FTA) VAT audit file from the general ledger (available from 19.0).
- Expense account descriptions have been added.
- The chart of accounts has been redesigned to comply with IFRS and UAE Commercial Companies Law. It features a scalable 6-digit numbering system and reverse-liquidity sequencing, and includes statutory equity reserves, essential technical accounts (WIP, Goods in Transit), and parent account groups.

**Payroll:**

- The employee benefit contributions have been revised to better align with GPSSA & ADPF's regulations. Sick leaves are managed through a single salary rule and a single leave type.
- Treatment of DIFC Employee Workplace Savings (DEWS) contributions has been adapted to align with Dubai International Financial Centre (DIFC) regulations.
- A new "Emiratization Compliance" report has been introduced to track Emiratization percentages in line with MoHRE regulations.
- Non‑salary employer cost items (e.g., insurance, work permits, visa processing fees) are now supported, improving labour cost visibility.
- The WPS export has been enhanced to better align with MoHRE regulations (available from 19.0).
- Calculations for annual leave and end-of-service provisions have been improved (available from 19.0).
- Calculations for overtime have been improved.
- The plane tickets benefit calculation has been added to the salary rules.
- A calendar-day working schedule has been added to support payroll and leave calculations based on calendar days.
- Compute the total end-of-service benefit liability for one or more employees at any point in time using the End-of-Service Benefit report.

## United Kingdom 🇬🇧

**Accounting:**

- HMRC authentication is now saved per company rather than per user, enabling multiple team members to manage different client accounts simultaneously.
- It is now possible to submit VAT returns for multiple companies without constant re-authentication.

## United States of America 🇺🇸

**Accounting:**

- Each pre-configured asset model now has dedicated depreciation and expense accounts, replacing the previous use of shared generic accounts.
- A new integration method for AvaTax is available: "Avalara Included." This integration offers a more affordable option for small and medium-sized businesses, while maintaining full tax computation capabilities for the United States and Canada.
- Avalara tax parameters are now automatically added while calculating taxes to support state-specific tax calculation requirements.
- The US Sales Tax Report has been redesigned to include multi-jurisdiction breakdowns, state summary rollups, and enhanced support for exemptions and non-taxable goods.

**Payroll:**

- Local taxes for New York City and Yonkers were added to the US Payroll localization.
- Support has been added for qualified overtime deduction rules under the "One Big Beautiful Bill," including a new salary rule and parameters to display capped overtime deduction information on employee payslips (available from 19.0).
- Support for Georgia, Iowa, Kansas, Kentucky, Michigan, Mississippi, Missouri, New Jersey, South Carolina, Tennessee, and Utah has been added, including state, county, and city tax rules and payroll configurations.

**Time Off:**The default US leave types have been expanded and improved to better align with standard workplace policies.

## Uruguay 🇺🇾

**Accounting:**

- A DGI lookup action has been added for Uruguayan partners, allowing users to fetch and update official taxpayer data from Uruware directly from the identification number.
- Products and services can now be configured as non-billable, allowing them to be included onelectronic invoices.

**Point of Sale:**

Electronic invoicing is now supported, including electronic sales documents, refunds, and customer identification requirements.

## Uzbekistan 🇺🇿

**Accounting:**

- The base localization package has been added, including a localized chart of accounts, taxes (VAT 12%, Export 0%, Exempt 0%), and standard financial reports: balance sheet and profit and loss (available from 19.0).
- The Uzbekistani Som (UZS) currency symbol has been updated to "so'm," which is used by the Central Bank of Uzbekistan.
- The Russian language is now supported in reports and in the chart of accounts (available from 19.0).
- The VAT Registry Number is displayed on Uzbek invoices using the 14-digit PINFL instead of the TIN for B2C invoices (available from 19.0).

## Vietnam 🇻🇳

**Accounting:**

- The chart of accounts and balance sheet have been updated following Circular 99/2025/TT-BTC on corporate accounting guidelines (available from 18.0).
- The Tax Declaration Form 01/GTGT report has been added to ensure compliance with local tax regulations.
- Electronic Internal Transfer Notes can now be issued via SInvoice.
- Parent accounts can now be used to structure the chart of accounts, allowing child accounts to be grouped for reporting and visualization.
- Appendix 142 has been added to Tax Declaration Form 01/GTGT to ensure compliance with local tax regulations.
- Export the 01/GTGT report and Appendix 142 in XML format for easy import into HTKK software or direct submission via the tax portal.
- Tax tags have been updated to offer more intuitive and user-friendly naming.
- The General Journal - S03a-DN and General Ledger - S03b-DN reports with counterpart account information have been added to comply with Circular 99/2025/TT-BTC.

**Point of Sale:** E-invoices can now be issued via SInvoice for POS orders, ensuring compliance with local tax regulations (available from 18.0).
