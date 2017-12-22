import settings
import main_page as mp
import interface as it

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure


class PearGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        settings.init()

        # Defining the title of the window, the size and the icon 
        tk.Tk.title(self, "Pear")
        tk.Tk.minsize(self, width = 800, height = 600)
        tk.Tk.iconbitmap(self, default = settings.ICON)
        tk.Tk.columnconfigure(self, 0, weight = 1)
        tk.Tk.rowconfigure(self, 0, weight = 1)

        # Creating the container of the window
        container = tk.Frame(self)
        container.grid(row = 0, column = 0, stick = "nsew")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Main menu
        self.menu_bar = it.MenuInterface(self, self)

        # Page handler (to handle different pages if required)
        self.active = None
        self.frames = {}
        frames = list([mp.MainPage])
       
        # Handles the case where there is only one frame 
        if len(frames) == 1:
            frame = frames[0](container, self)
            self.frames[frames[0]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        else:
            for fr in frames:
                frame = fr(container, self)
                self.frames[fr] = frame
                frame.grid(row = 0, column = 0, sticky = "nsew")
            
        self.show_frame(mp.MainPage)

        self.bind_all_actions()

        
    # Puts the frame we want to show on the top of the stack
    def show_frame(self, cont):
        frame = self.frames[cont]
        self.active = frame
        frame.tkraise()

    
    
    def popupmsg(self, message):
        popup = tk.Tk()
        def leavemini():
            popup.destroy()            
        popup.wm_title("Popup!")
        label = ttk.Label(popup, text = message, font = settings.FONT)
        label.grid()
        b1 = ttk.Button(popup, text = "Ok!", command = leavemini)
        b1.grid()
        popup.mainloop()

    # When a file is opened or closed, refresh the label displaying  its name
    def refresh_filename(self, filename):
        print("Refreshing the filename!")
        self.active.filename.config(text = filename)

    # When a figure is opened or closed, refresh the figure canvas
    def refresh_figure(self):
        print("Refreshing figure!")
        self.active.f.clear()
        if self.active.bg_checkbox.instate(["selected"]):
            print("Use approximated image as background!")
        else:
            print("Plain background!")
        if settings.OPENED:
            a = self.active.f.add_subplot(111)
            a.plot([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1])
        self.active.f.tight_layout()
        self.active.plot_figure.refresh(self.active, self.active.f)

        

    # Refresh the listboxes containing the layers (when opening, filling them; when closing, emptying them)
    def refresh_layers(self):
        print("Refreshing the layers' listboxes!")

    # Binds the important menu commands to keyboard shortcuts
    def bind_all_actions(self):
        def open_file_shortcut(event):
            return self.menu_bar.open_file(self, self)

        def close_file_shortcut(event):
            return self.menu_bar.close_file(self, self)

        def quit_shortcut(event):
            return self.menu_bar.quit(self)

        def save_figure_shortcut(event):
            return self.menu_bar.save_figure(self)

        def refresh_figure_shortcut(event):
            return self.refresh_figure(self)

        self.bind("<Control-Key-o>", open_file_shortcut)
        self.bind("<Control-Key-w>", close_file_shortcut)
        self.bind("<Control-Key-q>", quit_shortcut)
        self.bind("<Control-Key-s>", save_figure_shortcut)
        self.bind("<Control-Key-r>", refresh_figure_shortcut)
