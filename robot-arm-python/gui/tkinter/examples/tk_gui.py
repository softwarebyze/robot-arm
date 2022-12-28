# from tkinter import *
#
#
# class Application(Frame):
#
#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"] = "red"
#         self.QUIT["command"] = self.quit
#
#         self.QUIT.pack({"side": "left"})
#
#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi
#
#         self.hi_there.pack({"side": "left"})
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#
# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()

#
# # Use Tkinter for python 2, tkinter for python 3
# import tkinter as tk
#
#
# class MainApplication(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.parent = parent
#
#     # asdf
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     MainApplication(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()

import matplotlib

matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Entry, Button, Tk


class mclass:
    def __init__(self, window):
        self.window = window
        self.box = Entry(window)
        self.button = Button(window, text="check", command=self.plot)
        self.box.pack()
        self.button.pack()

    def plot(self):
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v = np.array([16, 16.31925, 17.6394, 16.003, 17.2861, 17.3131, 19.1259, 18.9694, 22.0003, 22.81226])
        p = np.array([16.23697, 17.31653, 17.22094, 17.68631, 17.73641, 18.6368,
                      19.32125, 19.31756, 21.20247, 22.41444, 22.11718, 22.12453])

        fig = Figure(figsize=(6, 6))
        a = fig.add_subplot(111)
        a.scatter(v, x, color='red')
        a.plot(p, range(2 + max(x)), color='blue')
        a.invert_yaxis()

        a.set_title("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()


window = Tk()
start = mclass(window)
window.mainloop()
