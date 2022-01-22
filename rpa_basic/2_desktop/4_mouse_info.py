import pyautogui
#pyautogui.mouseInfo() # 마우스 위치의 좌표 색깔 정보 알려주는 프로그램
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용


for i in range(10): # 반복작업이 실행중에 파이선을 종료하고 싶을때 네 귀퉁이 중 아무대나 갖다 놓으면 종료된다.
    pyautogui.move(100, 100) # 이런 동작을 fail safe 라고 함
   # pyautogui.sleep(1)# 어떤 경우라도 계속 작업을 하려면 pyautogui.FAILSAFE = False 하면 됨

# 2:45:53~