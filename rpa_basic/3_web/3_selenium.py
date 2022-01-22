# 셀레니움 기본 5:31:00~
#   웹 자동화
#   터미널에서 pip install selenium 설치
#   웹 드라이버 설치 : 우리는 크롬으로 할껴~~
#     익스프로어나 파이어 폭스로 하려면 그거 웹드라이버를 설치 해야함
#     크롬 버전이 맞나 확인해야함 : 주소창에서 chrome://version/ 입력함
#     버전 96.0.4664.110(공식 빌드) (64비트)
#     구글에서 chromedriver  검색해서 96.0 버전 맞는거 다운로드 한다.

from selenium import webdriver
# browser = webdriver.Chrome("./chromedriver.exe")# " "위치에 있는 크롬드라이버를 실행
browser = webdriver.Chrome()




# >>> elem = browser.find_element_by_link_text("카페")
# >>> elem
# >>> elem.click()
# >>> browser.back()
# >>> browser.forward()

# >>> browser.refresh()
# 5:41:59~~~


# browser.get("http://naver.com")

# >>> elem=browser.find_element_by_id("query")  
# >>> elem

# 글자입력
#>>> elem.send_keys("나도코딩")

# enter 치기

# >>> from selenium.webdriver.common.keys import Keys
# >>> elem.send_keys(Keys.ENTER)

browser.get("http://daum.net")

>>> elem=browser.find_element_by_name("q")
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="f82c5cc5b6fd23ee97bea47f7e601eee", element="5bca5b01-13f1-4391-a340-3955d390d7e6")>
>>> elem.send_keys("나도코딩")
>>> elem= browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
>>> elem.click()
# 스크린샷
>>> browser.save_screenshot('daem.png')


# 구글에서 seleniun with python 검색하면



>>> from selenium.webdriver.common.keys import Keys
>>> elem.send_keys(Keys.ENTER)

# 5:48:02~

