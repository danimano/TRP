from pear.reader import read_tensorflow_file
from pear.get_color_for_layeridx import get_color_for_layeridx
from pear.layer import Layer

class NetworkHandler:
    """Contains the structure a neural network given as an input."""

    def __init__(self, filename):
        """Create a new NetworkHandler object.
        A NetworkHandler object has three attributes:
        - a name "filename" (here, its full path)
        - parameters "theta" containing, for each layer, weight and bias
        - a list of layers "layers" containing Lyaer objects that correspond to a layer
        """
        self.__filename = self.parse_filename(filename)
        self.__theta = read_tensorflow_file(self.__filename)
        self.__layers = self.create_layers(self.__theta)

    
    def parse_filename(self, filename):
        """Parse the full path of the META input file containing a part of the network's structure.
        The network's structure is contained in three different files with the same name but various extensions.
        "filename" is being parsed so that the full path is preserved but the extension removed.
        """        
        filename_split = filename.split(".")
        filename_path = ""
        for i in range(0, len(filename_split) - 1):
            filename_path += filename_split[i]
            if i < len(filename_split) - 2:
                filename_path += "."
        print(filename_path)
        return filename_path


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
