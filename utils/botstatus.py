import sys
import os
import platform

def restart_bot():
    if platform.system() == "Windows":
        os.execv(sys.executable,["python3"] + sys.argv)
    else:
        os.execv(sys.executable,["python3"] + sys.argv)
    sys.exit()

def stop_bot():
    sys.exit()

def clear_console_output():
    if platform.system() == "Windows":
        os.system("cmd /k cls")
    else:
        os.system("bash -c clear")