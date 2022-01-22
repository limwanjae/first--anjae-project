from tkinter import *


root = Tk()
root.title("Nado GUI") # 프로그램 제목
root.geometry("640x480") # 크기지정 가로x세로

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # photo2를 전역변수로 지정해서 한번실행후 없어지지 않도록 한다.
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()