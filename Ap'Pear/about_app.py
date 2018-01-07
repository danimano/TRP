import settings

import tkinter as tk
from tkinter import ttk

class AboutApp(tk.Toplevel):
    """
    The AboutApp object is a top-level frame that contains an information box about the Ap'Pear GUI is about.
    Its attributes are:
        - parent: the frame over which we are raising the top-level frame.
        - initial_focus: the element on which the program focus should be.
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Initialize the AboutApp object by raising a top-level frame.
        """
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.transient(parent)
        self.parent = parent

        # Defining the title of the window and its size
        tk.Toplevel.title(self, "About Ap'Pear v1.0")
        tk.Toplevel.resizable(self, width = False, height = False)

        # Defining the main body of the top-level
        body = tk.Frame(self, bd = 2, relief = "ridge")
        self.initial_focus = self.body(body)
        body.pack(padx = 5, pady = 5)

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.initial_focus.focus_set()
        self.wait_window(self)

    def body(self, master):
        """
        Create the box containing the whole content of the "About Ap'Pear" window.
        """
        info_message = "A Python graphical user interface for the Python library Pear"
        info = tk.Message(master, text = info_message, font = ("Helvetica", 12, "bold"), width = 150)
        info.pack()

        guidelines = open("./guidelines.txt", "r")
        guide = tk.Message(master, text = guidelines.read())
        guide.pack()

        pass

    def buttonbox(self):
        """
        Create the box containing the close button.
        """
        box = tk.Frame(self)
        close = ttk.Button(box, text = "Close", width = 10, command = self.close, default = "active")
        close.pack(padx = 5, pady = 5)
        self.bind("<Return>", self.close)
        box.pack()

    def close(self, event = None):
        """
        Close the top-level window.
        """
        self.parent.focus_set()
        self.destroy()
        
    
