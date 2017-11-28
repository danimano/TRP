import settings

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


# Main page class: contains our application
class MainPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        filename = tk.Label(self, text = "Filename", font = settings.FONT)
        filename.grid(row = 0, column = 0, columnspan = 3, pady = 15)

        # Displaying the list of all the available layers to draw
        hidden_layers = tk.Listbox(self, selectmode = "extended")
        hidden_layers.grid(row = 2, column = 0, sticky = "n", padx = 10, ipady = 30)
        
        # Filling the list (so far, hardcoded values)
        for item in ["Layer 1", "Layer 2", "Layer 3", "Layer 4", "Layer 5", "Layer 6", "Layer 7", "Layer 1", "Layer 2", "Layer 3", "Layer 4", "Layer 5", "Layer 6", "Layer 7", "Layer 1", "Layer 2", "Layer 3", "Layer 4", "Layer 5", "Layer 6", "Layer 7"]:
            hidden_layers.insert("end", item)

        more_layer = ttk.Button(self, text = "Add layer", command = lambda:self.change_layer(hidden_layers, shown_layers))
        more_layer.grid(row = 1, column = 0)

        # Displaying the list of all the drawn layers
        shown_layers = tk.Listbox(self, selectmode = "extended")
        shown_layers.grid(row = 2, column = 1, sticky = "n", padx = 10, ipady = 30)

        rm_layer = ttk.Button(self, text = "Remove layer", command = lambda:self.change_layer(shown_layers, hidden_layers))
        rm_layer.grid(row = 1, column = 1)


        # Getting the Matplotlib figure to display
        f = Figure(figsize = (5, 5), dpi = 100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1])

        # Creating a specific frame to put the Matplotlib widget and the toolbar in
        # (if out of a specific frame, we cannot use the grid layout because the toolbar is packed
        # in the constructor)
        plot_fr = tk.Frame(self)
        plot_fr.grid(row = 2, column = 2, sticky = "nsew", padx = 10)

        # Adding the Matplotlib canvas to the specific frame
        canvas = FigureCanvasTkAgg(f, master=plot_fr)
        canvas.show()
        canvas.get_tk_widget().pack()
        # Adding the Matplotlib toolbar to the specific frame
        toolbar = NavigationToolbar2TkAgg(canvas, plot_fr)
        toolbar.update()
        canvas._tkcanvas.pack(anchor = "center")


    # Adds or removes one or several layers from the displayed figure
    def change_layer(self, listbox_from, listbox_to):
        # Gets the selected layers and removes them from the list they are taken from
        current = listbox_from.curselection()
        for item in current:
            listbox_to.insert("end", listbox_from.get(item))
            listbox_from.delete(item)

        # Sorts the items from the modified list to have ordered layers
        l = list()
        for i in range(0, listbox_to.size()):
           l.append(listbox_to.get(i)) 
        listbox_to.delete(0, "end")
        l.sort()

        # Inserts the ordered layers in the list they are going to
        for item in l:
            listbox_to.insert("end", item)

        # Here, should update the figure

