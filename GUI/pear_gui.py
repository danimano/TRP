import settings
import main_page as mp
import interface as it

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure

from pear.layer import Layer
from pear.get_color_for_layeridx import get_color_for_layeridx


class PearGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        settings.init()
        # Will contain the network information once opened
        self.network = None

        # Defining the title of the window, the size and the icon 
        tk.Tk.title(self, "Pear")
        tk.Tk.minsize(self, width = 800, height = 700)
        tk.Tk.iconbitmap(self, default = settings.ICON)
        tk.Tk.columnconfigure(self, 0, weight = 1)
        tk.Tk.rowconfigure(self, 0, weight = 1)

        # Creating the container of the window
        container = tk.Frame(self)    
        container.grid(row = 0, column = 0, stick = "nsew")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        container.parent = self # Setting the application as the parent of the main container.

        # Page handler (to handle different pages if required)
        self.active = None
        self.frames = {}
        frames = list([mp.MainPage])
       
        # Handles the case where there is only one frame 
        if len(frames) == 1:
            frame = frames[0](container, self, self.network)
            self.frames[frames[0]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        else:
            for fr in frames:
                frame = fr(container, self)
                self.frames[fr] = frame
                frame.grid(row = 0, column = 0, sticky = "nsew")
            
        self.show_frame(mp.MainPage)

        # Main menu
        self.menu_bar = it.MenuInterface(self, self)

        self.bind_all_actions()

        
    # Puts the frame we want to show on the top of the stack
    def show_frame(self, content):
        frame = self.frames[content]
        self.active = frame
        frame.tkraise()

    def get_network(self):
        return self.network
        

    # Binds the important menu commands to keyboard shortcuts
    def bind_all_actions(self):
        def open_file_shortcut(event):
            return self.menu_bar.open_file()

        def close_file_shortcut(event):
            return self.menu_bar.close_file()

        def quit_shortcut(event):
            return self.menu_bar.quit()

        def save_image_shortcut(event):
            return self.menu_bar.save_image()

        def save_figure_shortcut(event):
            return self.menu_bar.save_figure()

        def refresh_figure_shortcut(event):
            return self.active.plot_figure.refresh_figure(self.get_network())

        self.bind("<Control-o>", open_file_shortcut)
        self.bind("<Control-w>", close_file_shortcut)
        self.bind("<Control-q>", quit_shortcut)
        self.bind("<Control-s>", save_image_shortcut)
        self.bind("<Control-Shift-s>", save_figure_shortcut)
        self.bind("<Control-r>", refresh_figure_shortcut)
