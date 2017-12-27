import numpy as np
from draw_line import draw_line


def create_image(line_list, layer_indices, size, img=[]):
    """Generates the image with the boundary lines.
        -- line_list: contains all the lines from all the layers (list of lists)
        -- layer_indices: indicates which layers we would like to draw
        -- size: size of the image to draw
        -- img: optional. If given, the lines will be plotted to that image
    """

    # If the image is not given -> create it with the given size (each element is 0)
    if img == []:
        x = np.linspace(size[0], size[2], size[2]-size[0]+1)
        y = np.linspace(size[1], size[3], size[3]-size[1]+1)
        img = np.zeros((len(x),len(y),3))

    # for all the layers in layer_indices
    for i in range(len(layer_indices)):
        # for all the lines in the given layer
        for j in range(len(line_list[layer_indices[i]])):
            # draw the line to the image
            draw_line(img, line_list[layer_indices[i]][j])

    return img
