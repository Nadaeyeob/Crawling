from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import time

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

Label(root, text = 'menu').pack(side='top')
Button(root, text = 'order').pack(side='bottom')

frame_burger = Frame(root,relief='solid', bd=1 ) #bd 외곽선 표시
frame_burger.pack(side = 'left', fill='both', expand=True)

Button(frame_burger, text='Hamberger').pack()
Button(frame_burger, text='Chicken').pack()
Button(frame_burger, text='Cheese').pack()

frame_drink = LabelFrame(root,text = 'Drink')
frame_drink.pack(side = 'right', fill='both', expand=True)
Button(frame_drink, text='coke').pack()
Button(frame_drink, text='cider').pack()



root.mainloop()
