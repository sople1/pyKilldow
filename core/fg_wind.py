#!/usr/bin/env python
# encoding: utf-8
"""
fg_wind.py

use win32 api

(c) 2020 SnooeyNET
"""
import ctypes
from ctypes import c_short, c_char, c_uint8, c_int32, c_int, c_uint, c_uint32, c_long, Structure, CFUNCTYPE, POINTER
from ctypes.wintypes import WORD, DWORD, BOOL, HHOOK, MSG, LPWSTR, WCHAR, WPARAM, LPARAM, LONG, HMODULE, LPCWSTR, \
    HINSTANCE, HWND

# https://github.com/boppreh/mouse/issues/1
# user32 = ctypes.windll.user32
import win32con
import win32gui

user32 = ctypes.WinDLL('user32', use_last_error=True)


class FgWind:
    h_wnd = None
    pid = None

    def __init__(self):
        self.h_wnd = user32.GetForegroundWindow()
        self.pid = user32.GetWindowThreadProcessId(self.h_wnd, None)


def close_fg():
    fg = FgWind()
    win32gui.PostMessage(fg.h_wnd, win32con.WM_CLOSE, 0, 0)


def kill_fg():
    fg = FgWind()
    win32gui.PostMessage(fg.h_wnd, win32con.WM_DESTROY, 0, 0)


if __name__ == '__main__':
    raise Exception('Please launch by main.py')
