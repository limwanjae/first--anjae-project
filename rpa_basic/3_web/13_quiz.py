# # 퀴즈  07:4:37~
# Quiz) selenium을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오

# 1. http://wwww.w3schools.com 접속 (URL은 구글에서 w3school검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#    First Name :나도
#    Last Name : 코딩
#    Contry : Canada
#    Subject : 퀴즈 완료 했습니다.
#    #위 값들은 변수로 미리 저장해 두세요
# 6. 5초 대기 후 Submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료


import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/')

# LEARN HTML 클릭
browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# 3. 상단 메뉴 중 HOW TO 클릭
time.sleep(2)
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
time.sleep(2)
#browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click()
#browser.find_element_by_link_text('Contact Form').click()# Contact Form이라는 2개이상 일때 에러가능
#browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()# a[117]를 a[text()="Contact Form"]로 수정해 본다
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact Form")]').click()# 일부 text만 같은거 찾을때는~~a[contains(text(), "Contact Form")] 작성


# 5. 입력란에 아래 값 입력
#    First Name :나도
#    Last Name : 코딩
#    Contry : Canada
#    Subject : 퀴즈 완료 했습니다.

First_Name = "나도"
Last_Name  = "코딩"
Country = "Canada"
Subject = "퀴즈 완료 했습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(First_Name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(Last_Name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(Country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(Subject)

#6. 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

# 7. 5초 대기 후 브라우저 종료
time.sleep(5)
browser.close()

browser.quit()


