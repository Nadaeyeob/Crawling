import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# PyQT5 : C,C++ 로 된 Package들을 이용할 수 있음

from PyQt5.QtWidgets import * # QtWidgets 이후 label이 표시되는 형태
import time

app = QApplication(sys.argv)
# print(sys.argv) # 현재 File이 실행되는 경로 확인
label = QLabel('PyQT First Test!')
label.show()

print('Before Loop',time.time())
app.exec_()
print('After Loop',time.time())
# 한번 실행하면 Loop로 계속 실행 중
