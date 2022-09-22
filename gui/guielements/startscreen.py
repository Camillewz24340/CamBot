from PyQt5 import QtWidgets, QtGui, QtCore

class StartScreen:
    def __init__(self, win):
        startScreenLabel(win)
        startScreenIcon(win)
        

        


def startScreenLabel(win):
    label = QtWidgets.QLabel(win)
    
    label.setText("CamBot Client")
    label.setStyleSheet("color:#ffffff; font-size:35px; border:none")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.move(0,320)
    label.resize(300,40)
        
    label.show()

def startScreenIcon(win):

    image = QtWidgets.QLabel(win)

    pixmap = QtGui.QPixmap('gui/img/icon.png')

    image.setPixmap(pixmap)
    image.setAlignment(QtCore.Qt.AlignCenter)
    image.setStyleSheet("border: none")
    image.resize(300,220)
    image.move(0,100)

    image.show()