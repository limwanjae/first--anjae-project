import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI") # 프로그램 제목
root.geometry("640x480") # 크기지정 가로x세로

values = [str(i) + "일" for i in range(1,32)] # 1~31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결재일") # 최초 목록의 제목 설정



readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")# state= 정해주면 콤보박스에 글자 못 씀(읽기 전용)
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()



def btncmd(): # 버틍 클릭했을때~~
    print(combobox.get()) # 선택된 값 출력
    print(readonly_combobox.get())

  

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()