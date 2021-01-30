from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# Text = text widget
# 여러줄 사용할 땐 Text

listbox = Listbox(root,selectmode='extended', height=0)
# listbox = Listbox(root,selectmode='single', height=0)
# listbox = Listbox(root,selectmode='extended', height=3) -> height에 해당하는 숫자 만큼만 List로 보임
# -> Scroll Bar에 대해선 후 강의에서 진행

listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # 삭제
    listbox.delete(END) # 맨 뒤 List 삭제
    listbox.delete(0) # 맨 처음 List 삭제

    # 개수 확인
    print(listbox.size())

    # 항목 확인, 시작 Index와 끝 Index 입력
    print(listbox.get(0,2)) # 0부터 2까지의 List 출력 (3개 항목 출력)

    # 선택된 항목 확인
    print(listbox.curselection())

btn = Button(root, text = 'click', command = btncmd)
btn.pack()

root.mainloop()
