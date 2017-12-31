from create_image import*
import matplotlib.pyplot as plt
from save_image import *
from layer import *

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
    theta = []
    theta.append(l0)
    theta.append(l1)
    theta.append(l2)

    ##############################################################
    # # Define the input

    # Resolution of the plane (Comment Option1 or Option2)
    # Option1: according to an image:
    # Image to draw on (needed for resolution
    img3 = plt.imread('./lena.jpg')
    img3 = img3 / 255
    print(img3.shape)
    res = [img3.shape[0], img3.shape[1]]
    # # Option2: without image, can be set to any value
    # res = [21, 21]

    # Select which layers should be shown in the output image (all the elements should be less than layer_idx)
    layer_idx1_vec = [0, 1, 2]


    ##############################################################
    # # TEST get_all_lines
    print("\n****** CREATE_IMAGE ******\n")

    # x = np.linspace(0, 10, res[0])
    # y = np.linspace(0, 1, res[1])
    #img3 = np.ones((len(x), len(y), 3))

    img2 = np.array(img3, copy=True)
    img = create_image(theta, layer_idx1_vec, res, img=img2, plot_output=False)

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
    #ax[0].imshow(img3, cmap='gray', interpolation='nearest', origin='upper')
    ax.imshow(img, cmap='gray' ,interpolation='nearest', origin='upper')
    plt.show()


except ValueError as e:
    print("Exception cought")
    print(e.args[0])