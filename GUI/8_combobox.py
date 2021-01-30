from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# Combobox는 ttk import 필요

values=[ str(i) + '일' for i in range(1,32)]

combobox1 = ttk.Combobox(root,height=5, values=values)
combobox1.set('카드 결제일')
combobox1.pack()

# Readonly + 0번 째 값 설정
combobox2 = ttk.Combobox(root,height=5, values=values, state='readonly')
combobox2.current(0)
combobox2.pack()


def btncmd():
    print(combobox1.get()) # 선택된 값 출력

btn = Button(root, text = 'click', command = btncmd)
btn.pack()

root.mainloop()
