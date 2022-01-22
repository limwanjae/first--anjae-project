# # 퀴즈 4:51:43 ~
# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오.

# 1. 그림판을 실행( 단축키 : win + r,  입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역의 아무곳에나 글자 입력
#   - 입력글자  " 참 잘 했어요."

# 3.5초 대기 후 그림판 종료mspaint

# 이때, 저장하지 않음을 자동으로 선택하여 프로그램이  완전 종료 되도록 함.

import sys
import pyautogui

pyautogui.hotkey("win", "r")# 단축키 : win + r 입력효과
pyautogui.write("mspaint")# 프로그램 명 입력
pyautogui.press("enter")#엔터 키 누름

# 그림판 나타날때 까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]# 그림판 1개만 띄워쟈 있다고 가정
if window.isMaximized == False:
    window.maximize()# 최대화

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
#pyautogui.click(200, 200, duration=0.5)

btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 300, btn_brush.top + 500)

# 한글 입력하려면  pip install pyperclip 설치한다

import pyperclip
# pyperclip.copy("나도코딩")# "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")# 클립보드에 있는 애용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "V")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

#프로그램 종료
window.close()
pyautogui.sleep(1)
pyautogui.press("n")# 저장하지 않음

# HTML 5:07:28



