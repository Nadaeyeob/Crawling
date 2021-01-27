from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+100+300') #가로 x 세로 + 가로 좌표 + 세로 좌표

root.resizable(False,False) # x,y 값 변경 불가

root.mainloop()
