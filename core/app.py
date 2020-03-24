#!/usr/bin/env python
# encoding: utf-8
"""
app.py

app class file

(c) 2020 SnooeyNET
"""
from tkinter import *


class App(Tk):
    h_wnd = None

    def __init__(self, *args, **kwargs):
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
        self.config(background="yellow")

    def app_lost_focus(self, event):
        self.config(background="grey")

    def handle_return(self, event):
        print(f"return: event.widget is {event.widget}")
        print(f"focus is {self.focus_get()}")

    def set_event(self):
        self.bind("<FocusIn>", self.app_got_focus)
        self.bind("<FocusOut>", self.app_lost_focus)
        self.bind("<Return>", self.handle_return)

    def set_window(self):
        self.title('Window')
        self.focusmodel(model=None)
        self.attributes("-toolwindow", True)
        self.attributes("-topmost", True)

    def set_window_size(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('%sx%s' % (int(width / 2), int(height / 2)))

    def set_window_position(self):
        self.geometry('-%s-%s' % (1, 1))


if __name__ == '__main__':
    raise Exception('Please launch by main.py')
