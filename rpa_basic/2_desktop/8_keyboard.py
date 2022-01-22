#  키보드  3:33:58~
import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]# 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("nadocoding", interval=0.25)
# pyautogui.write("나도코딩")# pyautogui에서는 한글이 써지지 않는다- 뒷 부분에서 알려줌

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right","l", "a", "enter"], interval=0.25)
# t  e s t 순서대로 적고, 왼쪽 방향키2번, 오른쪽 방향키 1번, l a순서대로 적고 엔터.

#특수문자
#shift+4 --> $를 구현하기 위해서
# pyautogui.keyDown("shift")# shift키를 누른 상태에서
# pyautogui.press("4")# 숫자 4를 입력하고
# pyautogui.keyUp("shift")# shift키를 뗀다


# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")# press("a")
# pyautogui.keyUp("ctrl")# Ctrl + A --> 전체선택

# 간편한 조합키

# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl누르고, alt누르고, shift누르고, a누르고, > a떼고,shift떼고, alt떼고, ctrl떼고 순서
# pyautogui.hotkey("ctrl", "a")

# 한글 입력하려면  pip install pyperclip 설치한다

import pyperclip
# pyperclip.copy("나도코딩")# "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")# 클립보드에 있는 애용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "V")

my_write("나도코딩 두번째")

# 자동화 프로그램 종료
# WIN : ctrl + alt + del
# MAC : cmd + shift +option + q


