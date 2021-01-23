import pyautogui as pe
import os, time, sys
from win10toast import ToastNotifier
from infi.systray import SysTrayIcon
from os.path import expanduser as eu


def resource_path(relative_path):
    """is used for pyinstaller so it can read the relative path"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

#resources
ico = resource_path("./gui/logo.ico")
toaster = ToastNotifier()
home = eu("~")
t = time.localtime()
current_time = time.strftime("%Y%m%d_%H%M%S", t)

try:
    os.mkdir(eu("~"+"\\pictures\\screenshot\\"))
    home = eu("~"+"\\pictures\\screenshot\\")
except FileExistsError:
    home = eu("~"+"\\pictures\\screenshot\\")


def notification(message):
    """Windows10 notification"""
    toaster.show_toast("Printscreen",
                   message,
                   icon_path=ico,
                   duration=3,
                   threaded=True)


def printScr(systray):
    """takes screenshot and saves it after value in wait"""
    time.sleep(1)
    ss = pe.screenshot()
    ss.save(home+"Screenshot_"+current_time+".png")
    time.sleep(0.5)
    notification("Screenshot saved in "+home)

def openFolder(systray):
    """opens the screenshot folder"""
    os.startfile(home)


menu_options = (("Screenshot", None, printScr),("Open folder",None, openFolder))
systray = SysTrayIcon("./gui/logo.ico", "Screenshot", menu_options)
systray.start()
