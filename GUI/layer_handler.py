import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

from pear.get_color_for_layeridx import get_color_for_layeridx
from pear.layer import Layer

class LayerHandler(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Adding the button that moves layers from the hidden list to the shown list
        self.add_layer = ttk.Button(self, text = "Add layer", command = lambda:self.change_layer(self.hidden_layers, self.shown_layers), state = "disabled")
        add_icon = ImageTk.PhotoImage(file = settings.ADD)
        self.add_layer.config(image = add_icon, compound="right")
        self.add_layer.icon = add_icon
        self.add_layer.grid(row = 0, column = 0, pady = 2)
        
        # Displaying the list of all the available layers to draw
        self.hidden_layers = tk.Listbox(self, selectmode = "extended")
        self.hidden_layers.grid(row = 1, column = 0, sticky = "n", padx = (10, 0), ipady = 30)

        # Binding a scrollbar to the available layers' listbox
        scrollbar_hidden = tk.Scrollbar(self)
        self.hidden_layers.config(yscrollcommand = scrollbar_hidden.set)
        scrollbar_hidden.grid(row = 1, column = 1, sticky = "nsw")
        scrollbar_hidden.config(command = self.hidden_layers.yview) 

        # Adding the button that moves layers from the shown list to the hidden list
        self.rm_layer = ttk.Button(self, text = "Remove layer", command = lambda:self.change_layer(self.shown_layers, self.hidden_layers), state = "disabled")
        remove_icon = ImageTk.PhotoImage(file = settings.REMOVE)
        self.rm_layer.config(image = remove_icon, compound = "right")
        self.rm_layer.icon = remove_icon
        self.rm_layer.grid(row = 0, column = 2, pady = 2)

        # Displaying the list of all the drawn layers
        self.shown_layers = tk.Listbox(self, selectmode = "extended")
        self.shown_layers.grid(row = 1, column = 2, sticky = "n", padx = (10, 0), ipady = 30)

        # Binding a scrollbar to the shown layers' listbox
        scrollbar_shown = tk.Scrollbar(self)
        self.shown_layers.config(yscrollcommand = scrollbar_shown.set)
        scrollbar_shown.grid(row = 1, column = 3, sticky = "nse", padx = (0, 10))
        scrollbar_shown.config(command = self.shown_layers.yview)



    # Adds or removes one or several layers from the displayed figure
    def change_layer(self, listbox_from, listbox_to):

        # Gets the selected layers and removes them from the list they are taken from
        current = listbox_from.curselection()
        for item in current[: : -1]:
            listbox_to.insert("end", listbox_from.get(item))
            listbox_from.delete(item)

        # Sorts the items from the modified list to have ordered layers
        l = list()
        for i in range(0, listbox_to.size()):
           l.append(listbox_to.get(i)) 
        listbox_to.delete(0, "end")
        l.sort(key=lambda item: (len(item), item)) # Sort by length of the string, then by alphabetical order

        # Inserts the ordered layers in the list they are going to
        for item in l:
            listbox_to.insert("end", item)

        # Clears the selection (mouse selection over the listbox)
        listbox_from.selection_clear(0, "end")


    # Refresh the listboxes containing the layers (when opening, filling them; when closing, emptying them)
    def refresh_layers(self, network):
        print("Refreshing the layers' listboxes!")
        if settings.OPENED:
            self.add_layer.config(state = "normal")
            self.rm_layer.config(state = "normal")

            # Filling the listboxes with the existing layers
            layer_number = len(network.get_layers())
            for i in range(0, layer_number - 2):
                self.hidden_layers.insert("end", "Layer " + str(i + 1))
            self.shown_layers.insert("end", "Layer " + str(layer_number - 1))
            
        else: # Deleting the layers
            self.add_layer.config(state = "disabled")
            self.rm_layer.config(state = "disabled")
            self.hidden_layers.delete(0, "end")
            self.shown_layers.delete(0, "end")        

