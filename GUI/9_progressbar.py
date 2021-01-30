from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# Combobox는 ttk import 필요
progressbar = ttk.Progressbar(root,maximum = 100, mode='indeterminate')
progressbar.start(10) # 10 ms 마다 움직임, mode 값 indeterminate 와 함께 언제 끝날지 모르는 작업 설정
progressbar.pack()

progressbar1 = ttk.Progressbar(root,maximum = 100, mode='determinate')
progressbar1.start(10)
progressbar1.pack()


def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text = 'stop', command = btncmd)
btn.pack()

root.mainloop()
