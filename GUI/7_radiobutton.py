from tkinter import *

root = Tk()
root.title('GUI') # title 설정
# root.geometry('640x480')
root.geometry('640x480+1000+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# Radio Button : 여러가지 항목 중에 고름

Label(root,text='메뉴를 선택하세요').pack()

# Radiobutton 에선 항목이 그룹으로 묶여 있어야함
burger_var = IntVar()
btn_burger1 = Radiobutton(root,text='햄버거',value=1, variable=burger_var)
btn_burger2 = Radiobutton(root,text='Cheese',value=2, variable=burger_var)
btn_burger3 = Radiobutton(root,text='photato',value=3, variable=burger_var)

btn_burger1.select()

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root,text='음료를 선택하세요').pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root,text='Coke',value='coke',variable=drink_var)
btn_drink2 = Radiobutton(root,text='Cidar',value='cidar',variable=drink_var)
btn_drink1.select()

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text = 'order', command = btncmd)
btn.pack()

root.mainloop()
