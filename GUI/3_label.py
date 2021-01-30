from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+100+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# label = 글자나, 이미지만 보여줌

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file='C:/Users/sw993/Crawling/Section6/resource/title_ico.png')

label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='또 만나요')

    # photo1 = PhotoImage(file='C:/Users/sw993/Crawling/Section6/resource/Youtube-icon.png')
    # 전역 변수가 아니라 이대로 두면 삭제됌

    global photo1
    photo1 = PhotoImage(file='C:/Users/sw993/Crawling/Section6/resource/Youtube-icon.png')

    label2.config(image=photo1)

btn = Button(root, text='click', command=change)
btn.pack()

root.mainloop()
