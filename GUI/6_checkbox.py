from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# 선택자
checkvar1 = IntVar() # chkvar에 int 형으로 값 저장
checkbox1 = Checkbutton(root, text='오늘 하루 보지 않기', variable= checkvar1)
# checkbox.select() # 자동 선택 처리
# checkbox.deselect() # 선택 해제 처리
checkbox1.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = '일주일 동안 보지 않기',variable=checkvar2)
checkbox2.pack()

def btncmd():
    print('checkbox1 : checkvar1',checkvar1.get()) # 0 : Check 해제, 1 : Check
    print('checkbox2 : checkvar2'checkvar2.get())
    # checkvar에 0,1로 저장이 됌, variable에 저장되는 값이 0,1 이고 이를 통해 if 등으로 구현하면 될 듯

btn = Button(root, text = 'click', command = btncmd)
btn.pack()

root.mainloop()
