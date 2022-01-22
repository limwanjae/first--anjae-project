# 동적 페이지 스크롤 06:25:02~
# 네이버로 가고 쇼핑에서 ~
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.maximize_window()# 창 최대화

browser.get('https://shopping.naver.com/home/p/index.naver')


# # 무선 마우스 입력
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선마우스')

# # 검색 버튼 클릭
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()


elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')

time.sleep(1)
elem.send_keys(Keys.ENTER)# 검색버튼 클릭을 위한 엔터 처리

## 스크롤
# 지정한 위치로 스크롤 내리기:모니터(해상도) 놑이인 1080위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)')# 모니터 해상도에 따라서...( x=0, y=1080)
# time.sleep(1)
# browser.execute_script('window.scrollTo(0, 2080)')
# time.sleep(1)
# browser.execute_script('window.scrollTo(0, 3080)')

# 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

#  6:35:26~~~  동적 페이지 스크롤 2: 화면아 바뀌면 내리고~,안 바뀔때 까지 내리는~~
#동적페이지에 대해서 마지막까지 스크롤 반복 수행

interval =2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

#반복 수행
while True:
    #스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기(2초)
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height:# 직전 높이와 같으면=높이 변화가 없으면
        break# 반복문 탈출 (모든 스크롤 동작 완료)

    prev_height = curr_height


# 맨 위로 스크롤 올리기
browser.execute_script('window.scrollTo(0,0)')

time.sleep(5)
browser.quit()

# 6:42:24~~ 특정 영역 스크롤

