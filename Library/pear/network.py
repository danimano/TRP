from pear.reader import read_tensorflow_file
from pear.get_color_for_layeridx import get_color_for_layeridx
from pear.layer import Layer

class Network:
    """Contains the structure a neural network given as an input."""

    def __init__(self, filename):
        """Create a new NetworkHandler object.
        A NetworkHandler object has three attributes:
        - a name "filename" (here, its full path without any extension)
        - parameters "theta" containing, for each layer, weight and bias
        - a list of layers "layers" containing Lyaer objects that correspond to a layer
        """
        self.__filename = filename
        self.__theta = read_tensorflow_file(self.__filename)
        self.__layers = self.create_layers(self.__theta)

    def create_layers(self, theta):
        """Given the parameters "theta" of a network, extract the layers and build Layer objects from them.
        """
        layers = []
        for i in range(0, len(theta)):
            color = get_color_for_layeridx(i)
            W = theta[i][0]
            b = theta[i][1]
            layers.append(Layer(W, b, color))
        return layers

    def get_filename(self):
        return self.__filename

    def get_theta(self):
        return self.__theta

    def get_layers(self):
        return self.__layers
