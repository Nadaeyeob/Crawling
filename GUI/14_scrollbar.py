from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import time

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right',fill='y')

listbox = Listbox(frame,selectmode='extended',height=10, yscrollcommand= scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)


root.mainloop()
