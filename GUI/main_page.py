import settings

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from PIL import ImageTk


# Main page class: contains our application
class MainPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Defining which columns and rows will expand when the window will be resized
        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 0)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
              
        # Name of the currently opened file
        filename = ttk.Label(self, text = "Filename", font = settings.FONT)
        filename.grid(row = 0, column = 0, columnspan = 3, pady = 10)

        # Checkbox to determine whether to use the background approximation as the background
        self.bg_checkbox = ttk.Checkbutton(self, text = "Use the approximated image as background")
        self.bg_checkbox.state(['!alternate'])
        self.bg_checkbox.grid(row = 1, column = 0, pady = 3)

        

        # Frame with listboxes to choose which layers to display
        layer_lists = LayerHandler(self, controller)
        layer_lists.grid(row = 2, column = 0, sticky = "n", pady = 15)

        # Getting the Matplotlib figure to display
        f = Figure(figsize = (5, 5), dpi = 100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1])

        # Creating a specific frame to put the Matplotlib widget and the toolbar in
        plot_fr = FigureHandler(self, controller, f)
        plot_fr.grid(row = 2, column = 1, sticky = "nsew", padx = 10, rowspan = 3)

        



class LayerHandler(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Displaying the list of all the available layers to draw
        hidden_layers = tk.Listbox(self, selectmode = "extended")
        hidden_layers.grid(row = 1, column = 0, sticky = "n", padx = 10, ipady = 30)
        
        # Filling the list (so far, hardcoded values)
        for item in ["Layer 1", "Layer 2", "Layer 3", "Layer 4", "Layer 5", "Layer 6", "Layer 7", "Layer 8", "Layer 9", "Layer 10", "Layer 11", "Layer 12", "Layer 13", "Layer 14", "Layer 15", "Layer 16", "Layer 17", "Layer 18", "Layer 19", "Layer 20", "Layer 21"]:
            hidden_layers.insert("end", item)

        more_layer = ttk.Button(self, text = "Add layer", command = lambda:self.change_layer(hidden_layers, shown_layers))
        add_icon = ImageTk.PhotoImage(file = settings.ADD)
        more_layer.config(image = add_icon, compound="right")
        more_layer.icon = add_icon
        more_layer.grid(row = 0, column = 0)

        # Displaying the list of all the drawn layers
        shown_layers = tk.Listbox(self, selectmode = "extended")
        shown_layers.grid(row = 1, column = 1, sticky = "n", padx = 10, ipady = 30)

        rm_layer = ttk.Button(self, text = "Remove layer", command = lambda:self.change_layer(shown_layers, hidden_layers))
        remove_icon = ImageTk.PhotoImage(file = settings.REMOVE)
        rm_layer.config(image = remove_icon, compound = "right")
        rm_layer.icon = remove_icon
        rm_layer.grid(row = 0, column = 1)

    # Adds or removes one or several layers from the displayed figure
    def change_layer(self, listbox_from, listbox_to):
        # Gets the selected layers and removes them from the list they are taken from
        current = listbox_from.curselection()
        for item in current:
            listbox_to.insert("end", listbox_from.get(item))
        for item in current:
            listbox_from.delete(item)

        # Sorts the items from the modified list to have ordered layers
        l = list()
        for i in range(0, listbox_to.size()):
           l.append(listbox_to.get(i)) 
        listbox_to.delete(0, "end")
        l.sort()
        l.sort(key=lambda item: (len(item), item))

        # Inserts the ordered layers in the list they are going to
        for item in l:
            listbox_to.insert("end", item)

        listbox_from.selection_clear(0, "end")
        # Here, should update the figure




class FigureHandler(tk.Frame, Figure):

    def __init__(self, parent, controller, f):
        tk.Frame.__init__(self, parent)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        canvas = FigureCanvasTkAgg(f, master = self)
        canvas.show()
        canvas.get_tk_widget().pack(side = "top", fill = "both", expand =True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(anchor = "center")
