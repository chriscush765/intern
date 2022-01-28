import subprocess
import pyautogui
import win32gui
import win32process
import win32api
import time
import psutil
from util import WindowUtils

filename = r"redshift_v3.0.54_setup.exe"

redshift = subprocess.Popen(filename)
redshift_pid = redshift.pid 


wu = WindowUtils()


wu.waitForProgramOpen(redshift_pid)

print("open!")

#get window coordinates
coords = wu.getWindowCoords(redshift_pid)

print(coords)


