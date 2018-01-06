import matplotlib.pyplot as plt

def init():
    """
    Initialize all the global variables that will be called across the interface.
    All the values of these variables are fixed, except for the "OPENED" one, which changes depending on whether a file is opened.
    """
    global ICON, FONT, ADD, REMOVE, REFRESH, INFO, FILENAME
    global FIGURE, OPENED, BACKGROUND, RESOLUTION
    global OPEN_ICON, CLOSE_ICON, SAVE_ICON, REFRESH_ICON, EXIT_ICON, HELP_ICON, DOC_ICON
    global LOGO, URL, MISSING_DATA, MISSING_META, EMPTY_NETWORK
    ICON = "images/icon.ico"
    FONT= ("Georgia", 13)
    ADD = "images/add-icon.png"
    REMOVE = "images/remove-icon.png"
    REFRESH = "images/refresh-icon.png"
    INFO = "images/information-icon.png"
    FILENAME = "No file to visualize"
    FIGURE = plt.figure()
    OPENED = False
    BACKGROUND = "No file loaded..."
    RESOLUTION = [301, 301]    
    OPEN_ICON = "images/open-file-icon.png"
    CLOSE_ICON = "images/close-file-icon.png"
    SAVE_ICON = "images/save-image-icon.png"
    REFRESH_ICON = "images/reload-icon.png"
    EXIT_ICON = "images/exit-icon.png"
    HELP_ICON = "images/help-icon.png"
    DOC_ICON = "images/documentation-icon.png"
    LOGO = "images/pear_logo.png"
    URL = "https://pypi.python.org/pypi/pearlib/"
    MISSING_DATA = "The network you are trying to open presents missing or corrupted data and cannot be reconstructed. "
    MISSING_DATA += "The .INDEX or .DATA files might be missing."
    MISSING_META = "The .META file of the network you are trying to open does not seem to exist!"
    EMPTY_NETWORK = "The network you are trying to open seems empty. "
    EMPTY_NETWORK += "Either your network really is empty, or it does not follow the mandatory guidelines to open a TensorFlow network with Pear. "
    EMPTY_NETWORK += "Please refer to the network guidelines."
    
    
