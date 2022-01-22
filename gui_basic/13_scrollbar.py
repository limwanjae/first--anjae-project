from tkinter import *

root = Tk()
root.title("Nado GUI") # 프로그램 제목
root.geometry("640x480") # 크기지정 가로x세로

frame = Frame(root) # 하나의 프레임 안에서
frame.pack()

scrollbar = Scrollbar(frame)  # 스크롤바와 리스트박스를 매핑(1,2)해 줘야 됨
scrollbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set) #스크롤바와 리스트박스를 매핑1
for i in range(1,32):
    listbox.insert(END, str(i) + "일")# 1일, 2일,...
listbox.pack(side="left")   

scrollbar.config(command=listbox.yview) #스크롤바와 리스트박스를 매핑2

root.mainloop()