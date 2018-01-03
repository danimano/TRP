import settings

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class FigureHandler(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.f = settings.FIGURE

        self.canvas = FigureCanvasTkAgg(self.f, master = self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side = "top", fill = "both", expand = True)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(anchor = "center")


    def refresh_canvas(self):
        self.canvas.get_tk_widget().destroy()
        self.canvas._tkcanvas.destroy()
        self.toolbar.destroy()

        self.canvas = FigureCanvasTkAgg(self.f, master = self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side = "top", fill = "both", expand = True)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(anchor = "center")


    def refresh_figure(self):
        print("Refresh figure!")
        self.f.clear()

        layer_to_print = self.parent.layer_lists.get_layers_to_draw()
        
        if self.parent.bg_handler.bg_checkbox.instate(["selected"]):
            print("Use approximated image as background!")
            
        elif self.parent.bg_handler.img_checkbox.instate(["selected"]):
            print("Image as background!")
            if self.parent.bg_handler.background == None:
                message = "No image background was loaded. The figure will be generated on a blank background. Please select an image as your background next time."
                tk.messagebox.showwarning("No background loaded", message)

            else:
                print("Perform computation")

        else:
            print("Blank background!")


    def reset_figure(self):
        self.f = settings.FIGURE
