from matplotlib.figure import Figure

def init():
    global ICON, FONT, ADD, REMOVE, REFRESH, FILENAME, FIGURE
    ICON = "images/icon.ico"
    FONT= ("Georgia", 12)
    ADD = "images/add-icon.png"
    REMOVE = "images/remove-icon.png"
    REFRESH = "images/refresh-icon.png"
    FILENAME = "No file to visualize"
    FIGURE = Figure(figsize = (5, 5), dpi = 100)
    
    
    
