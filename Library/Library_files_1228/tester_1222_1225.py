import numpy as np
from layer import Layer
from calculate_output import calculate_output
from get_lines_from_layer_output import get_lines_from_layer_output
from draw_line import draw_line
import matplotlib.pyplot as plt

##############################################################
#                       TESTS                                #
##############################################################

# TODO play with the structure of the network, change parameters to test the library so far

# # Constructing the test network
# # Define the first layer
W0 = np.array([[1, 1], [1, -1]])
b0 = np.array([0, 0])
c0 = [255, 0, 0]
l0 = Layer(W0, b0, c0)

# # Define the second layer
W1 = np.array([[2, 1], [1, 1], [0, 1]])
b1 = np.array([0, 0, 0])
c1 = [0, 255, 0]
l1 = Layer(W1, b1, c1)

# # Define the third layer
W2 = np.array([[2, 1, 1]])
b2 = np.array([0])
c2 = [0, 0, 255]
l2 = Layer(W2, b2, c2)

# # Link the layers
theta = []
theta.append(l0)
theta.append(l1)
theta.append(l2)

##############################################################
# # Define the input

# [sizex1, sizex2] x [sizey1, sizey2]
sizex1 = -20
sizex2 = 20
sizey1 = -20
sizey2 = 20
# The index of the layer we would like to draw
layer_idx1 =2
# Right now you should select manually the neuron to visualize in the layer_idxth layer
neuron_idx = 0

##############################################################
# TEST calculate_output
print("\n****** CALCULATE_OUTPUT ******\n")
output = calculate_output(theta, [sizex1, sizey1, sizex2, sizey2], layer_idx1)
print("Final output, along 3rd dim.")
for z in range(0, output.shape[2]):
    print("output[:,:,", z, "]\n", output[:,:,z])


##############################################################
# TEST get lines
print("\n****** GET_LINES_FROM_LAYER_OUTPUT ******\n")
lines = get_lines_from_layer_output(output)

# Print the coordinates of zero elements layer by layer
for k in range(0, len(lines)):
    print("layer: ", layer_idx1, "neuron: ", k, ", coordinates:\n", lines[k].points)


##############################################################
# TEST draw lines
coords = lines[neuron_idx]

img = np.zeros((sizex2-sizex1+1, sizey2-sizey1+1, 3))
draw_line(img, coords)

# img is a 3D image, each layer should have the same elements.
#   When we can handle colors, or background images, we will need all the RGB channels
print("img, along 3rd dimension:\n")
for z in range(0, img.shape[2]):
    print("img[:,:,", z, "]\n", img[:,:,z])

# Show the result
fig, ax = plt.subplots()
ax.imshow(img, cmap='gray',interpolation='nearest', origin='upper')
plt.show()