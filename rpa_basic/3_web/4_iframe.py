# <html>
#     <body>
#         <iframe id="1">
#             <html>
#                 <body>
#                     <dov.../>

#                 </body>
#             </html>

#         </iframe>
#             <html>
#                 <body>
#                     <dov.../>
#
#                 </body>

#         <iframe id="2">
#         </iframe>
    
#         <dov.../>
#     </body>
# </html>

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')# frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]')

elem.click()

# browser.switch_to.defaulit_content()# 상위로 빠져 나옴

time.sleep(5)# 5초 대기

browser.quit()

