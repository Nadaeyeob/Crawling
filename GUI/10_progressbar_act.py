from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# Combobox는 ttk import 필요
progress_var = DoubleVar() # 실수 값 표시 위함
progressbar = ttk.Progressbar(root,maximum = 100, length= 150, variable=progress_var)
progressbar.pack()

def btncmd():
    for i in range(1, 101):
        time.sleep(0.01)

        progress_var.set(i) # progressbar의 값 설정
        progressbar.update() # ui update
        print(progress_var.get())

btn = Button(root, text = 'start', command = btncmd)
btn.pack()

root.mainloop()
