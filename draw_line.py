import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from line import Line


# Plan 1: draw lines with matplotlib function, and get the resulted figure as an image
#http://www.icare.univ-lille1.fr/tutorials/convert_a_matplotlib_figure
#https://stackoverflow.com/questions/35355930/matplotlib-figure-to-image-as-a-numpy-array
# I couldn't get the image

# Plan 2: Multidimensional numpy array, draw the lines as changing the belonging coordinates
# Havn't tried that so far.


def draw_segment(img, p1, p2):
    """This could draw a segment between the given two points"""

    # Draw the segment to the image
    # pad the array to 3D
    img = np.dstack([img]*3)
    return img

def draw_line(img, line):
    """ Draws the line( / broken line) on img
        img: image to draw on
        line: Line object
    """

    # Calls drawsegment with each segment
    for i in range(1, len(line.points)):
        draw_segment(img, line.points[i, i-1])


# Found on the internet, does not work for me...
def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    return buf



#######################################################
#                       TESTS                         #
#######################################################

# TEST 1
points1 = [[0, 0], [2, 2], [3, 5]]
sign = 1
line1 = Line(points1, sign)
x = 10
y= 10
img = np.zeros((x,y))

img_s = draw_segment(img, points1[0], points1[1])
print(img_s.shape)
fig, ax = plt.subplots()
ax.imshow(img_s)#, cmap='gray',interpolation='nearest',
            #origin='lower',  extent=[0, 10, 0, 10])

# # Things I tried randomly...

#img_l = draw_line(img, line1)
# check the parameters
# fig, ax = plt.subplots()
# ax.imshow(img, cmap='gray',interpolation='nearest',
#             origin='lower',  extent=[0, 10, 0, 10])
# plt.plot([0, 1], [2, 3], linestyle='-')

##
#
# fig = Figure()
# canvas = FigureCanvas(fig)
# ax = fig.gca()
#
# ax.text(0.0,0.0,"Test", fontsize=45)
# ax.axis('off')
#
# canvas.draw()       # draw the canvas, cache the renderer
#
# image = np.fromstring(canvas.tostring_rgb(), dtype=np.uint8)
# plt.imshow(image)
#
# ##

# fig1 = plt.gcf()
# img2 = fig2data(fig1)
#
# print(img2)

# plt.savefig("trial.png")
# print(img2)
# img2.draw(Line((2,2), (5,7)))

#print(img)
#plt.draw((0, 1), (2,3))

plt.show()


#plt.plot([0, 1], [2, 3], color='k', linestyle='-', linewidth=2)
#plt.savefig("trial.png")