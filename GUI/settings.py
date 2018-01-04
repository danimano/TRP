from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def init():
    global ICON, FONT, ADD, REMOVE, REFRESH, INFO, FILENAME, FIGURE, OPENED, BACKGROUND, RESOLUTION
    ICON = "images/icon.ico"
    FONT= ("Georgia", 12)
    ADD = "images/add-icon.png"
    REMOVE = "images/remove-icon.png"
    REFRESH = "images/refresh-icon.png"
    INFO = "images/information-icon.png"
    FILENAME = "No file to visualize"
    FIGURE = plt.figure()
    OPENED = False
    BACKGROUND = "No file loaded..."
    RESOLUTION = [301, 301]    
    
    
    
