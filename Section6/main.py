import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic # Layout 파일 불러오기

import re # 정규 표현식
import datetime

# 절대 경로
# form_class = uic.loadUiType('C:/Users/sw991/Crawling/Section6/ui/ui_ver1.0.ui')[0]
# ui 파일을 python 파일로 변경하여 진행(naming 등 목적)
# 명령어 : pyuic5 -x 이름.ui -o 이름.py 이후 lib으로 이동
from lib.Ui_Ver import Ui_MainWindow


# 상대 경로
# import os
# os.path.('C:/Users/sw991/Crawling/Section6/ui/ui_ver1.0.ui') 에 + join 하여 사용

#PyQt5 에 webengineview 를 pip install로 따로 처리해서 진행했음
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viwer_main = Main()
    you_viwer_main.show()
    app.exec_()
