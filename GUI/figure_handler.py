import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class FigureHandler(tk.Frame, Figure):

    def __init__(self, parent, f, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.canvas = FigureCanvasTkAgg(f, master = self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side = "top", fill = "both", expand =True)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(anchor = "center")
