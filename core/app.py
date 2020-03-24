#!/usr/bin/env python
# encoding: utf-8
"""
app.py

app class file

(c) 2020 SnooeyNET
"""
from tkinter import *


class App(Tk):
    """
    Container for remote controler
    """

    h_wnd = None

    def __init__(self, *args, **kwargs):
        """
        close, kill button will be present

        :param args: following TK
        :param kwargs: following TK
        """
        Tk.__init__(self, *args, **kwargs)

        self.btn_close = Button(self, text="close", width=10, height=10, takefocus=0)
        self.btn_close.bind('<Button-1>', lambda event: print("close button pressed"))
        self.btn_close.pack()

        self.btn_kill = Button(self, text="kill", width=10, height=10, takefocus=0)
        self.btn_kill.bind('<Button-1>', lambda event: print("kill button pressed"))
        self.btn_kill.pack()

        self.set_event()
        self.set_window()
        self.set_window_size()
        self.set_window_position()

    def app_got_focus(self, event):
        """
        check focus if this app got focus. but it will be not necessary.

        :param event: TK event
        :return: None
        """
        self.config(background="yellow")

    def app_lost_focus(self, event):
        """
        check focus if this app lost focus. but this app do not have focus.

        :param event: TK event
        :return:
        """
        self.config(background="grey")

    def handle_return(self, event):
        print(f"return: event.widget is {event.widget}")
        print(f"focus is {self.focus_get()}")

    def set_event(self):
        self.bind("<FocusIn>", self.app_got_focus)
        self.bind("<FocusOut>", self.app_lost_focus)
        self.bind("<Return>", self.handle_return)

    def set_window(self):
        """
        Appearance of This App
        only use two button, but must be top most

        :return: None
        """
        self.title('Window')
        self.focusmodel(model=None)
        self.attributes("-toolwindow", True)
        self.attributes("-topmost", True)

    def set_window_size(self):
        """
        no full screen but 1/2 of each (width, height)

        :return: None
        """
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('%sx%s' % (int(width / 2), int(height / 2)))

    def set_window_position(self):
        """
        no full screen but right 10, 10 of each (width, height)

        :return: None
        """
        self.geometry('-%s-%s' % (10, 10))


if __name__ == '__main__':
    raise Exception('Please launch by main.py')
