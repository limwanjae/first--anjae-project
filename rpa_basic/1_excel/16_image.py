# 이미지 가져오기 01:58:30
from openpyxl import Workbook
from openpyxl.drawing.image import Image 

wb = Workbook()
ws = wb.active

img = Image("img.png")

# c3 위치에 img.png 파일의 이미지를 삽입
ws.add_image(img, "c3")

wb.save("sample_img.xlsx")

# 2:01:24