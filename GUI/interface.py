import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from pear.reader import read_tensorflow_file
from pear.network import Network

from about_pear import AboutPear

class MenuInterface(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        self.parent = parent
        
        self.menu_bar = tk.Menu(parent)
        self.file_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "Open file", command = self.open_file, accelerator = "Ctrl + O")
        self.file_menu.add_command(label = "Save figure", command = self.save_figure, state = "disabled", accelerator = "Ctrl + S")
        self.file_menu.add_command(label = "Close file", command = self.close_file, state = "disabled", accelerator = "Ctrl + W")
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.quit, accelerator = "Ctrl + Q")
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

        self.figure_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.figure_menu.add_command(label = "Refresh the figure", command = self.parent.active.refresh_figure, state = "disabled", accelerator = "Ctrl + R")
        self.figure_menu.add_command(label = "Set the view to \"Automatic\"", command = lambda:print("Not supported yet!"), state = "disabled")
        self.figure_menu.add_command(label = "Reset the view to default", command =lambda:self.reset_default_view(parent), state = "disabled")
        self.menu_bar.add_cascade(label = "Figure", menu = self.figure_menu)

        self.help_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.help_menu.add_command(label = "About Pear", command = self.about)
        self.help_menu.add_separator()
        self.help_menu.add_command(label = "Pear Help", command = self.documentation)
        self.menu_bar.add_cascade(label = "Help", menu = self.help_menu)

        tk.Tk.config(parent, menu = self.menu_bar)
        

    # Quits the program
    def quit(self):
        print("Exiting the program!")
        self.parent.destroy()

    # Opens a file
    def open_file(self):
        print("Opening file!")
        filename = tk.filedialog.askopenfilename(filetypes=[("META",".meta")])
        if filename:
            # Activating all the menu options 
            self.file_menu.entryconfig("Save figure", state = "normal")
            self.file_menu.entryconfig("Close file", state = "normal")
            self.figure_menu.entryconfig("Refresh the figure", state = "normal")
            self.figure_menu.entryconfig("Set the view to \"Automatic\"", state = "normal")
            self.figure_menu.entryconfig("Reset the view to default", state = "normal")
            self.parent.active.activate_refresh()
                    
            # Extracting the neural network's parameters from the file and creating the Layer objects out of them
            def parse_filename(filename):
                filename_split = filename.split(".")
                filename_path = ""
                for i in range(0, len(filename_split) - 1):
                    filename_path += filename_split[i]
                    if i < len(filename_split) - 2:
                        filename_path += "."
                return filename_path

            filename_path = parse_filename(filename)
            print("Loading the neural network's parameters from the TensorFlow file...")
            self.parent.network = Network(filename_path)
            
            settings.OPENED = True

            # Displaying the filename without the whole path nor its extension
            self.parent.active.refresh_filename("Visualizing \"" + self.parent.network.get_filename().split("/")[-1] + "\"")
            self.parent.active.layer_lists.refresh_layers(self.parent.network)
            self.parent.active.refresh_figure()
            

    # Saves the currently displayed figure
    def save_figure(self):
        if settings.OPENED:
            print("Saving file!")
            self.parent.active.plot_figure.toolbar.save_figure()
        

    # Closes an opened file
    def close_file(self):
        # Only works if a file is opened (useless to refresh the canvas & co if no file is opened)
        if settings.OPENED:
            print("Closing file!")
            self.parent.network = None
            
            self.file_menu.entryconfig("Save figure", state = "disabled")
            self.file_menu.entryconfig("Close file", state = "disabled")
            self.figure_menu.entryconfig("Refresh the figure", state = "disabled")
            self.figure_menu.entryconfig("Set the view to \"Automatic\"", state = "disabled")
            self.figure_menu.entryconfig("Reset the view to default", state = "disabled")
            self.parent.active.deactivate_refresh()
            settings.OPENED = False
            self.parent.active.f = settings.FIGURE
            
            self.parent.active.refresh_filename(settings.FILENAME)
            self.parent.active.layer_lists.refresh_layers(self.parent.network)
            self.parent.active.refresh_figure()

    def reset_default_view(self, parent):
        print("Resetting the view to the original!")
        parent.active.plot_figure.toolbar.home()


    def documentation(self):
        documentation = tk.Tk()
        def close():
            documentation.destroy()            
        documentation.wm_title("Documentation")
        message = "The documentation will be written here"
        label = ttk.Label(documentation, text = message)
        label.grid()
        b1 = ttk.Button(documentation, text = "Ok!", command = close)
        b1.grid()
        documentation.mainloop()

    def about(self):
        about = tk.Tk()
        def close():
            about.destroy()            
        about.wm_title("About Pear v1.0")
        message = "The documentation will be written here"
        label = ttk.Label(about, text = message)
        label.grid()
        b1 = ttk.Button(about, text = "Ok!", command = close)
        b1.grid()
        about.mainloop()            
