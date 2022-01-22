
# 체크박스 : 여러개 선택할 수 있음 06:09:00~
# 구글에서검색 :  w3school checkbox

# import time
# from selenium import webdriver

# browser = webdriver.Chrome()

# browser.maximize_window()# 창 최대화

# browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

# browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')

# time.sleep(5)

# if elem.is_selected() == False:
#     print("선택 안되어 있으므로 선택")
#     elem.click()
# else:
#     print("선택되어 있어 아무것도 안함")

# time.sleep(5)


## 다른 문법 사용
# browser.find_element_by_name
# browser.find_element_by_xpath 형태에 대해


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()# 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')

#elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
#elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
elem = browser.find_element(By.ID, "vehicle1")

time.sleep(5)

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택")
    elem.click()
else:
    print("선택되어 있어 아무것도 안함")

time.sleep(5)

browser.quit()


