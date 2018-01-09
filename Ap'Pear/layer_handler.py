import settings

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import webcolors

from pearlib.get_color_for_layeridx import get_color_for_layeridx
from pearlib.layer import Layer

class LayerHandler(tk.Frame):
    """
    The LayerHandler object handles the user's choices as to which layers should be drawn on the figure and which should not.
    Its attributes are:
        - parent: the parent of the LayerHandler object, which gives access to the parent's objects' functions.
        - add_layer: the button moving layers from the hidden list to the showing list.
        - hidden_layers: the listbox containing all the layers that are currently not being shown on the image.
        - rm_layer: the button moving layers from the showing list to the hidden list.
        - shown_layers: the listbox containing all the layers that are currently being shown on the image.
        - info_last_layer: the message explaining why the last layer of the network never appears in any of the lists.
    """

    def __init__(self, parent, controller, *args, **kwargs):
        """
        Initialize the LayerHandler object.
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Adding the button that moves layers from the hidden list to the shown list
        self.add_layer = ttk.Button(self, text = "Add layer", command = lambda:self.change_layer(self.hidden_layers, self.shown_layers), state = "disabled")
        add_icon = ImageTk.PhotoImage(file = settings.ADD)
        self.add_layer.config(image = add_icon, compound="right")
        self.add_layer.icon = add_icon
        self.add_layer.grid(row = 0, column = 0, columnspan = 2, pady = 2)
        
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
        self.rm_layer.grid(row = 0, column = 2, columnspan = 2, pady = 2, padx = (0, 12))

        # Displaying the list of all the drawn layers
        self.shown_layers = tk.Listbox(self, selectmode = "extended")
        self.shown_layers.grid(row = 1, column = 2, sticky = "n", padx = (10, 0), ipady = 30)

        # Binding a scrollbar to the shown layers' listbox
        scrollbar_shown = tk.Scrollbar(self)
        self.shown_layers.config(yscrollcommand = scrollbar_shown.set)
        scrollbar_shown.grid(row = 1, column = 3, sticky = "nse", padx = (0, 10))
        scrollbar_shown.config(command = self.shown_layers.yview)

        # Adding some info about why the last layer does not appear in the list
        info_last_layer = "The last layer of the network does not appear in the layers' lists. This is due to the fact that we are applying a sigmoïd function on the last layer rather than the rectified liner unit operator. The last layer thus does not have any boundary decision to display."
        font = ("", 8, "italic")
        self.info_message = tk.Message(self, text = info_last_layer, font = font, width = 298)
        self.info_message.grid(row = 2, column = 0, columnspan = 5)



    def change_layer(self, listbox_from, listbox_to):
        """
        Move the selected layers in listbox_from to listbox_to.
        Make sure the lists are updated and re-ordered.
        """
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
        l.sort(key = lambda item: (len(item), item)) # Sort by length of the string, then by alphabetical order

        # Inserts the ordered layers in the list they are going to
        for item in l:
            listbox_to.insert("end", item)

        # Clears the selection (mouse selection over the listbox)
        listbox_from.selection_clear(0, "end")
        self.apply_color_to_layers()


    def refresh_layers(self, network):
        """
        Refresh the listboxes containing the layers.
        When opening a file, fill them.
        When closing a file, empty them.
        """
        if settings.OPENED:
            self.add_layer.config(state = "normal")
            self.rm_layer.config(state = "normal")

            # Filling the listboxes with the existing layers
            layer_number = len(network.get_layers())
            for i in range(0, layer_number - 2):
                self.hidden_layers.insert("end", "Layer " + str(i + 1))
            self.shown_layers.insert("end", "Layer " + str(layer_number - 1))

            self.apply_color_to_layers()
            
        else: # Deleting the layers
            self.add_layer.config(state = "disabled")
            self.rm_layer.config(state = "disabled")
            self.hidden_layers.delete(0, "end")
            self.shown_layers.delete(0, "end")


    def get_layers_to_draw(self):
        """
        Retrieve the indices of the layers contained in the to-show list.
        """
        layers_to_draw = []
        current_items = self.shown_layers.get(0, "end")
        for item in current_items:
            layers_to_draw.append(int(item.split(" ")[-1]) - 1)
        return layers_to_draw


    def apply_color_to_layers(self):
        """
        Sets the color of the layer in the listbox to the color of this layer's lines in the figure.
        """
        layers = self.parent.network.get_layers()
        hidden = self.hidden_layers.get(0,"end")
        shown = self.shown_layers.get(0, "end")

        # Getting the html color (or closest color) to the RGB code.
        cnt = 0
        for item in hidden:
            layer_number = int(item.split(" ")[-1]) - 1
            color = layers[layer_number].color # Retrieving the layer's color
            # Converting the color from double to uint8 and making a tuple out of it
            color = (round(color[0] * 255), round(color[1] * 255), round(color[2] * 255)) 
            real_color, closest_color = self.get_color_name(color)
            self.hidden_layers.itemconfig(cnt, foreground = closest_color)
            cnt += 1
            
        cnt = 0
        for item in shown:
            layer_number = int(item.split(" ")[-1]) - 1
            color = layers[layer_number].color # Retrieving the layer's color
            # Converting the color from double to uint8 and making a tuple out of it
            color = (round(color[0] * 255), round(color[1] * 255), round(color[2] * 255))
            real_color, closest_color = self.get_color_name(color)
            self.shown_layers.itemconfig(cnt, foreground = closest_color)
            cnt += 1


    def closest_color(self, requested_color):
        """
        Given a RGB color code that does not correspond to any HTML color code, find the closest HTML color code.
        """
        min_colors = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_color[0]) ** 2
            gd = (g_c - requested_color[1]) ** 2
            bd = (b_c - requested_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]


    def get_color_name(self, requested_color):
        """
        Given a RGB color, find its matching HTML color code or, if it does not exist, its closest matching color code.
        """
        try:
            closest_name = actual_name = webcolors.rgb_to_name(requested_color)
        except ValueError:
            closest_name = self.closest_color(requested_color)
            actual_name = None
        return actual_name, closest_name
