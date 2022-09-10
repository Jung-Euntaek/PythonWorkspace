from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# # ws.insert_rows(8)
# ws.insert_rows(8, 5) # row 8 위치에 5개 row 삽입 
# wb.save("sample_insert_rows.xlsx")

ws.insert_cols(2) # B열에 column 삽입
wb.save("sample_insert_cols.xlsx") 