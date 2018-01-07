import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk


class Toolbar(tk.Frame):
    """
    The Toolbar object contains the buttons that are representing the main menu actions.
    The Toolbar is intended to be displayed just below the menu, above the main page.
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Initializes the Toolbar, its buttons, and loaded their associated icons in.
        The Toolbar attributes are:
            - parent: the parent container of the toolbar.
            - open_file: the button that opens a file.
            - save_image: the button that saves the current image.
            - close_file: the button that closes the current file.
            - exit_app: the button that exits the program.
            - help: the button that displays the help window.
            - doc: the buttons that displays the GUI documentation.
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.open_file = tk.Button(self, text = "Open file", command = self.parent.menu_bar.open_file)
        open_icon = ImageTk.PhotoImage(file = settings.OPEN_ICON)
        self.open_file.config(image = open_icon, relief = "groove")
        self.open_file.icon = open_icon
        self.open_file.pack(side = "left", padx = 2)

        self.save_image = tk.Button(self, text = "Save image", command = self.parent.menu_bar.save_image)
        save_icon = ImageTk.PhotoImage(file = settings.SAVE_ICON)
        self.save_image.config(image = save_icon, relief = "groove", state = "disabled")
        self.save_image.icon = save_icon
        self.save_image.pack(side = "left", padx = 2)

        self.close_file = tk.Button(self, text = "Close file", command = self.parent.menu_bar.close_file)
        close_icon = ImageTk.PhotoImage(file = settings.CLOSE_ICON)
        self.close_file.config(image = close_icon, relief = "groove", state = "disabled")
        self.close_file.icon = close_icon
        self.close_file.pack(side = "left")

        self.exit_app = tk.Button(self, text = "Exit", command = self.parent.menu_bar.quit)
        exit_icon = ImageTk.PhotoImage(file = settings.EXIT_ICON)
        self.exit_app.config(image = exit_icon, relief = "groove")
        self.exit_app.icon = exit_icon
        self.exit_app.pack(side = "left")

        self.help = tk.Button(self, text = "Help", command = self.parent.menu_bar.about)
        help_icon = ImageTk.PhotoImage(file = settings.HELP_ICON)
        self.help.config(image = help_icon, relief = "groove")
        self.help.icon = help_icon
        self.help.pack(side = "left")

        self.doc = tk.Button(self, text = "Documentation", command = self.parent.menu_bar.documentation)
        doc_icon = ImageTk.PhotoImage(file = settings.DOC_ICON)
        self.doc.config(image = doc_icon, relief = "groove")
        self.doc.icon = doc_icon
        self.doc.pack(side = "left")


    def activate_toolbar(self):
        """
        Activate the Toolbar buttons that should not be accessible at all times.
        """
        self.save_image.config(state = "normal")
        self.close_file.config(state = "normal")

    def deactivate_toolbar(self):
        """
        Deactivate the Toolbar buttons that should not be accessible at all times.
        """
        self.save_image.config(state = "disabled")
        self.close_file.config(state = "disabled")
