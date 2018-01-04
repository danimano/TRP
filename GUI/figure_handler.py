import settings

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from pear.create_image import create_image

class FigureHandler(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.f = settings.FIGURE
        self.f.patch.set_facecolor('none')
        self.resolution = [501, 501]

        self.image = None

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


    def refresh_figure(self, network):
        print("Refresh figure!")
        self.f.clear()
        print(network)

        # Vector containing the indices of the layers to draw
        layers_to_print = self.parent.layer_lists.get_layers_to_draw()
        
        if self.parent.bg_handler.bg_checkbox.instate(["selected"]):
            print("Use approximated image as background!")
            figure = create_image(network, layers_to_print, self.resolution, None, True)
            
            
        elif self.parent.bg_handler.img_checkbox.instate(["selected"]):
            print("Image as background!")
            if self.parent.bg_handler.background == []:
                message = "No image background was loaded. The figure will be generated on a blank background. Please select an image as your background next time."
                tk.messagebox.showwarning("No background loaded", message)
                figure = create_image(network, layers_to_print, self.resolution, None, False)

            else:
                figure = create_image(network, layers_to_print, self.resolution, self.parent.bg_handler.background, False)

        else:
            print("Blank background!")
            figure = create_image(network, layers_to_print, self.resolution, None, False)

        self.image = figure;
        ax = self.f.add_subplot(1, 1, 1)
        ax.imshow(figure, cmap = "gray", interpolation = "nearest", origin = "upper")
        ax.axes.set_aspect('equal')
        self.canvas.draw()


    def reset_figure(self):
        self.f = settings.FIGURE
