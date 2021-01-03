import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *


class TestForm(QMainWindow): # 메뉴, 상태표시줄 등 표시
    def __init__(self):
        super().__init__() # 부모 초기화
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('PyQt Test')
        self.setGeometry(800,400,500,500) # X,Y width, height (좌상단 0,0)

        label_1 = QLabel('입력테스트',self)
        label_2 = QLabel('출력테스트',self)

        label_1.move(20,20)
        label_2.move(20,60)

        self.lineEdit = QLineEdit('',self) # Default 값
        self.plainEdit = QtWidgets.QPlainTextEdit(self)
        # self.plainEdit.setReadOnly(True) -> 출력만 가능하게끔 만듬

        self.lineEdit.move(90,20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,361,231)) # X,Y width, height (좌상단 0,0)

        self.lineEdit.textChanged.connect(self.lineEditChanged) # Signal은 Connect로
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        # Status Bar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())
    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())
        # self.plainEdit.insertPlainText(self.lineEdit.text()) # 줄바꿈을 하지 않음
        self.lineEdit.clear() # Enter 이후 초기화 시킴

if __name__ == '__main__': # Main은 실행시키는 파일 위치라고 생각하면 편함
                           # ex) pyqt_basic_1 에서 import 해서 사용할 경우 Main은 pyqt_basic_1이 됌
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
