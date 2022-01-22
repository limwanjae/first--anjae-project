from tkinter import *

root = Tk()
root.title('Nado GUI') # 프로그램 제목

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10,  text="버튼222222222") #pad 는 여백으로 글자가 많아 지면 자동으로 버튼이 커짐
btn2.pack()

btn3 = Button(root, padx=10, pady=5,  text="버튼3")
btn3.pack()


btn4 = Button(root, width=10, height=3, text="버튼44444444444444") # width=10, height=3는 고정된 버튼의 크기 
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5" ) # fg는 글자색, bg는 버튼색 
btn5.pack() 

photo = PhotoImage(file="gui_basic/img.png") 
btn6 = Button(root, image=photo ) # 사진을 버튼에 넣기
btn6.pack() 

def btncmd():
    print("버튼이 클릭 되었어요.")

btn7 = Button(root,  text="동작하는 버튼", command=btncmd  ) #  
btn7.pack()

root.mainloop()