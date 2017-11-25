import numpy as np


class Layer:
    """Class for defining a layer with its weight matrix and bias vector"""
    W = []
    b= []
    n_neurons = 0
    n_input = 0

    def __init__(self, _W, _b):
        self.W = _W
        self.b = _b
        self.n_neurons = _W.shape[0]
        self.n_input = _W.shape[1]

    def calculate_layer_output(self, *args):
        input_vec = np.array(args)
        #print("Input_vec:\n", input_vec, input_vec.shape)
        if input_vec.shape[0] != self.n_input:
            # TODO error handling
            print("Inputs are not matching")
            return

        # it multiplies even if it shouldn't because of the shape.. careful
        return np.matmul(self.W, input_vec) + self.b


##############################################################
#                       TESTS                                #
##############################################################

# Empty constructor - error since we do not have that
#l1 = Layer()
#print("W:\n", l1.W, "b:\n", l1.b)


l2 = Layer(np.array([(1,2), (2,3), (5,6)]), [1,2,3])
print("W:\n", l2.W, "\nb:\n", l2.b)

l3 = Layer(np.array([[1,2], [2,3], [5,6]]), [1,2,3])
l3.b = [4,5,6]
print("W:\n", l3.W, "\nb:\n", l3.b)

l4 = Layer(np.array([ [2, 1], [1, 2] ]), [-2, -2])
out4 = l4.calculate_layer_output(2, 10)
expected = [12, 20]
print("Output:\n", out4, "\nExpected:\n", expected)