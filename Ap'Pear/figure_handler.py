import settings

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt

import numpy as np

from pearlib.create_image import create_image
from pearlib.create_image_from_lines import create_image_from_lines

class FigureHandler(tk.Frame):
    """
    The FigureHandler class contains the widgets and information regarding the Matplotlib canvas of the GUI.
    It contains the canvas itself, the toolbar, and the content of the canvas.
    Its goal is to update the figure depending on the user's requests.
    Its attributes are:
        - parent: the parent container of the FigureHandler object, useful to access the parent's other objects' functions.
        - resolution: the resolution used to compute the figure.
        - previous_resolution: the resolution that was used the last time the figure was refreshed, to know if recomputing everything is necessary or not.
        - image: the computed image containing the requested layers' decisions boundaries and optionally a background.
        - canvas: the Matplotlib canvas in which the figure is drawn.
        - toolbar: the Matplotlib toolbar which is used for zooming and doing translations.
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Initialize the FigureHandler object without any other argument than the widget's parent (the main window).
        """
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


    def refresh_figure(self, network):
        """
        Refresh the figure with the given network, the requested layers and the given options (approximated image background, image background, blank background).
        """
        self.parent.update_refreshing_label(True) # Displays the label showing that the computations are being done
        self.f.clear()
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
                
                if self.resolution != self.previous_resolution:
                    figure = create_image(network, layers_to_print, self.resolution, None, False)
                    self.previous_resolution = self.resolution                    
                else:
                    figure = create_image_from_lines(network.get_lines(), layers_to_print, self.resolution, None, network, False)
                    
            # If the background image is checked and loaded in
            else:
                bkg = np.array(self.parent.bg_handler.background) # Copy to avoid writing on the image
                self.previous_resolution = self.resolution
                self.resolution = [bkg.shape[1], bkg.shape[0]]
                
                if self.resolution != self.previous_resolution:
                    figure = create_image(network, layers_to_print, self.resolution, bkg, False)
                    self.previous_resolution = self.resolution                    
                else:
                    figure = create_image_from_lines(network.get_lines(), layers_to_print, self.resolution, bkg, network, False)

        # If the background is blank
        else:
            self.resolution = settings.RESOLUTION            
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
        """
        Reset the figure to an empty one.
        """
        self.f.clear()
        self.f = settings.FIGURE


    def reset_resolution(self):
        """
        Reset the resolution and previous_resolution attributes to their default settings.
        """
        self.resolution = settings.RESOLUTION
        self.previous_resolution = None
        

    def reset_image(self):
        """
        Reset the image.
        """
        self.image = None
