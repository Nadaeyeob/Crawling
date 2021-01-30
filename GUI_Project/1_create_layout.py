from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import time
import os

root = Tk()
root.title('GUI') # title 설정

# root.geometry('640x480')
root.geometry('640x540+800+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx= 5, pady=5)
btn_add_file = Button(file_frame, padx=5, pady=5, width = 12, text = '파일 추가')
btn_add_file.pack(side='left')
btn_del_file = Button(file_frame, padx=5, pady=5, width = 12, text = '선택 삭제')
btn_del_file.pack(side='right')

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx= 5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand = scrollbar.set)
list_file.pack(side='left',fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root,text='저장경로')
path_frame.pack(fill='x', padx= 5, pady=5,ipady=5)
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left',fill='x', expand=True, ipady=4, padx= 5, pady=5) # ipad : innerpad 높이 변경
btn_txt_dest = Button(path_frame, text = '찾아보기')
btn_txt_dest.pack(side='right', padx= 5, pady=5,ipady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text='옵션')
option_frame.pack(fill='x', padx= 5, pady=5)
# 가로 넓이
label_width = Label(option_frame, text = '가로 넓이', width=8)
label_width.pack(side='left', padx= 5, pady=5)
opt_width = ['원본유지','1024','800','640']
combobox_width = ttk.Combobox(option_frame, state='readonly', values=opt_width, width=10)
combobox_width.current(0)
combobox_width.pack(side='left', padx= 5, pady=5)
# 간격 넓이
label_space = Label(option_frame, text = '간격 넓이', width=8)
label_space.pack(side='left', padx= 5, pady=5)
opt_space = ['없음','좁게','보통','넓게']
combobox_space = ttk.Combobox(option_frame, state='readonly', values=opt_space, width=10)
combobox_space.current(0)
combobox_space.pack(side='left', padx= 5, pady=5)
# 파일 포맷
label_format = Label(option_frame, text = '파일 포맷', width=8)
label_format.pack(side='left', padx= 5, pady=5)
opt_format = ['png','jpg','bmp']
combobox_format = ttk.Combobox(option_frame, state='readonly', values=opt_format, width=10)
combobox_format.current(0)
combobox_format.pack(side='left', padx= 5, pady=5)

# 진행 상황
progress_frame = LabelFrame(root,text='진행상황')
progress_frame.pack(fill='x', padx= 5, pady=5)
p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum = 100, variable=p_var)
progress_bar.pack(fill='x', padx= 5, pady=5,ipady=5)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill='x', padx= 5, pady=5)
btn_close = Button(run_frame, padx= 5, pady= 5, text = '닫기' ,width = 10, command = root.quit)
btn_close.pack(side='right', padx= 5, pady=5)
btn_start = Button(run_frame, padx = 5, pady = 5, text = '시작',width = 10)
btn_start.pack(side='right', padx= 5, pady=5)

root.mainloop()
