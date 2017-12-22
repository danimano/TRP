import numpy as np
from pear.line import Line

# Why are the imports unused?...


def draw_line(img, line):
    """Draw the line given in 'line' on 'img'."""
    print("\n--Function draw_line starts...\n")

    # TODO set colors to layer
    color = 1

    # For each pixel indicated in line we set img to color.
    # TODO there should be a better way than do it pixel by pixel
    for i in range(0, line.points.shape[1]):
        idx = line.points[:,i]
        img[idx[0], idx[1], :] = color

    # print function end - debug
    print("\n--Function draw_line ends...\n")




# TODO
#######################################################
#                       TESTS                         #
#######################################################
