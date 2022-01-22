
import time
from typing import ByteString
from selenium import webdriver




browser = webdriver.Chrome()
browser.maximize_window()# 창 최대화

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_class_name_text("가는날 선택").click()

# 이번달 27일,28일 선택
# browser.find_elements_by_link_text("27")[0].click() #[0] --> 이번달 달력에서 선택
# browser.find_elements_by_link_text("28")[0].click() #[0] --> 이번달 달력에서 선택

# 다음달 27일,28일 선택
# browser.find_elements_by_link_text("27")[1].click() #[1] --> 다음달 달력에서 선택
# browser.find_elements_by_link_text("28")[1].click() #[1] --> 다음달 달력에서 선택

# 이번달 27일,28일 선택
browser.find_elements_by_link_text("27")[0].click() #[0] --> 이번달 달력에서 선택
browser.find_elements_by_link_text("28")[1].click() #[1] --> 다음달 달력에서 선택


