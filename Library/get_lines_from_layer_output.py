import numpy as np
from line import Line

# The boundary can not be on the first column or row of the output h - is it a problem?...


def get_lines_from_layer_output(h):
    """
    h: output of a layer
    From the output, calculate the boundary lines.
    Return a list of lines, containing a line object for each neuron in the layer.
    If the layer contained m neuron, lines will be m long.
        [lines] = get_lines_from_layer_output(h)
    """

    # print info - debug
    print("\n--Function get_lines_from_layer_output starts...\n")

    # Plan: where the sign changes, we have the boundary

    # Get the sign for each element
    signed_h = np.sign(h)
    # Create an array to store if the sign changes at a given point of the input or not
    h_conv = np.zeros_like(signed_h)

    # This is a kind of convolution with [1 1] and [1,1]' kernels, but I could not find 2d convolution in numpy
    # This for loops could be merged and optimized...

    # For each neuron separately
    for k in range(0, signed_h.shape[2]):
        # Search for sign change in columns: If the sign changes from [i,j-1] to [i,j] than h_conv at [i,j]
        #   will contain 0, otherwise h[i,j] = 1. We do not examine where j=0. (first column)
        for i in range(0, signed_h.shape[0]):
            for j in range(0, signed_h.shape[1]):
                # first column: skip, here we can not have the boundary
                if j == 0:
                    h_conv[i, j, :] = 1
                # j > 0
                else:
                    # If the sign does not change
                    if signed_h[i, j, k] == signed_h[i, j-1, k]:
                        h_conv[i,j,k] = 1
                    # if the sign changes
                    else:
                        h_conv[i, j, k] = 0

        # Search for sing change in rows: almost the same as with columns, but we compare [i-1, j] with [i,j]
        # We only overwrite the elements if the sign differs between the rows, we do not set to '1'
        #   any element which was marked as 'changing sign' ones during examining the columns.
        for j in range(0, signed_h.shape[1]):
            for i in range(0, signed_h.shape[0]):
                # if it is the first row -> skip
                if i == 0:
                    h_conv[i, j, :] = 1
                # if the signe differs: set
                else:
                    if signed_h[i, j, k] != signed_h[i-1, j, k]:
                        h_conv[i, j, k] = 0

    print("h_conv (0 indicates sign changing) along 3rd dimension:\n")
    for z in range(0, h_conv.shape[2]):
        print("h_conv[:,:,", z, "]\n", h_conv[:, :, z])


    lines = []
    # For each neuron (channel) find the zero elements in h_conv. Convert them to Line objects,
    #   and append these Line objects ordered to the lines list
    for k in range(0, h_conv.shape[2]):
        lines.append(Line(np.array(np.where(h_conv[:,:,k] == 0))))

    # print info - debug
    print("\n--Function get_lines_from_layer_output ends...\n")

    return lines



# TODO tests...
