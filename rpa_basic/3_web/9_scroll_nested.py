# 6:42:24~~ 특정영역 스크롤
# 구글에서  w3school html 로 검색해서

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/default.asp')
browser.maximize_window()

time.sleep(5)

# 특정영역 스크롤 : html tag list의 xpath
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# # 방법1 ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# # 방법2: 좌표정보 이용

# xy = elem.location_once_scrolled_into_view# 함수가 아니니까 ()쓰지 마세요

# print("type: ", type(xy))# dict 형태
# print("value :", xy)

elem.click()

time.sleep(5)
browser.quit()

# 파일 다은로드  06:50:42~







