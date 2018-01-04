import settings
import figure_handler as fh
import layer_handler as lh
import background_handler as bh

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
    
    def __init__(self, parent, controller, network, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.network = network

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

        # Background handler: makes sure that both checkboxes cannot be checked at the same time and potential loads a background image
        self.bg_handler = bh.BackgroundHandler(self, self)
        self.bg_handler.grid(row = 1, column = 0, columnspan = 2, pady = 3, padx = 20, sticky = "w")

        # Frame with listboxes to choose which layers to display
        self.layer_lists = lh.LayerHandler(self, self)
        self.layer_lists.grid(row = 2, column = 0, sticky = "nsew", pady = (45, 0))

        # Creating a specific frame to put the Matplotlib widget and the toolbar in
        self.plot_figure = fh.FigureHandler(self)
        self.plot_figure.grid(row = 2, column = 1, sticky = "nsew", padx = 10, rowspan = 4)

        # Displaying the "Refresh the image" button
        self.refresh = ttk.Button(self, text = "Refresh the figure", command = lambda:self.plot_figure.refresh_figure(self.network), state = "disabled")
        refresh_icon = ImageTk.PhotoImage(file = settings.REFRESH)
        self.refresh.config(image = refresh_icon, compound = "right")
        self.refresh.icon = refresh_icon
        self.refresh.grid(row = 4, column = 0, sticky = "n", ipadx = 20, ipady = 10)
        
        
    # When a file is opened or closed, refresh the label displaying its name
    def refresh_filename(self, filename):
        self.filename.config(text = filename)

    def activate_refresh(self):
        self.refresh.config(state = "normal")

    def deactivate_refresh(self):
        self.refresh.config(state = "disabled")
        

    # When a figure is opened or closed, refresh the figure canvas accordingly
    def reset_figure(self, network):
        
        if settings.OPENED:
            self.plot_figure.refresh_figure(network)
        else:
            self.plot_figure.f.clear()
            self.plot_figure.f.tight_layout()
            self.plot_figure.canvas.draw()

