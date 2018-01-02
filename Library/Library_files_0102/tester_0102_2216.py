from layer import *
from network import *
from get_all_lines import *
from create_image_from_lines import *
import matplotlib.pyplot as plt

##############################################################
#                       TESTS                                #
##############################################################

# TODO play with the structure of the network, change parameters to test the library so far
# Cannot handle intermediate layer having only 1 neuron :(


try:

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
    b2 = np.array([-2])
    c2 = [0, 0, 1]
    l2 = Layer(W2, b2, c2)

    # # Link the layers
    layers = []
    layers.append(l0)
    layers.append(l1)
    layers.append(l2)

    mynet = Network()
    mynet.set_layer(layers)


    res = [201, 101]
    mynet.calculate_all_output(res)

    all_lines_main = get_all_lines(mynet)
    img = create_image_from_lines(all_lines_main, [0, 1], res, network=mynet, plot_output=True)

    # # Show the result
    fig, ax = plt.subplots()
    # ax[0].imshow(img3, cmap='gray', interpolation='nearest', origin='upper')
    ax.imshow(img, cmap='gray', interpolation='nearest', origin='upper')
    plt.show()


except ValueError as e:
    print("Exception cought")
    print(e.args[0])