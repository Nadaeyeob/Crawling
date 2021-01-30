from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# Text = text widget
# 여러줄 사용할 땐 Text

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END,'글자를 입력하세요') # Text widget에 기본 값 입력

# 한줄로 입력 받을 때 사용
e = Entry(root, width=30)
e.insert(0,'한줄만 입력하세요') # 현재 아무 값도 없으므로 END와 동일
e.pack()

def btncmd():
    print(txt.get('1.0',END)) # 1.0 -> Line 1 : Col 0 부터 호출
    print(e.get())

    txt.delete('1.0',END)
    e.delete(0,END) # entry의 경우 한줄 밖에 안되므로 x.x 등으로 표시할 필요 없음

btn = Button(root, text = 'click', command = btncmd)
btn.pack()

root.mainloop()
