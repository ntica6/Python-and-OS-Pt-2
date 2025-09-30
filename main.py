import subprocess
import webbrowser
import time
from win10toast import ToastNotifier
import random

toaster = ToastNotifier()



messages = [
    "It's time to take a break!",
    "Good job on your studying",
    "Take a little breather",
    "You deserve a break!"
]
subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.2.1.1/bin/pycharm64.exe"])

webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://google.com")

while True:
    toaster.show_toast("Reminder!", random.choice(messages), duration = 1)
    time.sleep(3)
