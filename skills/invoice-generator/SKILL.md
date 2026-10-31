---
name: invoice-generator
description: Generate a professional invoice as .xlsx (and optional PDF) from client, line items, tax and payment terms. Use when the user says invoice, tagihan, bill a client, or needs a numbered invoice with due date.
---
# Invoice generator

## When to use
User wants an invoice for a client. Works for freelancers and small studios. Output is a real spreadsheet with formulas, not a picture of one.

## Inputs to collect (ask only for what is missing)
- Your business name, address, email, bank details (name, bank, account no.)
- Client name + address/email
- Line items: description, qty, unit price
- Currency (default IDR if the user is in Indonesia, else USD)
- Tax: none / VAT-PPN 11% / withholding PPh 23 (2%) — withholding is *subtracted* from the amount received, not added
- Invoice number (default `INV-YYYYMM-NNN`), issue date (today), due date (default +14 days)

## Steps
1. Build the workbook with `openpyxl` (see `scripts/xlsx_helpers.py` → `make_invoice()` if present, otherwise write it inline):
   - Header block: business name bold 16pt, address, contact.
   - Meta block: Invoice no., Issue date, Due date, Client.
   - Items table starting row 12: Description | Qty | Unit price | Amount, with `=B{r}*C{r}` in Amount.
   - Subtotal `=SUM(D12:D{last})`, Tax row with formula, Total bold, "Amount due" with bank details beneath.
   - Number format `#,##0` for IDR, `#,##0.00` for others. Column widths 42/8/16/18.
2. Save as `Invoice-<number>-<client-slug>.xlsx`.
3. If the user asked for PDF, render the same layout with `reportlab` (A4, same fields).
4. Open the file once with openpyxl in read mode and print Subtotal/Total to confirm formulas are present.

## Output
The file path, plus a 4-line summary: invoice no., client, total, due date. Do not paste the whole table in chat.

## Example
> "Invoice PT Nusa for 2 days wedding coverage at 4.5jt/day plus 300 edited photos at 15k each, PPh 23 withheld, due in 30 days."
→ `Invoice-INV-202610-001-pt-nusa.xlsx`, Subtotal 13,500,000, PPh 23 −270,000, Amount received 13,230,000.

## Test prompt
"Make me an invoice for Acme Ltd: 10 hours consulting at $80, no tax, due 14 days." Expect an .xlsx with Total $800 computed by formula.
