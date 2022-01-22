
import time
import tkinter.ttk as ttk # 콤보박스, 프로그래스바
from tkinter import *

root = Tk()
root.title("Nado GUI") # 프로그램 제목
root.geometry("640x480") # 크기지정 가로x세로

# #Progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# Progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# Progressbar.start(10) # 10 : 10ms마다 움직임
# Progressbar.pack()

# def btncmd(): # 버튼 클릭했을때~~
#     Progressbar.stop()  # 작동중지 되면도 움직임 이 없어짐

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
Progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
Progressbar2.pack()

def btncmd2():
    
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) #프로그래스이 값 설정
        Progressbar2.update() # gui 업데이트하는거 시각화
        print(p_var2.get()) # 지금 어디쯤 가는지 보여줌

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()