import settings

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from pear.network import Network
from pear.save_image import save_image

from about_pear import AboutPear

class MenuInterface(tk.Frame):
    """
    The MenuInterface object contains the GUI's menu.
    Its attributes are:
        - parent: the menu's parent, used to access the parent's other objects' functions.
        - menu_bar: the literal menu bar.
        - file_menu: the "File" menu, tied to the menu bar.
        - figure_menu: the "Figure" menu, tied to the menu bar.
        - help_menu: the "Help" menu, tied to the menu bar.
    """

    def __init__(self, parent, controller, *args, **kwargs):
        """
        Initialize the MenuInterface object and sets the commands of each menus tied to the menu bar.
        """
        self.parent = parent
        
        self.menu_bar = tk.Menu(parent)
        self.file_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "Open file", command = self.open_file, accelerator = "Ctrl + O")
        self.file_menu.add_command(label = "Save image", command = self.save_image, state = "disabled", accelerator = "Ctrl + S")
        self.file_menu.add_command(label = "Save figure", command = self.save_figure, state = "disabled", accelerator = "Ctrl + Shift + S") 
        self.file_menu.add_command(label = "Close file", command = self.close_file, state = "disabled", accelerator = "Ctrl + W")
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.quit, accelerator = "Ctrl + Q")
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

        self.figure_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.figure_menu.add_command(label = "Refresh the figure", command = lambda:self.parent.active.plot_figure.refresh_figure(parent.network), state = "disabled", accelerator = "Ctrl + R")
        self.figure_menu.add_command(label = "Reset the view", command =lambda:self.reset_default_view(parent), state = "disabled")
        self.menu_bar.add_cascade(label = "Figure", menu = self.figure_menu)

        self.help_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.help_menu.add_command(label = "About Pear", command = self.about)
        self.help_menu.add_separator()
        self.help_menu.add_command(label = "Pear Help", command = self.documentation)
        self.menu_bar.add_cascade(label = "Help", menu = self.help_menu)

        tk.Tk.config(parent, menu = self.menu_bar)
        

    def quit(self):
        """
        Exit the program.
        """
        self.parent.destroy()

    
    def open_file(self):
        """
        Open a dialog box asking the user to choose a file to open. Only META files can be opened.
        The chosen file's path is parsed to be used as an input to the reader function.
        The network is loaded, and its layers extracted and saved.
        The menu commands that should not be active at all times are activated.
        """
        print("Opening file")        
        filename = tk.filedialog.askopenfilename(filetypes=[("META",".meta")])
        if filename:
            if settings.OPENED:
                self.close_file()
            
            # Activating all the menu options 
            self.file_menu.entryconfig("Save image", state = "normal")
            self.file_menu.entryconfig("Save figure", state = "normal")
            self.file_menu.entryconfig("Close file", state = "normal")
            self.figure_menu.entryconfig("Refresh the figure", state = "normal")
            self.figure_menu.entryconfig("Reset the view", state = "normal")
            self.parent.active.activate_refresh()
            self.parent.toolbar.activate_toolbar()
                    
            
            def parse_filename(filename):
                """
                Withdraw the extension of the open file's full path.
                """
                filename_split = filename.split(".")
                filename_path = ""
                for i in range(0, len(filename_split) - 1):
                    filename_path += filename_split[i]
                    if i < len(filename_split) - 2:
                        filename_path += "."
                return filename_path

            # Extracting the neural network's parameters from the file and creating the Layer objects out of them
            filename_path = parse_filename(filename)
            self.parent.network = Network(filename_path)
            self.parent.active.network = self.parent.get_network()
            print("Opened network!")
            
            settings.OPENED = True

            # Displaying the filename without the whole path nor its extension
            self.parent.active.refresh_filename("Visualizing \"" + self.parent.network.get_filename().split("/")[-1] + "\"")
            self.parent.active.layer_lists.refresh_layers(self.parent.network)
            self.parent.active.layer_lists.get_layers_to_draw()
            self.parent.active.reset_figure(self.parent.get_network())
            

    def save_image(self):
        """
        Save the image currently displayed as a figure.
        The image, unlike the figure, does not have any axis.
        """
        if settings.OPENED:
            print("Saving file!")
            filename = tk.filedialog.asksaveasfilename(filetypes=[('PNG', ".png")])
            if filename:
                save_image(filename, self.parent.active.plot_figure.image)


    def save_figure(self):
        """
        Save the figure containing the currently displayed image.
        The figure, unlike the image, has axis.
        """
        if settings.OPENED:
            self.parent.active.plot_figure.toolbar.save_figure()
        

    def close_file(self):
        """
        Close the currently opened file.
        Clear the network structure.        
        Disable the menu commands that should not be active at all times.
        """
        print("Closing file")
        # Only works if a file is opened
        if settings.OPENED:            
            self.file_menu.entryconfig("Save image", state = "disabled")
            self.file_menu.entryconfig("Save figure", state = "disabled")
            self.file_menu.entryconfig("Close file", state = "disabled")
            self.figure_menu.entryconfig("Refresh the figure", state = "disabled")            
            self.figure_menu.entryconfig("Reset the view", state = "disabled")
            self.parent.active.deactivate_refresh()
            self.parent.toolbar.deactivate_toolbar()
            settings.OPENED = False
            
            self.parent.active.refresh_filename(settings.FILENAME)
            self.parent.active.layer_lists.refresh_layers(self.parent.get_network())
            self.parent.active.reset_figure(self.parent.get_network())
            self.parent.network = None
            self.parent.active.network = None
            
            self.parent.active.plot_figure.reset_resolution()
            self.parent.active.plot_figure.reset_image()
            print(self.parent.active.plot_figure.resolution)
            print(self.parent.active.plot_figure.previous_resolution)


    def reset_default_view(self, parent):
        """
        Reset the view of the network on the figure to its default settings.
        """
        parent.active.plot_figure.toolbar.home()


    def documentation(self):
        """
        Display the documentation.
        """
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
        """
        Display information about the GUI and the library.
        """
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
