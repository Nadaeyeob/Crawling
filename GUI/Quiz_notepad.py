from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import time
import os

root = Tk()

###### Title
root.title('제목없음 - Windows 메모장') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
# root.resizable(False,False)

filename = 'C:/Users/sw993/OneDrive/바탕 화면/Crawling/mynote.txt'
###### menu
menu = Menu(root)

menu_file = Menu(menu,tearoff = 0)
menu.add_cascade(label='파일', menu=menu_file)

def open_file():
    if os.path.isfile(filename):
        with open(filename,'r',encoding='utf8') as f:
            txt1.delete('1.0',END) # Text widget 본문 삭제
            txt1.insert(END,f.read())

menu_file.add_command(label = '열기', command = open_file)

def save_file():
    with open(filename,'w',encoding='utf8') as w:
        w.write(txt1.get('1.0',END))

menu_file.add_command(label = '저장', command = save_file)
menu_file.add_separator()
menu_file.add_command(label = '끝내기', command = root.quit)


menu_edit = Menu(menu,tearoff = 0)
menu.add_cascade(label='편집', menu=menu_edit)

menu_temp = Menu(menu,tearoff = 0)
menu.add_cascade(label='서식', menu=menu_temp)

menu_show = Menu(menu,tearoff = 0)
menu.add_cascade(label='보기', menu=menu_show)

menu_help = Menu(menu,tearoff = 0)
menu.add_cascade(label='도움말', menu=menu_help)

###### Scroll Bar
scrollbar = Scrollbar(root)
scrollbar.pack(side='right',fill='y')

###### 본문
txt1 = Text(root, yscrollcommand = scrollbar.set)
txt1.pack(fill='both',expand=True,side='left')
# txt1.insert('본문을 채워주세요')

###### Status Bar
# progress_var = DoubleVar() # 실수 값 표시 위함
# progressbar = ttk.Progressbar(root,maximum = 100, length= 150, variable=progress_var)
# progressbar.pack()



root.config(menu=menu)

root.mainloop()
