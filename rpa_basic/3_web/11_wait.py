# 페이지 로딩 대기1  6:57:39~~
import time
from selenium import webdriver

browser = webdriver.Chrome()
#browser.maximize_window()
browser.get('https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C&qdt=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C')

# 가는날 클릭
browser.find_element_by_xpath('//*[@id="_flight_section"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/p').click()

browser.find_elements_by_link_text('30')[0].click()

# 오는날 클릭
browser.find_elements_by_link_text('5')[1].click()


# 도착 : 제주 클릭
browser.find_element_by_xpath('//*[@id="_flight_section"]/div/div[2]/div[2]/div[1]/div[2]/div/h4/a/span[1]').click()


# 항공권 검색 클릭
time.sleep(1)
browser.find_element_by_link_text('항공권 검색').click()

time.sleep(5)
browser.quit()

# 07:06:32~~~
