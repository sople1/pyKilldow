#!/usr/bin/env python
# encoding: utf-8
"""
fg_wind.py

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


class FgWind:
    """
    for foreground window
    having h_wnd, pid

    """
    h_wnd = None
    pid = None

    def __init__(self):
        self.h_wnd = user32.GetForegroundWindow()
        self.pid = user32.GetWindowThreadProcessId(self.h_wnd, None)


def close_fg():
    """
    Post WM_CLOSE message to foreground window

    :return: None
    """
    fg = FgWind()
    win32gui.PostMessage(fg.h_wnd, win32con.WM_CLOSE, 0, 0)


def kill_fg():
    """
    Post WM_DESTROY message to foreground window
    (but it not work for close process?)

    :return: None
    """
    fg = FgWind()
    win32gui.PostMessage(fg.h_wnd, win32con.WM_DESTROY, 0, 0)


if __name__ == '__main__':
    raise Exception('Please launch by main.py')
