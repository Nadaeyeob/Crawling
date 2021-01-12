import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic # Layout 파일 불러오기
from PyQt5.QtCore import pyqtSlot, pyqtSignal

import re # 정규 표현식
import datetime

# 절대 경로
# form_class = uic.loadUiType('C:/Users/sw991/Crawling/Section6/ui/ui_ver1.0.ui')[0]
# ui 파일을 python 파일로 변경하여 진행(naming 등 목적)
# 명령어 : pyuic5 -x 이름.ui -o 이름.py 이후 lib으로 이동
from lib.Ui_Ver import Ui_MainWindow
from lib.AuthDialog import AuthDialog

# 상대 경로
# import os
# os.path.('C:/Users/sw991/Crawling/Section6/ui/ui_ver1.0.ui') 에 + join 하여 사용

#PyQt5 에 webengineview 를 pip install로 따로 처리해서 진행했음
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 초기 잠금
        self.initAuthLock()
        self.initSignal()

        # login 관련 변수 선언
        self.user_id = None
        self.user_pw = None

    # 기본 UI 비활성화
    def initAuthLock(self): # 인증받기전에 쓰지 못하게 하기 위해서 Lock
        self.previewButton.setEnabled(False) # Check Button을 누를 수 없음
        self.FileNaviButton.setEnabled(False)
        self.StreamCombobox.setEnabled(False)
        self.StartButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')
    # 기본 UI 활성화
    def initAuthActive(self):
        # Start Button은 URL 입력시 활성화 되도록 할 예정
        self.previewButton.setEnabled(True)
        self.FileNaviButton.setEnabled(True)
        self.StreamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        # self.initAuthActive.()

    @pyqtSlot()
    def authCheck(self):
        dig = AuthDialog()
        dig.exec_()
        self.user_id = dig.user_id # dig로 객체를 만들었기 때문에 자식 Class의 User_id 사용
        self.user_pw = dig.user_pw

        # print('id: %s pass word: %s'%(self.user_id,self.user_pw))

        # if False:
        #     pass
        # else:
        #     QMessageBox.about(self,'인증오류','ID 또는 PW 인증 오류')

        if True:
            self.initAuthActive()
            self.loginButton.setText('인증완료')
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setEnabled(True)
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viwer_main = Main()
    you_viwer_main.show()
    app.exec_()
