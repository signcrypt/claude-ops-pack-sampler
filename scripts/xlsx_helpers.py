"""Small openpyxl helpers used by the xlsx-builder, invoice-generator and tracker skills.

Usage:
    from xlsx_helpers import header_row, add_list_validation, autosize, add_readme, count_formulas, make_invoice
"""
from __future__ import annotations
import datetime as dt
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

HEADER_FILL = PatternFill("solid", fgColor="1F2A44")
HEADER_FONT = Font(bold=True, color="FFFFFF")
THIN = Side(style="thin", color="D0D4DC")


def header_row(ws, headers, row=1, widths=None):
    """Write a styled header row and freeze panes beneath it."""
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.fill, c.font = HEADER_FILL, HEADER_FONT
        c.alignment = Alignment(vertical="center")
        if widths:
            ws.column_dimensions[get_column_letter(i)].width = widths[i - 1]
    ws.freeze_panes = ws.cell(row=row + 1, column=1)


def add_list_validation(ws, col_letter, options, first_row=2, last_row=500):
    """Dropdown on a column from a literal list of options."""
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}{first_row}:{col_letter}{last_row}")
    return dv


def autosize(ws, min_w=8, max_w=60):
    for col in ws.columns:
        letter = get_column_letter(col[0].column)
        longest = max((len(str(c.value)) for c in col if c.value is not None), default=0)
        ws.column_dimensions[letter].width = max(min_w, min(max_w, longest + 2))


def add_readme(wb, lines, title="README"):
    ws = wb.create_sheet(title, 0)
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=14)
    for i, line in enumerate(lines, start=3):
        ws.cell(row=i, column=1, value=line)
    ws.column_dimensions["A"].width = 100
    return ws


def count_formulas(path):
    wb = load_workbook(path)
    return sum(
        1 for ws in wb for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("=")
    )


def make_invoice(path, business, client, items, currency="USD", tax_mode="none",
                 number=None, issue=None, due_days=14, bank=""):
    """items: list of (description, qty, unit_price). tax_mode: none | ppn11 | pph23."""
    issue = issue or dt.date.today()
    number = number or f"INV-{issue:%Y%m}-001"
    wb = Workbook(); ws = wb.active; ws.title = "Invoice"
    ws["A1"] = business; ws["A1"].font = Font(bold=True, size=16)
    ws["A3"] = "Invoice no."; ws["B3"] = number
    ws["A4"] = "Issue date"; ws["B4"] = issue; ws["B4"].number_format = "yyyy-mm-dd"
    ws["A5"] = "Due date"; ws["B5"] = "=B4+" + str(due_days); ws["B5"].number_format = "yyyy-mm-dd"
    ws["A6"] = "Bill to"; ws["B6"] = client
    header_row(ws, ["Description", "Qty", "Unit price", "Amount"], row=11, widths=[42, 8, 16, 18])
    fmt = "#,##0" if currency == "IDR" else "#,##0.00"
    r = 12
    for desc, qty, price in items:
        ws.cell(r, 1, desc); ws.cell(r, 2, qty); ws.cell(r, 3, price).number_format = fmt
        ws.cell(r, 4, f"=B{r}*C{r}").number_format = fmt
        r += 1
    last = r - 1
    ws.cell(r + 1, 3, "Subtotal"); ws.cell(r + 1, 4, f"=SUM(D12:D{last})").number_format = fmt
    if tax_mode == "ppn11":
        ws.cell(r + 2, 3, "PPN 11%"); ws.cell(r + 2, 4, f"=D{r+1}*0.11").number_format = fmt
        ws.cell(r + 3, 3, "Total"); ws.cell(r + 3, 4, f"=D{r+1}+D{r+2}").number_format = fmt
    elif tax_mode == "pph23":
        ws.cell(r + 2, 3, "PPh 23 (2%) withheld"); ws.cell(r + 2, 4, f"=-D{r+1}*0.02").number_format = fmt
        ws.cell(r + 3, 3, "Amount received"); ws.cell(r + 3, 4, f"=D{r+1}+D{r+2}").number_format = fmt
    else:
        ws.cell(r + 3, 3, "Total"); ws.cell(r + 3, 4, f"=D{r+1}").number_format = fmt
    ws.cell(r + 3, 3).font = Font(bold=True); ws.cell(r + 3, 4).font = Font(bold=True)
    ws.cell(r + 5, 1, "Payment details"); ws.cell(r + 5, 1).font = Font(bold=True)
    ws.cell(r + 6, 1, bank)
    wb.save(path)
    return path, number


if __name__ == "__main__":
    p, n = make_invoice("/tmp/demo-invoice.xlsx", "Demo Studio", "Acme Ltd",
                        [("Consulting", 10, 80)], currency="USD")
    print(p, n, "formulas:", count_formulas(p))
