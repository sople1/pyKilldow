#!/usr/bin/env python
# encoding: utf-8
"""
fg_wnd.py

use win32 api

(c) 2020 SnooeyNET
"""
import ctypes

# https://github.com/boppreh/mouse/issues/1
# user32 = ctypes.windll.user32
import win32con
import win32gui

"""
it necessary for GetWindowThreadProcessId
"""
user32 = ctypes.WinDLL('user32', use_last_error=True)


class FgWnd:
    """
    for foreground window
    having h_wnd, pid

    """
    h_wnd = None
    pid = None

    def __init__(self):
        self.h_wnd = user32.GetForegroundWindow()
        self.pid = user32.GetWindowThreadProcessId(self.h_wnd, None)

    def __str(self):
        return f"hWind: {self.h_wnd}, pid: {self.pid}"

    def close(self):
        """
        Post WM_CLOSE message to foreground window

        :return: None
        """
        win32gui.PostMessage(self.h_wnd, win32con.WM_CLOSE, 0, 0)

    def kill(self):
        """
        Post WM_DESTROY message to foreground window
        (but it not work for close process?)

        :return: None
        """
        win32gui.PostMessage(self.h_wnd, win32con.WM_DESTROY, 0, 0)


if __name__ == '__main__':
    raise Exception('Please launch by main.py')
