import numpy as np

# Changes the array itself!


def apply_nonlinearity(h):
    """Applies ReLU on each element of h.
        h -- 3D numpy array, each plane contains the output of a neuron for all possible input pair
             ReLU:
                0 if h <= 0
                h if h > 0
        Returns the result. (list having the same size as the input)
    """

    low_values_flags = h < 0  # Where values are low
    h[low_values_flags] = 0  # All low values set to 0



#########################################################
#                       TESTS                           #
#########################################################

# # TEST 1
# # Example with array containing positive numbers
# trial1 =  np.ones((3,3,3))
# print(trial1)
# nonl_trial1 = applyNonLinearity(trial1)
# print(nonl_trial1)

# # TEST 2
# # Complicated example (positive and negative numbers as well)
# trial2 = np.zeros((3,3,3))
# for i in range(0,3):
#     for j in range(0, 3):
#         for k in range(0, 3):
#             trial2[i][j][k] = i/2+j/3-k
#
# print('trial2:\n')
# print(trial2)
# apply_nonlinearity(trial2)
# print('\nAfter ReLU:\n')
# print(trial2)