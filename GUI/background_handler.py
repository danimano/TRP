import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

class BackgroundHandler(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.background = None

        # Checkbox to determine whether to use the background approximation as the background
        self.bg_checkbox = ttk.Checkbutton(self, text = "Use the approximated image as background", command = self.change_status_approximation)
        self.bg_checkbox.state(["!alternate"])
        self.bg_checkbox.grid(row = 1, column = 0, pady = 3, sticky = "w")

        # Checkbox to determine whether to use an image as the background
        self.img_checkbox = ttk.Checkbutton(self, text = "Use an image as background", command = self.change_status_image)
        self.img_checkbox.state(["!alternate"])
        self.img_checkbox.grid(row = 2, column = 0, pady = 5, sticky = "w")

        # Button to browse the file
        self.browse_button = ttk.Button(self, text = "Browse image", command = self.load_image)
        self.browse_button.grid(row = 2, column = 1, pady = 3, sticky = "w")
        self.browse_button.grid_remove()

        # Label with the currently loaded file
        self.loaded_file = ttk.Label(self, text = settings.BACKGROUND)
        self.loaded_file.grid(row = 2, column = 2, pady = 3, padx = 5)
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
        filename = tk.filedialog.askopenfilename(filetypes=[("All files", ".*"), ("JPG",".jpg"), ("PNG", ".png"), ("JPEG", ".jpeg"), ("TIFF", ".tiff"), ("BMP", ".bmp")])
        if filename:
            self.background = Image.open(filename)
            self.background.show()
            self.loaded_file.config(text = filename.split("/")[-1])
            
