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
from pear.create_image_from_lines import create_image_from_lines

class FigureHandler(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.f = settings.FIGURE
        self.f.patch.set_facecolor('none')

        self.resolution = settings.RESOLUTION
        self.previous_resolution = None

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
        self.parent.update_refreshing_label(True)
        self.f.clear()

        # Vector containing the indices of the layers to draw
        layers_to_print = self.parent.layer_lists.get_layers_to_draw()

        # If the background approximation is checked
        if self.parent.bg_handler.bg_checkbox.instate(["selected"]):
            self.resolution = settings.RESOLUTION
            # Recomputing everything only if there is a change in resolution
            if self.resolution != self.previous_resolution:                
                figure = create_image(network, layers_to_print, self.resolution, None, True)
                self.previous_resolution = self.resolution
            else:
                figure = create_image_from_lines(network.get_lines(), layers_to_print, self.resolution, None, network, True)

        # If the background image is checked
        elif self.parent.bg_handler.img_checkbox.instate(["selected"]):
            # If the background image is checked but not loaded in
            if self.parent.bg_handler.background is None:
                message = "No image background was loaded. The figure will be generated on a blank background. Please select an image as your background next time."
                tk.messagebox.showwarning("No background loaded", message)
                # Recomputing everything only if there is a change in resolution
                if self.resolution != self.previous_resolution:
                    figure = create_image(network, layers_to_print, self.resolution, None, False)
                    self.previous_resolution = self.resolution                    
                else:
                    figure = create_image_from_lines(network.get_lines(), layers_to_print, self.resolution, None, network, False)
                    print("don't recompute everything")
                    
            # If the background image is checked and loaded in
            else:
                self.previous_resolution = self.resolution
                self.resolution = [self.parent.bg_handler.background.shape[1], self.parent.bg_handler.background.shape[0]]
                # Recomputing everything only if there is a change in resolution
                if self.resolution != self.previous_resolution:
                    figure = create_image(network, layers_to_print, self.resolution, self.parent.bg_handler.background, False)
                    self.previous_resolution = self.resolution                    
                else:
                    figure = create_image_from_lines(network.get_lines(), layers_to_print, self.resolution, self.parent.bg_handler.background, network, False)

        # If the background is blank
        else:
            self.resolution = settings.RESOLUTION
            # Recomputing everything only if there is a change in resolution
            if self.resolution != self.previous_resolution:
                figure = create_image(network, layers_to_print, self.resolution, None, False)
                self.previous_resolution = self.resolution
            else:
                figure = create_image_from_lines(network.get_lines(), layers_to_print, self.resolution, None, network, False)

        self.image = figure;
        ax = self.f.add_subplot(1, 1, 1)
        ax.imshow(figure, cmap = "gray", interpolation = "nearest", origin = "upper")
        ax.axes.set_aspect('equal')
        self.canvas.draw()

        self.parent.update_refreshing_label(False)


    def reset_figure(self):
        self.f = settings.FIGURE
