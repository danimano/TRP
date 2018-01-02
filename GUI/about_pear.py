import settings

import tkinter as tk
from tkinter import ttk

class AboutPear(tk.Toplevel):

    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.transient(parent)
        self.parent = parent
                
        settings.init()

        # Defining the title of the window and its size
        tk.Toplevel.title(self, "About Pear v1.0")
        tk.Toplevel.resizable(self, width = False, height = False)
        self.geometry('{}x{}'.format(270, 400))

        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx = 5, pady = 5)

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.initial_focus.focus_set()
        self.wait_window(self)

    def body(self, master):
        pass

    def buttonbox(self):
        box = tk.Frame(self)
        w = ttk.Button(box, text = "Close", width = 10, command = self.close, default = "active")
        w.pack(side = "left", padx = 5, pady = 5)

        self.bind("<Return>", self.close)

        box.pack()

    def close(self, event = None):
        self.parent.focus_set()
        self.destroy()

if __name__ == "__main__":  
    app = AboutPear(None)
    app.mainloop()
