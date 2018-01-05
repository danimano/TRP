import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PIL import ImageTk
import matplotlib.pyplot as plt
import numpy as np

class BackgroundHandler(tk.Frame):
    """
    The BackgroundHandler object is used to handle the user's choices regarding the background of the figure (blank, approximated image, given image).
    Its attributes are:
        - parent: the parent of the BackgroundHandler object, which allows to access the parent's objects' functions.
        - background: the image used as the background of the figure.
        - bg_checkbox: the checkbox containing the user's decision to use or not the approximated image as the background.
        - bg_help: the help button that displays information about what it means to use the approximated image as a background.
        - img_checkbox: the checkbox containing the user's decision to use or not a given image as the background.
        - img_help: the help button that displays information about what it means to use a given image as the background.
        - browse_button: the button that allows the user to choose an image to load in in order to use it as the background.
        - loaded_file: a label indicating if a file is being loaded in as the background and if so, which one.
    """
    
    def __init__(self, parent, controller, *args, **kwargs):
        """
        Initialize the BackgroundHandler object.
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.background = None

        # Checkbox to determine whether to use the background approximation as the background
        self.bg_checkbox = ttk.Checkbutton(self, text = "Use the approximated image as background", command = self.change_status_approximation)
        self.bg_checkbox.state(["!alternate"])
        self.bg_checkbox.grid(row = 0, column = 0, columnspan = 2, pady = 3, sticky = "w")

        # Help button for approximated background
        self.bg_help = tk.Button(self, text = "Information", command = self.help_approximation)
        bg_help_icon = ImageTk.PhotoImage(file = settings.INFO)
        self.bg_help.config(image = bg_help_icon, relief = "flat")
        self.bg_help.icon = bg_help_icon
        self.bg_help.grid(row = 0, column = 2, pady = 3, sticky = "w")        

        # Checkbox to determine whether to use an image as the background
        self.img_checkbox = ttk.Checkbutton(self, text = "Use a chosen image as background  ", command = self.change_status_image)
        self.img_checkbox.state(["!alternate"])
        self.img_checkbox.grid(row = 1, column = 0, pady = 5, padx = 0, sticky = "w")

        # Help button for given image background
        self.img_help = tk.Button(self, text = "Information", command = self.help_image)
        img_help_icon = ImageTk.PhotoImage(file = settings.INFO)
        self.img_help.config(image = img_help_icon, relief = "flat")
        self.img_help.icon = img_help_icon
        self.img_help.grid(row = 1, column = 0, pady = 3, padx = 0, sticky = "e")
        
        # Button to browse the file
        self.browse_button = ttk.Button(self, text = "Browse image", command = self.load_image)
        self.browse_button.grid(row = 1, column = 2, pady = 3, sticky = "w")
        self.browse_button.grid_remove()

        # Label with the currently loaded file
        self.loaded_file = ttk.Label(self, text = settings.BACKGROUND)
        self.loaded_file.grid(row = 1, column = 3, pady = 3, padx = 5)
        self.loaded_file.grid_remove()


    def change_status_approximation(self):
        """
        When checking the "use the approximated image as background" checkbox, uncheck the "use an image as the background" checkbox.
        If an image was loaded in, delete it.
        """
        if self.img_checkbox.instate(["selected"]):
            self.img_checkbox.state(["!selected"])
            self.loaded_file.config(text = settings.BACKGROUND)
            if self.background is not None:
                self.background = None
            self.browse_button.grid_remove()
            self.loaded_file.grid_remove()
            
            
    def change_status_image(self):
        """
        When checking the "use an image as the background" checkbox, uncheck the "use the approximated image as the background" checkbox.
        If unchecking the "use an image as the background" checkbox while an image is loaded in, delete the image.
        """
        if self.bg_checkbox.instate(["selected"]):
            self.bg_checkbox.state(["!selected"])

        if self.img_checkbox.instate(["selected"]):
            self.browse_button.grid()
            self.loaded_file.grid()

        else:
            self.browse_button.grid_remove()
            self.loaded_file.grid_remove()
            self.loaded_file.config(text = settings.BACKGROUND)
            if self.background is not None:
                self.background = None


    def load_image(self):
        """
        Load an image chosen by the user in.
        """
        filename = tk.filedialog.askopenfilename(filetypes=[("JPG, PNG, TIFF, BMP", (".jpg", ".jpeg", ".png", ".tiff", ".bmp")), ("JPG",".jpg"), ("PNG", ".png"), ("JPEG", ".jpeg"), ("TIFF", ".tiff"), ("BMP", ".bmp")])
        if filename:
            self.background = plt.imread(filename)
            if np.amax(self.background) > 1:
                self.background = self.background / 255

            self.loaded_file.config(text = filename.split("/")[-1])


    def help_approximation(self):
        """
        Display the information box about using the approximated image as the background.
        """
        description = "When this option is checked, the decision boundaries of the chosen layers to be displayed will be displayed on the image that the network is approximating at the state of the latest layer to show rather than on a blank background."
        tk.messagebox.showinfo("Details", description)


    def help_image(self):
        """
        Display the information box about using a given image as the background.
        """
        description = "When this option is checked, the decision boundaries of the chosen layers to be displayed will be displayed on a given image rather than on a blank background. To do so, you will need to load an image from your disk using the \"Browse image\" button that appears when this option is checked."
        tk.messagebox.showinfo("Details", description)

    
