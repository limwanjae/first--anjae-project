from tkinter import *

root = Tk()
root.title('Nado GUI') # 프로그램 제목
root.geometry("640x480") # 크기지정 가로x세로

txt = Text(root, width=30, height=5) # TXT는 여러줄을 입력할 수 있음
txt.pack()

txt.insert(END, "글자를 입력하세요") # txt창에 기본값을 미리 넣어 줄수 있음~~

e = Entry(root, width=30) # 엔트리는 TXT와 다르게 한 줄만 입력됨
e.pack()
e.insert(0,"한 줄만 입력해요")# 엔트리 창에 기본값을 미리 넣어 줄수 있음~~

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END)) # 텍스트에서 가져와라 ~~ 1은 첫번째줄, 0은 맨 왼쪽 컬럼, END는 끝까지
    print(e.get()) # 엔트리 값 가져오기

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()