from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8) # row 8 삭제
# ws.delete_rows(8, 3) # 8번째 줄부터 총 3줄 삭제
# wb.save("sample_delete_row.xlsx")

# ws.delete_cols(2, 2)
# wb.save("sampel_delete_col.xlsx")