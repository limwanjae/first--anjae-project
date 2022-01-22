# 파일 다은로드  06:50:42~
# 구글에서 w3school download attribute 를 검색해서
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r' C:\Users\lim\Desktop\PythonWorkspace>'})

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# download 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a/img')
elem.click()

time.sleep(5)
browser.quit()


