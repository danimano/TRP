import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class MenuInterface(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        self.menu_bar = tk.Menu(parent)
        self.file_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "Open file", command = lambda:self.open_file(parent, controller), accelerator = "Ctrl + O")
        self.file_menu.add_command(label = "Save figure", command = lambda:self.save_figure(parent), state = "disabled", accelerator = "Ctrl + S")
        self.file_menu.add_command(label = "Close file", command = lambda:self.close_file(parent, controller), state = "disabled", accelerator = "Ctrl + W")
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = lambda:self.quit(parent), accelerator = "Ctrl + Q")
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

        self.figure_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.figure_menu.add_command(label = "Refresh the figure", command = controller.refresh_figure, state = "disabled", accelerator = "Ctrl + R")
        self.figure_menu.add_command(label = "Set the view to \"Automatic\"", command = lambda:controller.popupmsg("Not supported yet!"), state = "disabled")
        self.figure_menu.add_command(label = "Reset the view to default", command =lambda:self.reset_default_view(parent), state = "disabled")
        self.menu_bar.add_cascade(label = "Figure", menu = self.figure_menu)

        self.about_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.about_menu.add_command(label = "Stuff", command = lambda:controller.popupmsg("Stuff"))
        self.about_menu.add_command(label = "Doc", command = lambda:controller.popupmsg("Documentation!"))
        self.menu_bar.add_cascade(label = "About", menu = self.about_menu)

        tk.Tk.config(parent, menu = self.menu_bar)
        

    # Quits the program
    def quit(self, parent):
        print("Exiting the program!")
        parent.destroy()

    # Opens a file
    def open_file(self, parent, controller):
        print("Opening file!")
        filename = tk.filedialog.askopenfilename(filetypes=[("Python",".py")])
        if filename:
            filename = filename.split("/")[-1]
            self.file_menu.entryconfig("Save figure", state = "normal")
            self.file_menu.entryconfig("Close file", state = "normal")
            self.figure_menu.entryconfig("Refresh the figure", state = "normal")
            self.figure_menu.entryconfig("Set the view to \"Automatic\"", state = "normal")
            self.figure_menu.entryconfig("Reset the view to default", state = "normal")
            parent.active.refresh.config(state = "normal")
            settings.OPENED = True

            controller.refresh_filename("Visualizing " + filename)
            controller.refresh_figure()

    # Saves the currently displayed figure
    def save_figure(self, parent):
        if settings.OPENED:
            print("Saving file!")
            parent.active.plot_figure.toolbar.save_figure()
        

    # Closes an opened file
    def close_file(self, parent, controller):
        # Only works if a file is opened (useless to refresh the canvas & co if no file is opened)
        if settings.OPENED: 
            print("Closing file!")
            self.file_menu.entryconfig("Save figure", state = "disabled")
            self.file_menu.entryconfig("Close file", state = "disabled")
            self.figure_menu.entryconfig("Refresh the figure", state = "disabled")
            self.figure_menu.entryconfig("Set the view to \"Automatic\"", state = "disabled")
            self.figure_menu.entryconfig("Reset the view to default", state = "disabled")
            parent.active.refresh.config(state = "disabled")
            settings.OPENED = False
            parent.active.f = settings.FIGURE
            
            controller.refresh_filename(settings.FILENAME)
            controller.refresh_figure()

    def reset_default_view(self, parent):
        print("Resetting the view to the original!")
        parent.active.plot_figure.toolbar.home()

            
            
            
