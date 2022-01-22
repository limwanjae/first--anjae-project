from tkinter import *

root = Tk()
root.title("Nado GUI") # 프로그램 제목
root.geometry("640x480") # 크기지정 가로x세로

listbox = Listbox(root, selectmode="extended", height=0) # 리스트 박스
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #pass

    # 삭제
    #listbox.delete(END) # 버튼 클릭했을 때 맨 뒤 항목을 삭제
    #listbox.delete(0) # 버튼 클릭했을 때 맨 앞 항목을 삭제

    # 갯수 확인
    #print("리스트에는", listbox.size(),'개가 있어요' )

    # 항목 확인
    #print("1번째부터 3번째까지의 항목:", listbox.get(0,2)) # get 뒤에 시작, 끝 idx를 주면 됨

    # 선택된 항목 확인 ( 위치로 반환, 예 1,2,3)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()