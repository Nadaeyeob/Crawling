from PyQt5.QtCore import QObject,pyqtSignal, pyqtSlot
from PyQt5.QtMultimedia import QSound

class IntroWorker(QObject): # Pyqt 위에서 실행되기 때문에 QObject로 상속 받음
    startMsg = pyqtSignal(str,str)
    @pyqtSlot()
    def playBgm(self):
        self.intro = QSound('C:/Users/sw991/Crawling/Section6/resource/intro.wav')
        self.intro.play()
        self.startMsg.emit('Anonymous',self.intro.fileName())
