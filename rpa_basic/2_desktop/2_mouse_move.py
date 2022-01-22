# 마우스 이동 : 2:20:53~
import pyautogui

# 절대 좌표로 마우스 이동
#pyautogui.moveTo(200, 100)# 지정한 위치(x, y)로 마우스를 이동
#pyautogui.moveTo(100, 200, duration=5)# 5초 동안 100, 200 위치로 이동

# pyautogui.moveTo(100, 100, duration=1)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 300, duration=1)

# 상대 좌표로 마우스 이동( 현재커서가 있는 커서로 부터)
# pyautogui.moveTo(100, 100, duration=1)
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100, 100, duration= 1)# 100, 100기준으로 +100, +100--> 200, 200
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100, 100, duration= 1)# 200, 200기준으로 --> 300, 300
# print(pyautogui.position()) # point(x, y)

# 마우스 위치(x, y) 프린트
p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y)# x, y

