import threading
import os
import time
from win10toast import ToastNotifier
from subprocess import call

from threading import Thread
from time import sleep

notifier = ToastNotifier()

def main():

    botReady = False

    def startBot():
        call(r"python bot.py")
    def startTrayIcon():
        call(r"python trayicon.py")
    def prt():
        notifier.show_toast(
            "CamBot",
            "Starting...",
            duration=2,
            threaded=True
        )

    prtTh = Thread(target=prt)
    prtTh.start()

    trayIconThread = Thread(target=startTrayIcon)
    trayIconThread.start()

    botThread = Thread(target=startBot)
    botThread.start()


    while botReady == False:
        with open("./states/isReady.txt") as f:
            if f.read() == "1":
                print("Bot is ready, notifying...")
                notifier.show_toast(
                    "CamBot",
                    "Ready !",
                    duration=2,
                    threaded=True
                )
                botReady = True
            time.sleep(2)
            f.close()
            if botReady:
                with open("./states/isReady.txt", "w") as f:
                    f.write("0")

    while botReady == True:
        if open("./states/trayStop.txt").read() == "1":
            open("./states/isOnline.txt", "w").write("0")
            open("./states/isReady.txt", "w").write("0")
            open("./states/isRestarting.txt", "w").write("0")
            open("./states/trayStop.txt", "w").write("0")
            open("./states/trayRestart.txt", "w").write("0")
            os.abort()
        if open("./states/isOnline.txt").read() == "0":
            if open("./states/isRestarting.txt").read() == "1":
                notifier.show_toast(
                    "CamBot",
                    "Restarting...",
                    duration=2,
                    threaded=True
                )
                open("./states/isRestarting.txt", "w").write("0")
                botReady = False
                return
            else:
                if open("./states/trayRestart.txt").read() == "1":
                    open("./states/trayRestart.txt", "w").write("0")
                    return
                else:
                    notifier.show_toast(
                        "CamBot",
                        "Stopping...",
                        duration=2,
                        threaded=True
                    )
                    time.sleep(2)
                    os.abort()
            
        time.sleep(2)
                



while True:
    main()