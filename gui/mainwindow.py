import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import os
import time
from gui.guielements import startscreen, closebtn, startbotbtn

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("CamBot Client")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setGeometry(100,100,300,450)
        self.setFixedSize(300,450)
        self.setStyleSheet("background:#000e30; border:1px solid #000000")
        self.setWindowIcon(QtGui.QIcon('gui/img/icon.png'))
        self.show()

        startscreen.StartScreen(self)
        closebtn.CloseBtn(self)
        startbotbtn.startBtn(self)

        app.exec()