from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#ws.insert_rows(8) # 8번째 줄을 삽입
#ws.insert_rows(8, 5) # 8번째에서 5개의 줄을 추가삽입
#wb.save("sample_insert_rows.xlsx")

#ws.insert_cols(2)# B번 열에 빈 열 삽입
ws.insert_cols(2, 3)# B번열부터 3개의 빈 열 삽입

wb.save("sample_insert_cols.xlsx")