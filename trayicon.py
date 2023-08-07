from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys
app = QApplication([]) 
app.setQuitOnLastWindowClosed(False) 
  
def restart():
    open("./states/trayRestart.txt", "w").write("1")
    sys.exit(0)
def ex():
    open("./states/trayStop.txt", "w").write("1")
    sys.exit(0)

# Adding an icon 
icon = QIcon("icon.ico") 
  
# Adding item on the menu bar 
tray = QSystemTrayIcon() 
tray.setIcon(icon) 
tray.setVisible(True) 
  
# Creating the options 
menu = QMenu() 
menu.setStyleSheet("background:#003; color:#fff; font-family:sans-serif; font-size:20px")

restartOption = QAction("Restart")
restartOption.triggered.connect(restart)
menu.addAction(restartOption) 
  
# To quit the app 
Exit = QAction("Exit") 
Exit.triggered.connect(ex) 
menu.addAction(Exit) 
  
# Adding options to the System Tray 
tray.setContextMenu(menu) 
app.exec_()