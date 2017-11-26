import numpy as np
from layer import Layer
from apply_nonlinearity import apply_nonlinearity

# I think it calculates the right things, but should be checked
# there is no kind of error handling so far

def calculate_output(theta, size, layer_idx):
    """Calculates the  output of the given layer for all the possible inputs in [0, size-1].

        theta ~ ([layer]) -- List of layers. Weight matrices and bias vectors of the network, where i = [1..layer_idx]
        layer_idx -- index of the layer, for which we want to determine the output
        size -- The size of the input area we are working with ([size_x, size_y]).
            The input parameters goes from 0..size_x-1, 0..size_y-1

        The output is calculated in the following way:
            h_0 = W_0*x+b_0
            h_i = W_i*applyNonLinearity(W_{i-1}*h_{i-1}+b_{i-1})+b_i   for i = 1..layer_idx

        Returns the output(s) of the queried layer in a 3D array, where each plane represents the output of one neuron.
            (If the layer has n_i neuron, the size of the output will be size_x * size_y * n_i).
    """
    # TODO - test if we really have enough (and the right) layer in theta?
        # we can test the size of the weight matrices eg

    # generate input field - it is always 2 dimensional
    x = np.linspace(0, size[0], size[0]+1)
    y = np.linspace(0, size[1], size[1]+1)
    # initialize h_new for the first layer
    # TODO there should be a better way to do this...
    h_new = np.zeros((theta[0].n_input, len(x)*len(y)))
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            h_new[:,i*len(y)+j] = [x[i], y[j]]

    print("\nInput of the 0th layer\n", h_new)

    # for each layer 0..layer_idx-1
    for layer_i in range(0, layer_idx+1):
        # save the output of the previous layer/input of the layer to h_old
        h_old = h_new

        # Calculate the layer's output
        del h_new
        h_new = theta[layer_i].calculate_layer_output_mat(h_old)

        # If it is not the output of the layer_idxth layer: apply the nonlinearity
        if layer_i != layer_idx:
            apply_nonlinearity(h_new)

        # Clear the input (it will be overwritten in the next iteration
        del h_old

        # Print the output of the layer - debug
        print("Output of layer", layer_i, ":\n",h_new)

    # Convert the output of the layer in the abovedefined format
    h_new = np.reshape(h_new.transpose(), [len(x), len(y), h_new.shape[0]], 'C')

    # return the output of the layer_idxth layer
    return h_new


#################################################
#                   TESTS                       #
#################################################

# TEST 1
# 3layer network, predefined weights and biases

# Define the first layer
W0 = np.array([ [1, 0], [0, 1], [-1, 0], [0, -1] ])
b0 = np.array([0, 0, 0, 0])
# Why does it run the whole layer.py file??
l0 = Layer(W0, b0)

# Define the second layer
W1 = np.array([ [1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 1, 2]])
b1 = np.array([ 0, 0, 0])
l1 = Layer(W1, b1)

# Define the third layer
W2 = np.array([ [-1, 0, 0], [1, 1, 0]])
b2 = np.array([ 0, 0])
l2 = Layer(W2, b2)

theta = []
theta.append(l0)
theta.append(l1)
theta.append(l2)
sizex1 = 2
sizey1 = 3
layer_idx1 = 2
output = calculate_output(theta, [sizex1, sizey1], layer_idx1)
print("Final output, along 3rd dim.")
for z in range(0, output.shape[2]):
    print("output[:,:,z]\n", output[:,:,z])