import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# PyQT5 : C,C++ 로 된 Package들을 이용할 수 있음
# 실행되면 대기 상태 돌입
# Signal -> Event 발생 알림
# SLOT -> Event 처리 (Signal을 SLOT과 연결시키면 된다)

from PyQt5.QtWidgets import * # QtWidgets 이후 label이 표시되는 형태
from PyQt5.QtCore import *
import time

class TestForm(QMainWindow): # 메뉴, 상태표시줄 등 표시
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('PyQt Test')
        self.setGeometry(800,400,500,300) # X,Y width, height (좌상단 0,0)

        btn_1 = QPushButton('click1',self)
        btn_2 = QPushButton('click2',self)
        btn_3 = QPushButton('click3',self)

        btn_1.move(20,20)
        btn_2.move(20,60)
        btn_3.move(20,100)

        btn_1.clicked.connect(self.btn_1_clicked)
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)
        # 사용자 정의 함수가 아닌, 기존 함수 호출

    def btn_1_clicked(self):
        QMessageBox.about(self,'message','clicked')

    def btn_2_clicked(self):
        print('Button clicked') # Console 창에서 확인 가능


if __name__ == '__main__': # Main은 실행시키는 파일 위치라고 생각하면 편함
                           # ex) pyqt_basic_1 에서 import 해서 사용할 경우 Main은 pyqt_basic_1이 됌
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
