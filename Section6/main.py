import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic # Layout 파일 불러오기
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl

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

        # 재생여부
        self.is_play = False

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

    # Signal 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # self.initAuthActive.()
        self.webView.loadProgress.connect(self.showProgressBrowserLoading)
        self.FileNaviButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.appendDate)

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
            self.append_log_msg('Login Success')


        else:
            pass

    def append_log_msg(self,act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = self.user_id + ':' + act + '- (' + nowDatetime + ')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg) # appendPlainText, insertPlainText

        # 활동 Log 저장(또는 DB를 사용 추천)
        # 상대 경로로 저장하는 방법도 확인 필요
        with open('C:/Users/sw991/Crawling/Section6/log/log.txt','a') as f: #'a' append option
            f.write(app_msg+'\n')

    def load_url(self):
        url = self.urlTextEdit.text().strip() # strip = 공백제거
        v = re.compile('^https://www.youtube.com/?') # regex 정규 표현식으로 내용이 방대함

        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webView.load(QUrl('about:blank')) # internet browser에 about:blank 할시 공백 page
            self.previewButton.setText('재생')
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.StartButton.setEnabled(False)
            self.StreamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg('인증완료')

        else:
            if v.match(url) is not None: # url과 맞지 않은 경우
                self.append_log_msg('Play Click')
                self.webView.load(QUrl(url))
                self.showStatusMsg(url+'  재생 중')
                self.previewButton.setText('중지')
                self.is_play = True
                self.StartButton.setEnabled(True)
            else:
                QMessageBox.about(self,'URL 형식 오류','Youtube 주소 형식이 아닙니다.')
                self.urlTextEdit.clear() # URL 오입력으로 삭제
                self.urlTextEdit.setFocus(True) # 새로운 Focus

    @pyqtSlot(int) # 명시적으로 int가 넘어온다고 표시해줘야함
    def showProgressBrowserLoading(self,v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        # File 선택
        # fname = QFileDialog.getOpenFileName(self)
        # self.pathTextEdit.setText(fname[0]) # file 선택 기능

        # 경로 선택
        fpath = QFileDialog.getExistingDirectory(self,'Select Directory')
        self.pathTextEdit.setText(fpath)

    @pyqtSlot()
    def appendDate(self):
        cur_date = self.calendarWidget.selectedDate()
        # 한글로 요일 등 출력
        print('click date : ',self.calendarWidget.selectedDate().toString())
        print('cur_date : ',cur_date)
        print(str(cur_date.year())+'-'+str(cur_date.month())+'-'+str(cur_date.day()))
        self.append_log_msg('Calender Click')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viwer_main = Main()
    you_viwer_main.show()
    app.exec_()
