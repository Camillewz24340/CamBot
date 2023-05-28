import sys
import os
import platform

def stop_bot():
    sys.exit()

def clear_console_output():
    if platform.system() == "Windows":
        os.system("cmd /c cls")
    else:
        os.system("bash -c clear")