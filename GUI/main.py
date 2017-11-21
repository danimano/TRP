import tkinter as tk
from tkinter.messagebox import *

class VisuGUI:
    # Constructor of the GUI
    def __init__(self, window):
        # Initializing the main window, its title and its size
        self.window = window
        self.window.title("Wonderful Neural Network Visualization")
        self.window.geometry("600x400")

        self.menubar = tk.Menu(self.window)
        menu_file = tk.Menu(self.menubar, tearoff = 0)
        menu_file.add_command(label = "Open TensorFlow file", command = self.helloMenu)
        menu_file.add_command(label = "Save current visualization", command = self.helloMenu)
        menu_file.add_separator()
        menu_file.add_command(label = "Exit", command = self.quit)
        self.menubar.add_cascade(label = "File", menu = menu_file)
        self.window.config(menu = self.menubar)

        # Random label
        self.label = tk.Label(self.window, text = "This is the GUI where our NN visualization magic will happen!")
        self.label.pack()
        
        # Random buttons doing simple actions
        self.greet_button = tk.Button(self.window, text = "Hello", command = self.hello)
        self.greet_button.pack(side = tk.LEFT)
        self.close_button = tk.Button(self.window, text = "Close", command = self.quit)
        self.close_button.pack(side = tk.RIGHT)


    # Dummy functions to test displaying and make sure buttons/actions are working
    def hello(self):
        print("Hello!")

    def helloMenu(self):
        print("Hello world!")
        tk.messagebox.showinfo("Say Hello", "Hello World")

    # Exit function (destroy the window) 
    def quit(self):
        self.window.destroy()

# If we are running this file, then we are launching the whole GUI
if __name__ == '__main__':
    root = tk.Tk()
    main = VisuGUI(root)
    # Main window's loop
    root.mainloop()
