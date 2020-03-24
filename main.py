#!/usr/bin/env python
# encoding: utf-8
"""
main.py

main file for app

(c) 2020 SnooeyNET
"""

from core import *

import launcher_win32 as launcher

app = App()
app.btn_close.bind('<Button-1>', lambda event: close_fg())
app.btn_kill.bind('<Button-1>', lambda event: kill_fg())


if __name__ == '__main__':
    launcher.run(app)
