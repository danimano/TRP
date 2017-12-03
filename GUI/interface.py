import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class MenuInterface(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        self.menu_bar = tk.Menu(parent)
        self.file_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "Open file", command = lambda:self.open_file(controller), accelerator = "Ctrl + O")
        self.file_menu.add_command(label = "Save figure", command = lambda:parent.popupmsg("Not supported yet"), state = "disabled", accelerator = "Ctrl + S")
        self.file_menu.add_command(label = "Close file", command = lambda:self.close_file(controller), state = "disabled", accelerator = "Ctrl + W")
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = lambda:self.quit(parent), accelerator = "Ctrl + Q")
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

        self.about_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.about_menu.add_command(label = "Stuff", command = lambda:parent.popupmsg("Stuff"))
        self.about_menu.add_command(label = "Doc", command = lambda:parent.popupmsg("Documentation!"))
        self.menu_bar.add_cascade(label = "About", menu = self.about_menu)

        tk.Tk.config(parent, menu = self.menu_bar)

    # Quits the program
    def quit(self, parent):
        parent.destroy()

    # Opens a file
    def open_file(self, controller):
        print("Opening file!")
        filename = tk.filedialog.askopenfilename(filetypes=[("Python",".py")])
        if filename:
            filename = filename.split("/")[-1]
            self.file_menu.entryconfig("Save figure", state = "normal")
            self.file_menu.entryconfig("Close file", state = "normal")
            settings.OPENED = True

            controller.refresh_filename("Visualizing " + filename)
            controller.refresh_figure()

    def close_file(self, controller):
        print("Closing file!")
        self.file_menu.entryconfig("Save figure", state = "disabled")
        self.file_menu.entryconfig("Close file", state = "disabled")
        settings.OPENED = False
        
        controller.refresh_filename(settings.FILENAME)
        controller.refresh_figure()
            
            
            
