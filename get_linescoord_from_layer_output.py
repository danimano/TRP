import numpy as np
from line_coords import Line_coords

# The boundary can not be on the first coloumn of the output h


def get_linescoord_from_layer_output(h):
    """
    h: output of a layer
    From the output, it calculates the parameters of the lines.
    Return a list of lines, containing the line object for each neuron in the layer.
    If the layer contained m neuron, lines will be m long.
        [lines] = get_lines_from_layeroutput(h)
    """
    signed_h = np.sign(h)
    print(h.shape, signed_h, signed_h.shape)
    h_conv = np.zeros_like(signed_h)
    #h_conv = h_conv.squeeze()
    print(h_conv.dtype)

    # This is a kind of convolution with [1 1] kernel, but I could not find 2d convolution in numpy
    # It is unnecessary to go through the lines
    for i in range(0, signed_h.shape[0]):
        for j in range(0, signed_h.shape[1]):
            if j == 0:
                h_conv[i, j, :] = 1
            else:
                for k in range(0, signed_h.shape[2]):
                    if signed_h[i, j, k] == signed_h[i, j-1, k]:
                        h_conv[i,j,k] = 1
                    else:
                        h_conv[i, j, k] = 0
            # print(i,j,":\n\t", h_conv[i,j], "\n")

    print("h_conv along 3rd dim.")
    for z in range(0, h_conv.shape[2]):
        print("h_conv[:,:,", z, "]\n", h_conv[:, :, z])

    coords = np.where(h_conv == 0)
    coords = np.array(coords)
    print("coords: \n", coords)
    #lcoords = []

    #for i in range(0, coords.shape[1]):
    #    lcoords.append(coords[:, i])
        #print(output[idx[0], idx[1], idx[2]])

    return Line_coords(coords)
        #signed_h_ext = np.concatenate((signed_h, signed_h[:, 1]), axis = 1)
    #print(signed_h_ext.shape, signed_h_ext)





