import settings
import figure_handler as fh
import layer_handler as lh

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from PIL import ImageTk


# Main page class: contains our application
class MainPage(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        # Defining which columns and rows will expand when the window will be resized
        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 0)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_rowconfigure(4, weight = 1)
              
        # Name of the currently opened file
        self.filename = ttk.Label(self, text = settings.FILENAME, font = settings.FONT)
        self.filename.grid(row = 0, column = 0, columnspan = 3, pady = 10)

        # Checkbox to determine whether to use the background approximation as the background
        self.bg_checkbox = ttk.Checkbutton(self, text = "Use the approximated image as background")
        self.bg_checkbox.state(["!alternate"])
        self.bg_checkbox.grid(row = 1, column = 0, pady = 3)

        # Frame with listboxes to choose which layers to display
        self.layer_lists = lh.LayerHandler(self, self)
        self.layer_lists.grid(row = 2, column = 0, sticky = "nsew", pady = (45, 0))

        # Checkbox to determine whether the view should be automatically scaled or not
        self.scaling_checkbox = ttk.Checkbutton(self, text = "Automatically scale the plot and set the view")
        self.scaling_checkbox.state(["!alternate"])
        self.scaling_checkbox.grid(row = 3, column = 0, sticky = "s")

        # Displaying the "Refresh the image" button
        self.refresh = ttk.Button(self, text = "Refresh the figure", command = controller.refresh_figure, state = "disabled")
        refresh_icon = ImageTk.PhotoImage(file = settings.REFRESH)
        self.refresh.config(image = refresh_icon, compound = "right")
        self.refresh.icon = refresh_icon
        self.refresh.grid(row = 4, column = 0, sticky = "n", ipadx = 20, ipady = 10)

        self.f = settings.FIGURE

        # Creating a specific frame to put the Matplotlib widget and the toolbar in
        self.plot_figure = fh.FigureHandler(self, self.f)
        self.plot_figure.grid(row = 2, column = 1, sticky = "nsew", padx = 10, rowspan = 4)
