import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

class Documentation(tk.Tk):
    """
    The Documentation object is a frame containing some documentation elements.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Documentation object by creating a new independent frame.
        """
        tk.Tk.__init__(self, *args, **kwargs)
        settings.init()

        tk.Tk.configure(self)
        tk.Tk.title(self, "Ap'Pear Help")
        tk.Tk.iconbitmap(self, default = settings.ICON)

        frame = tk.Frame(self)
        frame.pack()


        faq = tk.Label(frame, text = "Frequently Asked Questions", font = ("Helvetica", 12, "bold"))
        faq.pack()

        doc = open("./documentation.txt")
        faq_answer = tk.Message(frame, text = doc.read(), font = ("Helvetica", 10))
        faq_answer.pack(padx = 5, pady = 5, fill = "both")
        
        
