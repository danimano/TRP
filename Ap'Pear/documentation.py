import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import webbrowser

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
        tk.Tk.minsize(self, width = 400, height = 600)
        self.resizable(0, 0)
        self.geometry('{}x{}'.format(700, 770))

        frame = tk.Canvas(self)
        frame.pack()

        title = tk.Label(frame, text = "AP'PEAR", font = ("Helvetica", 14, "bold"))
        title.pack()

        guidelines = open("./guidelines.txt")
        guide = tk.Message(frame, width = 700, text = guidelines.read(), font = ("Helvetica", 10))
        guide.pack(padx = 5)

        faq = tk.Label(frame, text = "Frequently Asked Questions", font = ("Helvetica", 12, "bold"))
        faq.pack(pady = [10, 0])

        doc = open("./documentation.txt")
        faq_answer = tk.Message(frame, width = 690, text = doc.read(), font = ("Helvetica", 10))
        faq_answer.pack(padx = 5, pady = 5)
        
        
