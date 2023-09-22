import win32gui
import win32con
import time


def check_current_window_title():
    # Get the handle of the active window
    hwnd = win32gui.GetForegroundWindow()
    # Get the window title
    title = win32gui.GetWindowText(hwnd)
    # Check if the window title contains the word "chrome" or "firefox"
    if ['chrome','firefox','edge'] in title.lower():
        return 'Web browser detected'
    return title.lower()


