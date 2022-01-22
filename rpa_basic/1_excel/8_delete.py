from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#ws.delete_rows(8) # 8번째 줄에 있는 7번째 학생 데이터를 지운다
# ws.delete_rows(8, 3) # 8번째 줄 있는 7번째 학생 데이터부터 3개 데이터를 지운다
# wb.save("sample_delete_row.xlsx")

#ws.delete_cols(2) # 2번째 열 있는 영어 데이터를 지운다
ws.delete_cols(2, 2) # 2번째 열 부터 2개열의 데이터를 지운다
wb.save("sample_delete_cols.xlsx")