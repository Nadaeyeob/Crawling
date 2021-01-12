import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.user_id = None
        self.user_pw = None

    def setupUI(self):
        self.setGeometry(300,400,300,100)
        self.setWindowTitle('Sign In')
        self.setFixedSize(300,100)

        label1 = QLabel('ID : ')
        label2 = QLabel('PassWord : ')

        self.LineEdit1 = QLineEdit() # ID
        self.LineEdit2 = QLineEdit() # Password
        self.LineEdit2.setEchoMode(QLineEdit().Password)

        self.pushButton = QPushButton('Login')
        self.pushButton.clicked.connect(self.submitLogin)

        layout = QGridLayout()

        layout.addWidget(label1,0,0) # (label, 0행, 0열에 배치)
        layout.addWidget(self.LineEdit1,0,1)
        layout.addWidget(self.pushButton,0,2)
        layout.addWidget(label2,1,0)
        layout.addWidget(self.LineEdit2,1,1)

        self.setLayout(layout)

    def submitLogin(self):
        self.user_id = self.LineEdit1.text()
        self.user_pw = self.LineEdit2.text()

        if self.user_id is None or self.user_id =='' or not self.user_id:
            QMessageBox.about(self,'인증오류','ID를 입력하세요')
            self.LineEdit1.setFocus(True)
            return None
        if self.user_pw is None or self.user_pw =='' or not self.user_pw:
            QMessageBox.about(self,'인증오류','PW를 입력하세요')
            self.LineEdit2.setFocus(True)

            return None

        # 이 부분에서 필요한 경우 실제 Local DB 또는 서버로 연동 후
        # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣으면 됌

        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginDialog = AuthDialog()
    loginDialog.show()
    app.exec_()
