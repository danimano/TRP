from get_all_lines import *
from create_image_from_lines import *

def create_image(theta, layer_indices, res, img=[], plot_output=False):
    """Generates the image with the boundary lines.
        -- theta: All the layers in the network, ordered.
        -- layer_indices: indicates which layers we would like to draw
        -- res: resolution of the plane
        -- img: optional. If given, the lines will be plotted to that image
        -- plot_output: optional. If true, theta should be given as well.
            If true, the background of the image will be the output of the neuron in the last layer
    """

    all_the_lines = get_all_lines(theta, res, max(layer_indices))
    return create_image_from_lines(all_the_lines, layer_indices, res=res, img=img, theta=theta, plot_output=plot_output)


###############################################################
#    test
###############################################################
