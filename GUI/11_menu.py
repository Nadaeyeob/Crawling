from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

def create_new_file():
    print('make new file')

menu = Menu(root)

menu_file = Menu(menu,tearoff = 0) 

menu_file.add_command(label='New File', command = create_new_file)
menu_file.add_command(label='New Window')
menu_file.add_separator()
menu_file.add_command(label='Open File...')
menu_file.add_separator()
menu_file.add_command(label='Savel All',state = 'disable')
menu_file.add_command(label='exit', command = root.quit)

menu.add_cascade(label='File', menu=menu_file)

# Edit menu
menu.add_cascade(label='Edit')

# Language menu 추가
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label='python')
menu_lang.add_radiobutton(label='java')
menu_lang.add_radiobutton(label='C++')

menu.add_cascade(label='Edit', menu=menu_lang)

# View menu 추가
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label='show minimap')

menu.add_cascade(label='Edit', menu=menu_view)

root.config(menu=menu)
root.mainloop()
