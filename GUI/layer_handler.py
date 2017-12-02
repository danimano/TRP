import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

class LayerHandler(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        
        # Displaying the list of all the available layers to draw
        hidden_layers = tk.Listbox(self, selectmode = "extended")
        hidden_layers.grid(row = 1, column = 0, sticky = "n", padx = 10, ipady = 30)
        
        # Filling the list (so far, hardcoded values)
        for item in ["Layer 1", "Layer 2", "Layer 3", "Layer 4", "Layer 5", "Layer 6", "Layer 7", "Layer 8", "Layer 9", "Layer 10", "Layer 11", "Layer 12", "Layer 13", "Layer 14", "Layer 15", "Layer 16", "Layer 17", "Layer 18", "Layer 19", "Layer 20", "Layer 21"]:
            hidden_layers.insert("end", item)

        # Adding the button that moves layers from the hidden list to the shown list
        more_layer = ttk.Button(self, text = "Add layer", command = lambda:self.change_layer(hidden_layers, shown_layers))
        add_icon = ImageTk.PhotoImage(file = settings.ADD)
        more_layer.config(image = add_icon, compound="right")
        more_layer.icon = add_icon
        more_layer.grid(row = 0, column = 0, pady = 2)

        # Displaying the list of all the drawn layers
        shown_layers = tk.Listbox(self, selectmode = "extended")
        shown_layers.grid(row = 1, column = 1, sticky = "n", padx = 10, ipady = 30)

        # Adding the button that moves layers from the shown list to the hidden list
        rm_layer = ttk.Button(self, text = "Remove layer", command = lambda:self.change_layer(shown_layers, hidden_layers))
        remove_icon = ImageTk.PhotoImage(file = settings.REMOVE)
        rm_layer.config(image = remove_icon, compound = "right")
        rm_layer.icon = remove_icon
        rm_layer.grid(row = 0, column = 1, pady = 2)
      

    # Adds or removes one or several layers from the displayed figure
    def change_layer(self, listbox_from, listbox_to):

        # Gets the selected layers and removes them from the list they are taken from
        current = listbox_from.curselection()
        for item in current:
            listbox_to.insert("end", listbox_from.get(item))

         # BUG HERE   
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

        # Clears the selection (mouse selection over the listbox)
        listbox_from.selection_clear(0, "end")
