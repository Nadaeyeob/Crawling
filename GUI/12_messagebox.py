from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import time

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가


def info():
    msgbox.showinfo('title','Content')

def warning():
    msgbox.showwarning('title','Content')

def error():
    msgbox.showerror('title','Content')

def okcancel():
    msgbox.askokcancel('title','Content')

def retrycancel():
    msgbox.askretrycancel('title','Content')

def yesno():
    msgbox.askyesno('title','Content')

def yesnocancel():
    response = msgbox.askyesnocancel(title=None,message='Content')
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소
    print(response)
    if response == 1:
        print('yes')
    elif response == 0:
        print('no')
    else:
        print('cancel')

Button(root,command = info, text = 'Alarm').pack()
Button(root,command = warning, text = 'Warning').pack()
Button(root,command = error, text = 'Error').pack()


Button(root,command = okcancel, text = 'cancel').pack()
Button(root,command = retrycancel, text = 'try').pack()
Button(root,command = yesno, text = 'yesno').pack()
Button(root,command = yesnocancel, text = 'yesnocancel').pack()




# Message Box = Error 차 등
root.mainloop()
