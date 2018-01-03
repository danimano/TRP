from pear.get_all_lines import *
from pear.create_image_from_lines import *


def create_image(network, layer_indices, res=None, img=None, plot_output=False):
    """Generates the image with the boundary lines.
        -- network: The Network object representing the network
        -- layer_indices: indicates which layers we would like to draw
        -- res: resolution of the plane ([n_col, n_row]) (if img is given, [should be img.shape[1], img.shape[0]])
        -- img: optional. If given, the lines will be plotted to that image
        -- plot_output: optional.
            If true, the background of the image will be the output of the neuron in the last layer
    """

    # If neither img nor res is given -> error, we do not know the resolution
    if img is None and res is None:
        raise ValueError("ERROR in create_image: No resolution specified")

    # If img is given, we set res for the resolution of the image
    if img is not None:
        res = [img.shape[1], img.shape[0]]

    # Calculate the output of the network for the specified resolution
    network.calculate_all_output(res)
    # Get the boundary lines
    all_the_lines = get_all_lines(network)
    # Return the created image
    return create_image_from_lines(all_the_lines, layer_indices, res=res, img=img, network=network, plot_output=plot_output)


###############################################################
#    test
###############################################################
