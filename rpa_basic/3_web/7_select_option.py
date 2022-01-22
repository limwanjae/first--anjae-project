# select& option 6:16:37 ~~
# 구글에서검색 :  w3school html option
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()# 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

time.sleep(5)


# #방법1 : 옵션 인덱스에서 찾아서 선택 하는것
# #cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
# # option[1] : 첫번째 항목
# # option[2] : 두번째 항목

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()

# #방법2 : 완전히 일치하는 텍스트 값을 통해서 선택 하는것
# # 옵션중에서 텍스트가 Audi인 항목을 선택

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

# elem.click()

#방법3 : 텍스트 값이 부분 일치하는 항목 선택 하는것
# option 부분을 contains로 바꾸고

elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')

elem.click()



time.sleep(5)

browser.quit()




