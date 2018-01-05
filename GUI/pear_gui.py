import settings
import main_page as mp
import interface as it
import toolbar as tb

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure

from pearlib.layer import Layer
from pearlib.get_color_for_layeridx import get_color_for_layeridx


class PearGUI(tk.Tk):
    """
    The PearGUI object contains the whole wrapping frame for the graphical interface of the Pear library.
    Its attributes are:
        - network: the opened network.
        - active: the page that is currently being shown to the user.
        - frames: the list of pages that can be shown to the user.
        - menu_bar: the menu bar containing the commands that can be executed by the user.
        - toolbar: the toolbar, containing the buttons for the most useful menu commands.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the PearGUI object.
        Create a main container in which the pages will be displayed.
        """
        tk.Tk.__init__(self, *args, **kwargs)
        settings.init()
        # Will contain the network information once opened
        self.network = None

        # Defining the title of the window, the size and the icon 
        tk.Tk.title(self, "Ap'Pear")
        tk.Tk.minsize(self, width = 800, height = 700)
        tk.Tk.iconbitmap(self, default = settings.ICON)
        tk.Tk.columnconfigure(self, 0, weight = 1)
        tk.Tk.rowconfigure(self, 0, weight = 1)
        tk.Tk.rowconfigure(self, 1, weight = 19)

        # Creating the container of the window
        container = tk.Frame(self)
        container.grid(row = 1, column = 0, sticky = "nsew", pady = 0)
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
        self.toolbar = tb.Toolbar(self)
        self.toolbar.grid(row = 0, column = 0, sticky = "new", ipady = 5)

        self.bind_all_actions()

        
    def show_frame(self, content):
        """
        Put the page we want to show the user on the top of the stack.
        """
        frame = self.frames[content]
        self.active = frame
        frame.tkraise()


    def get_network(self):
        """
        Get the network structure.
        """
        return self.network
        

    def bind_all_actions(self):
        """
        Bind the important menu commands to keyboard shortcuts.
        """
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
        self.bind("<Control-S>", save_figure_shortcut)
        self.bind("<Control-r>", refresh_figure_shortcut)
