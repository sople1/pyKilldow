#!/usr/bin/env python
# encoding: utf-8
"""
launcher_win32.py

launcher file

(c) 2020 SnooeyNET
"""

import win32api
import win32con
import pywintypes


def run(app: object) -> object:
    return run_win32(app)


def run_win32(app: object) -> object:
    app.lift()

    app.h_wnd = pywintypes.HANDLE(int(app.frame(), 16))
    ex_style = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE
    win32api.SetWindowLong(app.h_wnd, win32con.GWL_EXSTYLE, ex_style)

    return app.mainloop()


if __name__ == '__main__':
    raise Exception('Please launch by main.py')
