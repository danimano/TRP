import numpy as np
from draw_line import draw_line
from calculate_output import *
from layer import *
from sigmoid import *


def create_image_from_lines(line_list, layer_indices, res, img=[], theta=[] , plot_output=False):
    """Generates the image with the boundary lines.
        -- line_list: contains all the lines from all the layers (list of lists)
        -- layer_indices: indicates which layers we would like to draw
        -- res: resolution of the plane
        -- img: optional. If given, the lines will be plotted to that image
        -- theta: optional. All the layers in the network, ordered.
        -- plot_output: optional. If true, theta should be given as well.
            If true, the background of the image will be the output of the neuron in the last layer
    """

    # If we should plot the network's output, get it
    if plot_output and theta != []:
        # If in the last layer we truly have only 1 neuron
        if theta[(len(theta)-1)].n_neurons == 1:
            # Get the output of the last layer
            img = calculate_output(theta, res, (len(theta)-1))
            # Expand the image to be colored
            img = np.tile(img, (1, 1, 3))
            # print debug info
            print("img shape:", img.shape)
        # If in the last layer we have more than one neuron
        else:
            raise ValueError("Error in create_image_from_lines: The number of neurons in the last layer should be one.")

    # If the image is not given -> create it with the given size (each element is 0)
    if img == []:
        # debug branch
        if plot_output:
            print("plot_output is true, but theta is empty")
        x = np.linspace(-1,1, res[0])
        y = np.linspace(-1,1, res[1])
        img = np.zeros((len(x),len(y),3))
    # If the image is grayscale (has only 1 channel)
    elif len(img.shape) == 2 or img.shape[2] == 1:
        img = img[:, :, np.newaxis]
        img = np.tile(img, (1, 1, 3))

    # for all the layers in layer_indices, draw the boundary lines
    for i in range(len(layer_indices)):
        # If it is not the last layer
        if layer_indices[i] != len(theta)-1:
            # for all the lines in the given layer
            for j in range(len(line_list[layer_indices[i]])):
                # draw the line to the image
                draw_line(img, line_list[layer_indices[i]][j])

    return img
