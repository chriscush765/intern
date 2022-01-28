import subprocess
import pyautogui
import win32gui
import win32process
import win32api
import time
import psutil

class WindowUtils:
        
    def waitForProgramOpen(self, pid):
        program_open = False
        while not program_open:
            window_name = self.getWindowName(pid)
            if window_name != None:
                break
            else:
                time.sleep(.5)
        return 

    def getWindowName(self, pid):
        def findWindow(window_pid, output_list):
            process_handle = win32process.GetWindowThreadProcessId(window_pid)
            if pid == int(process_handle[1]):  
                output_list.append(win32gui.GetWindowText(window_pid))

        window_name = list()
        win32gui.EnumWindows(findWindow, window_name)
        if len(window_name) == 0:
            return None
        else:
            return window_name[0]

    def getWindowCoords(self, pid):
        window_name = self.getWindowName(pid)
        window = win32gui.FindWindow(None, window_name)
        placement_info = win32gui.GetWindowPlacement(window)
        position = placement_info[4]
        return position