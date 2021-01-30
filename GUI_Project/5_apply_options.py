from tkinter import * # __all__
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog # __all__ 에 해당하지 않음
import time
import os
from PIL import Image

root = Tk()
root.title('GUI') # title 설정

# root.geometry('640x480')
root.geometry('640x580+800+300') #가로 x 세로 + 가로 좌표 + 세로 좌표
root.resizable(False,False) # x,y 값 변경 불가

# 파일 추가
def add_file():
    files= filedialog.askopenfilenames(title='이미지 파일 선택',\
        filetypes=(('PNG 파일','*.png'), ('모든 파일','*.*')),\
        initialdir = 'C:/Users/sw991/OneDrive/Desktop/')
    for file in files:
        list_file.insert(END, file)

    # for file in files:
    #     print(file)

# 선택 삭제
def del_file():
    for index in reversed(list_file.curselection()): # 선택된 index 반환
    # list.reverse() -> 실제로 바뀜
    # list.reversed() -> 실제로 바뀌지 않고 넘겨만 받음
        list_file.delete(index)
# 저장 경로
def browse_save_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(END, folder_selected)

def merge_image():

    try:
        # 가로 넓이
        img_width = combobox_width.get()
        if img_width == '원본유지':
            img_width = -1 # -1일 때는 원본 기준으로
        else:
            img_width = int(img_width)

        # 간격
        img_space = combobox_space.get()
        if img_space == '좁게':
            img_space = 30
        elif img_space == '보통':
            img_space = 60
        elif img_space == '넓게':
            img_space = 90
        else:
            img_space = 0

        # 포맷
        img_format = combobox_format.get().lower() # 소문자로 변경

        images = [Image.open(x) for x in list_file.get(0,END)]
        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1]/x.size[0])) for x in images]
        else:
            img_sizes = [(x.size[0],x.size[1]) for x in images]

        widths, heights = zip(*(x.size for x in images))
        max_width, total_height = max(widths) , sum(heights)

        # 최종 파일
        if img_space > 0:
            total_height += (img_space * (len(images) -1))
        result_img = Image.new('RGB', (max_width,total_height), (255,255,255)) # (255,255,255) 배경 흰색
        y_offset = 0
        # for img in images:
        #     result_img.paste(img,(0,y_offset))
        #     y_offset += img.size[1]

        # 프로그레스바 를 위해 enumerate 추가
        for idx, img in enumerate(images):
            if img_width>-1:
                img = img.resize(image_sizes[idx])
            result_img.paste(img,(0,y_offset))
            y_offset += (img.size[1] + img_space) # height 값 + 사용자가 지정한 간격

            progress = (idx+1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        filename = 'nadae.' + img_format
        dest_path = os.path.join(txt_dest_path.get(),filename)
        result_img.save(dest_path)
        msgbox.showinfo('알림','작업이 완료 됐습니다.')
    except Exception as err: # 예외처리
        msgbox.showerror('에러',err)

def start():
    # 각 옵션들 값 확인
    if list_file.size() == 0:
        msgbox.showwarning('경고','이미지 파일을 추가하세요')
        return
    if len(txt_dest_path.get()) ==0:
        msgbox.showwarning('경고','저장 경로를 선택하세요')
        return

    merge_image()

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx= 5, pady=5)
btn_add_file = Button(file_frame, padx=5, pady=5, width = 12, text = '파일 추가', command = add_file)
btn_add_file.pack(side='left')
btn_del_file = Button(file_frame, padx=5, pady=5, width = 12, text = '선택 삭제', command = del_file)
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
btn_txt_dest = Button(path_frame, text = '찾아보기', command = browse_save_path)
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
btn_start = Button(run_frame, padx = 5, pady = 5, text = '시작',width = 10, command = start)
btn_start.pack(side='right', padx= 5, pady=5)

root.mainloop()
