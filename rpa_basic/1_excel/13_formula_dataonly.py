from openpyxl import load_workbook
wb = load_workbook("sample_formula.xlsx",data_only=True)
ws = wb.active

# 수식 그대로 가져옴( 데이터를 가져오려면, WORKBOOK을 열때, data_only=True를 추가한다 )
for row in ws.values: # 워크시트의 값을 가져온다
    for cell in row:
        print(cell)

# 출력값이 아래처럼 보인다.
#2021-12-15 22:39:12.845000
# None  --> evaluate 되지 않은 상태의 데이터는 None이라고 표시됨--> 열린파일은 저장후 다시 실행하면 계산된 값 확인
# None
# 10
# 20
# None
# None
# 01:55:15