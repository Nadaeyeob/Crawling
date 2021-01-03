import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# PyQT5 : C,C++ 로 된 Package들을 이용할 수 있음
# 실행되면 대기 상태 돌입
# Signal -> Event 발생 알림
# SLOT -> Event 처리 (Signal을 SLOT과 연결시키면 된다)

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
from pyqt_basic_ui import Ui_MainWindow

###### Ui를 XML 로 불러서 오는 방법 ######

# form_class = uic.loadUiType('C:/Users/sw991/Crawling/Section6/example/pyqt_basic_3.ui')[0]
# class TestForm(QMainWindow,form_class): # 메뉴, 상태표시줄 등 표시
#     def __init__(self):
#         super().__init__() # 부모 생성자 호출
#         self.setupUi(self)

###### Python file에서 직접 호출하는 방법 ######
class TestForm(QMainWindow,Ui_MainWindow): # 메뉴, 상태표시줄 등 표시
    def __init__(self):
        super().__init__() # 부모 생성자 호출
        self.setupUi(self)


if __name__ == '__main__': # Main은 실행시키는 파일 위치라고 생각하면 편함
                           # ex) pyqt_basic_1 에서 import 해서 사용할 경우 Main은 pyqt_basic_1이 됌
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
