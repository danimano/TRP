import settings
from main_page import MainPage

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

class VisuGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        settings.init()

        # Defining the title of the window, the size and the icon 
        tk.Tk.title(self, "Wonderful Neural Network Visualization")
        tk.Tk.minsize(self, width = 800, height = 600)
        tk.Tk.iconbitmap(self, default = settings.ICON)
        tk.Tk.columnconfigure(self, 0, weight = 1)
        tk.Tk.rowconfigure(self, 0, weight = 1)

        # Creating the container of the window
        container = tk.Frame(self)
        container.grid(row = 0, column = 0, stick = "nsew")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # MAIN MENU HANDLER
        menu_bar  = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff = 0)
        file_menu.add_command(label = "Open file", command = lambda:self.popupmsg("Not supported yet"))
        file_menu.add_command(label = "Save figure", command = lambda:self.popupmsg("Not supported yet"))
        file_menu.add_command(label = "Close file", command = lambda:self.popupmsg("Not supported yet"))
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.quit)
        menu_bar.add_cascade(label = "File", menu = file_menu)

        about_menu = tk.Menu(menu_bar, tearoff = 0)
        about_menu.add_command(label = "Stuff", command = lambda:self.popupmsg("Stuff"))
        about_menu.add_command(label = "Doc", command = lambda:self.popupmsg("Documentation!"))
        menu_bar.add_cascade(label = "About", menu = about_menu)

        tk.Tk.config(self, menu = menu_bar)

        # PAGE HANDLER (to handle different pages if required)
        frames = list([MainPage])
        self.frames = {}

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
            
        self.show_frame(MainPage)


    # Puts the frame we want to show on the top of the stack
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # Quits the program
    def quit(self):
        self.destroy()

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
   
        

if __name__ == "__main__":
    app = VisuGUI()
    app.mainloop()
