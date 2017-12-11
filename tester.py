from get_linescoord_from_layer_output import get_linescoord_from_layer_output
import numpy as np
from layer import Layer
from calculate_output import calculate_output
from line_coords import Line_coords
from draw_line_coords import draw_line_coords
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


##############################################################
#                       TESTS                                #
##############################################################

# # Test 1
print("Test 1 - get_lines_from_layer_output\n")
# # Define the first layer
W0 = np.array([[-1, 20]])
b0 = np.array([0])
c0 = [255, 0, 0]
l0 = Layer(W0, b0, c0)

theta = []
theta.append(l0)
sizex1 = 100
sizey1 = 100
layer_idx1 = 0
# TEST calculate_output
output = calculate_output(theta, [sizex1, sizey1], layer_idx1)
print("Final output, along 3rd dim.")
for z in range(0, output.shape[2]):
    print("output[:,:,", z, "]\n", output[:,:,z])

# TEST get lines
coords = get_linescoord_from_layer_output(output)
print(coords)

# for i in range(0, coords.shape[1]):
#     print(coords[:,i])
#     idx = coords[:, i]
#     print(output[idx[0], idx[1], idx[2]])
#

# TEST draw lines
img = np.zeros((sizex1+1, sizey1+1, 3))
img2 = np.zeros((sizex1+1, sizey1+1, 3))
draw_line_coords(img2, coords)
print(img2)
fig, ax = plt.subplots(2)
ax[0].imshow(img, cmap='gray',interpolation='nearest', origin='upper')
ax[1].imshow(img2, cmap='gray',interpolation='nearest', origin='upper')

plt.show()
