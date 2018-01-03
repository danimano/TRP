import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image
from PIL import ImageTk

class BackgroundHandler(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.background = None

        # Checkbox to determine whether to use the background approximation as the background
        self.bg_checkbox = ttk.Checkbutton(self, text = "Use the approximated image as background", command = self.change_status_approximation)
        self.bg_checkbox.state(["!alternate"])
        self.bg_checkbox.grid(row = 0, column = 0, columnspan = 2, pady = 3, sticky = "w")

        # Help button for approximated background
        self.bg_help = ttk.Button(self, text = "", command = self.help_approximation)
        bg_help_icon = ImageTk.PhotoImage(file = settings.INFO)
        self.bg_help.config(image = bg_help_icon)
        self.bg_help.icon = bg_help_icon
        self.bg_help.grid(row = 0, column = 2, pady = 3, sticky = "w")        

        # Checkbox to determine whether to use an image as the background
        self.img_checkbox = ttk.Checkbutton(self, text = "Use a chosen image as background  ", command = self.change_status_image)
        self.img_checkbox.state(["!alternate"])
        self.img_checkbox.grid(row = 1, column = 0, pady = 5, padx = 0, sticky = "w")

        # Help button for given image background
        self.img_help = ttk.Button(self, text = "", command = self.help_image)
        img_help_icon = ImageTk.PhotoImage(file = settings.INFO)
        self.img_help.config(image = img_help_icon)
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
        if self.img_checkbox.instate(["selected"]):
            self.img_checkbox.state(["!selected"])
            self.browse_button.grid_remove()
            self.loaded_file.grid_remove()
            
            
    def change_status_image(self):
        if self.bg_checkbox.instate(["selected"]):
            self.bg_checkbox.state(["!selected"])

        if self.img_checkbox.instate(["selected"]):
            self.browse_button.grid()
            self.loaded_file.grid()

        else:
            self.browse_button.grid_remove()
            self.loaded_file.grid_remove()
            self.loaded_file.config(text = settings.BACKGROUND)
            if self.background != None:
                self.background.close()
            self.background = None


    def load_image(self):        
        filename = tk.filedialog.askopenfilename(filetypes=[("JPG, PNG, TIFF, BMP", (".jpg", ".jpeg", ".png", ".tiff", ".bmp")), ("JPG",".jpg"), ("PNG", ".png"), ("JPEG", ".jpeg"), ("TIFF", ".tiff"), ("BMP", ".bmp")])
        if filename:
            self.background = Image.open(filename)
            self.loaded_file.config(text = filename.split("/")[-1])

    def help_approximation(self):
        description = "When this option is checked, the decision boundaries of the chosen layers to be displayed will be displayed on the image that the network is approximating at the state of the latest layer to show rather than on a blank background."
        tk.messagebox.showinfo("Details", description)

    def help_image(self):
        description = "When this option is checked, the decision boundaries of the chosen layers to be displayed will be displayed on a given image rather than on a blank background. To do so, you will need to load an image from your disk using the \"Browse image\" button that appears when this option is checked."
        tk.messagebox.showinfo("Details", description)

    
