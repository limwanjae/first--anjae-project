import pyautogui
# 마우스로 파일을 클릭하기위해 위치 알아내기
#pyautogui.sleep(3)# 3초 대기
# print(pyautogui.position())

# pyautogui.click(92, 15, duration=1)# 1초 동안 (92, 15) 좌표로 이동 후 마우스로 클릭
#pyautogui.click()
#pyautogui.mouseUp() # 드래그 할때 활용
#pyautogui.mouseDown()# 드래그 할때 활용

#pyautogui.doubleClick()
#pyautogui.click(clicks=500)

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()# 마우스 버튼 누른 상태
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()# 마우스 버튼 뗀 상태

pyautogui.sleep(3)# 3초 대기
#pyautogui.rightClick()
#pyautogui.middleClick()

# print(pyautogui.position())

# pyautogui.moveTo(1116, 408)
# #pyautogui.drag(100, 0)# 현재 위치 기준으로 x 100만큼, y 0만큼 드래그
# #pyautogui.drag(100, 0, duration= 0.25)# 너무 빠른 동작으로 drag 수행이 안될때는 duration값을 설정
# pyautogui.dragTo(1416, 408, duration= 0.25)# dragTo 는 절대 좌표 기준으로 동작

# 스크롤
pyautogui.scroll(-300) # 300 양수이면 위방향으로, 음수이면 아래 방향으로~

# 2:40:24~~