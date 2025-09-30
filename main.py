import subprocess
import webbrowser
import time
from win10toast import ToastNotifier
import random
import threading

toaster = ToastNotifier()



messages = [
    "It's time to take a break!",
    "Good job on your studying",
    "Take a little breather",
    "You deserve a break!"
]
subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.2.1.1/bin/pycharm64.exe"])

webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://itskola.net")

def write_reminder():
    while True:
        toaster.show_toast("Reminder!", random.choice(messages), duration = 1)
        time.sleep(3)

thread_write_reminder = threading.Thread(target = write_reminder)
thread_write_reminder.start()

print("Hello world")