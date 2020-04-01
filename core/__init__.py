from .app import App
from .fg_wnd import FgWnd


def close_fg():
    fg = FgWnd()
    return fg.close()


def kill_fg():
    fg = FgWnd()
    return fg.kill()