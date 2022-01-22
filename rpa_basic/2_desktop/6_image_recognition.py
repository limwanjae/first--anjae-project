# 이미지 처리 기본  2:50:30~
# 화면의 해상도,크기가 다르면 에러가 날수 있으니 조심~~
from PIL.ImageOps import grayscale
import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 화면에 같은 고양이 여러개 있을때는
# 구글에서 w3 schools checkbox 로 검색해서
# from pyautogui import locateAllOnScreen
# import pyautogui


# for i in locateAllOnScreen("checkbox.png"):# 동일한 이미지 모두 확인
#     print(i)
#     pyautogui.click(i, duration=0.25)# 클릭

# checkbox= pyautogui.locateOnScreen("checkbox.png")# 처음있는것 만 확인
# pyautogui.click(checkbox) # 클릭

# trash_icon1 = pyautogui.locateOnScreen("trash_icon1.png")
# pyautogui.moveTo(trash_icon1)

# 속도 개선
# 1.  GrayScale
# trash_icon1 = pyautogui.locateOnScreen("trash_icon1.png", grayscale=True)
# pyautogui.moveTo(trash_icon1)

# 2.범위 지정
# trash_icon1 = pyautogui.locateOnScreen("trash_icon1.png", region=(1540, 476, 400, 200))
# pyautogui.moveTo(trash_icon1)

# pyautogui.mouseInfo() # <-- 마우스 위치 알려주는 프로그램
#1540,476
#1840, 605

# 3. 정확도 조정 : pip install opencv-python 실행
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90% , confudence 기본값은 0.999임
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
#1. 계속 기다리기
#file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None: # 대상이 보이지 않으면 계속 기다린다(발견 실패 를 프린트)
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad) # 대상이 나타나면 실행

#2. 일정 시간 기다리기 ( TimeOut)
import time
import sys

timeout = 10 # 10초 대기
# start = time.time()# 시작시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None: # 대상이 보이지 않으면 계속 기다린다(발견 실패 를 프린트)
#     print("발견 실패")
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()# 종료시간 설정
#     if end - start > timeout: #지정한 10 초 보다 크면 프로그램종료(sys)
#         print("시간 종료")
#         sys.exit()#프로그램종료(sys)
# pyautogui.click(file_menu_notepad) # 대상이 나타나면 실행

##############
def find_target(img_file, timeout=10):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout =10):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate Program.")
        sys.exit()

my_click("file_menu_notepad.png", 5)
# 3:23 30~~

