import numpy as np
from line_coords import Line_coords


def draw_line_coords(img, line_coords):
    print("In draw_line_coords...\n")
    color = 1
    for i in range(0, line_coords.points.shape[1]):
        idx = line_coords.points[:,i]
        img[idx[0], idx[1], :] = color



# for i in range(0, coords.shape[1]):
#     print(coords[:,i])
#     idx = coords[:, i]
#     print(output[idx[0], idx[1], idx[2]])





#######################################################
#                       TESTS                         #
#######################################################
# Maybe it has a different type
#coords = (np.array([0, 1, 1, 2, 2]), np.array([1, 1, 2, 2, 3]), np.array([0, 0, 0, 0, 0]))
#l0 = Line_coords()