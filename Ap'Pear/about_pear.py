import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import webbrowser

class AboutPear(tk.Toplevel):
    """
    The AboutPear object is a top-level frame that contains an information box about what the Pear library is about.
    Its attributes are:
        - parent: the frame over which we are raising the top-level frame.
        - initial_focus: the element on which the program focus should be.
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Initialize the AboutPear object by raising a top-level frame.
        """
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.transient(parent)
        self.parent = parent                

        # Defining the title of the window and its size
        tk.Toplevel.title(self, "About Pear v1.0")
        tk.Toplevel.resizable(self, width = False, height = False)
        self.geometry('{}x{}'.format(237, 400))

        # Defining the main body of the top-level
        body = tk.Frame(self, bd = 2, relief = "ridge", width = 270)
        self.initial_focus = self.body(body)
        body.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.initial_focus.focus_set()
        self.wait_window(self)
        

    def body(self, master):
        """
        Create the box containing the whole content of the "About Pear" window.
        """        
        logo_img = ImageTk.PhotoImage(file = settings.LOGO)
        logo = tk.Label(master, text = "", image = logo_img, compound = "center")
        logo.image = logo_img
        logo.grid(row = 0, column = 0)

        
        info_message = "A Python library to visualize neural networks built with TensorFlow" 
        info = tk.Message(master, text = info_message, width = 210)
        info.grid(row = 1, column = 0, padx = 3, pady = 6, sticky = "w")

        authors = tk.Message(master, text = "Written by Candice Bentéjac, Anna Csörgő and Dániel Hajtó", width = 210)
        authors.grid(row = 2, column = 0, padx = 3, pady = [0, 6], sticky = "w")

        python_version = tk.Message(master, text = "Python version: 3.6.4", width = 200)
        python_version.grid(row = 3, column = 0, padx = 3, sticky = "w")

        tk_version = tk.Message(master, text = "Tk version: 8.6.6", width = 200)
        tk_version.grid(row = 4, column = 0, padx = 3, sticky = "w")

        download = ttk.Button(master, text = "Download Pear", command = lambda:openweb(settings.URL))
        download.grid(row = 5, column = 0, pady = 10)

        pass


    def buttonbox(self):
        """
        Create the box containing the close button.
        """
        box = tk.Frame(self)
        close = ttk.Button(box, text = "Close", width = 10, command = self.close, default = "active")
        close.pack(side = "left", padx = 5, pady = 5)
        self.bind("<Return>", self.close)
        box.grid(row = 1, column = 0, sticky = "s")
        

    def close(self, event = None):
        """
        Close the top-level window.
        """
        self.parent.focus_set()
        self.destroy()

def openweb(url):
    webbrowser.open(url, new = 1)
        
