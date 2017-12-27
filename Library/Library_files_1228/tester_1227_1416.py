from get_all_lines import *
from create_image import*
import matplotlib.pyplot as plt
from save_image import *
from layer import *

##############################################################
#                       TESTS                                #
##############################################################

# TODO play with the structure of the network, change parameters to test the library so far
# Cannot handle intermediate layer having only 1 neuron :(

# # Constructing the test network
# # Define the first layer
W0 = np.array([[1, 2], [2, 1]])
b0 = np.array([0, 0])
c0 = [1, 0, 0]
l0 = Layer(W0, b0, c0)

# # Define the second layer
W1 = np.array([[-1, 1], [1, -2]])
b1 = np.array([0, 0])
c1 = [0, 1, 0]
l1 = Layer(W1, b1, c1)

# # Define the third layer
W2 = np.array([[1, 1]])
b2 = np.array([-3])
c2 = [0, 0, 1]
l2 = Layer(W2, b2, c2)

# # Link the layers
theta = []
theta.append(l0)
theta.append(l1)
theta.append(l2)

##############################################################
# # Define the input

# [sizex1, sizex2] x [sizey1, sizey2]
sizex1 = -30
sizex2 = 30
sizey1 = -30
sizey2 = 30
size_vec = [sizex1, sizey1, sizex2, sizey2]
# The index of the layer until we would like to calculate the output
layer_idx1 = 2
# Select which layers should be shown in the output image (all the elements should be less than layer_idx)
layer_idx1_vec = [0, 1, 2]

##############################################################
# # TEST get_all_lines
print("\n****** GET_ALL_LINES ******\n")

all_lines_main = get_all_lines(theta, size_vec, layer_idx1)

for i in range(0, len(all_lines_main)):
    print("Lines in the ", i, "th layer:\n")
    for j in range(len(all_lines_main[i])):
        print("--", j, "th neuron:\n")
        print(all_lines_main[i][j].points)


##############################################################
# # TEST create_image
print("\n****** CREATE_IMAGE ******\n")

x = np.linspace(size_vec[0], size_vec[2], size_vec[2] - size_vec[0] + 1)
y = np.linspace(size_vec[1], size_vec[3], size_vec[3] - size_vec[1] + 1)

img2 = np.zeros((len(x), len(y), 3))
img = create_image(all_lines_main, layer_idx1_vec, size_vec, img2)


print("img, along 3rd dimension:\n")
for z in range(0, img.shape[2]):
    print("img[:,:,", z, "]\n", img[:,:,z])


##############################################################
# # TEST save_image
print("\n****** SAVE_IMAGE ******\n")

save_image('./trial.png', img)


##############################################################
# # Show the result
fig, ax = plt.subplots()
ax.imshow(img, cmap='gray',interpolation='nearest', origin='upper')
plt.show()