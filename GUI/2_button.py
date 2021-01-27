from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+100+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

btn1 = Button(root, text='button1')
btn1.pack() # pack으로 호출

btn2 = Button(root, padx=320,pady=10, text='button2') # 글자를 기준으로 글자-button 간 넓이 (여백)
btn2.pack()

btn3 = Button(root, padx=10,pady=5, text='button3')
btn3.pack()

btn4 = Button(root, width=10,height=5, text='button4') # 글자 무시하고 button 넓이
btn4.pack()

btn5 = Button(root, fg='red',bg='yellow', text='button5') # fg 글자색, bg 바탕색
btn5.pack()

photo = PhotoImage(file='C:/Users/sw993/Crawling/Section6/resource/title_ico.png')
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print('Clicked')

btn7 = Button(root, text='activate button', command=btncmd)
btn7.pack()



root.mainloop()
