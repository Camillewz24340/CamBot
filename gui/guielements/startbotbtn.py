from tkinter import W
from PyQt5 import QtWidgets, QtGui, QtCore


def startBotAction(win:QtWidgets.QMainWindow):
    print(win)
        

        


def startBtn(win:QtWidgets.QMainWindow):
    winObject = win
    btn = QtWidgets.QPushButton(win)
    
    btn.setText("Start Bot")
    btn.setStyleSheet("color:#ffffff; font-size:35px; border:none; border-radius:20px; background:#1f0044;")
    btn.move(0,400)
    btn.resize(300,40)
    btn.clicked.connect(startBotAction(win=winObject))
        
    btn.show()