from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5
import sys

class CloseBtn():
    def __init__(self,win):
        btn(win)

def btn(win):

    closeBtn = QtWidgets.QPushButton(win)

    closeBtn.setText("X")
    closeBtn.setStyleSheet("color:#ffffff; background:#ff0000; font-weight:bold; font-size:16px")
    closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    closeBtn.move(275,0)
    closeBtn.resize(25,25)
    closeBtn.clicked.connect(close)
    closeBtn.show()

def close():
    sys.exit()