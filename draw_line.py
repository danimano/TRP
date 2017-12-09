import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from line import Line


# TODO color handling
# so far the image has only 1 channel (since it's gray). If we want to have colors, we should make it 3D
# TODO simplify functions
# the line-drawing functions are from the internet, we do not use all the output values, might be simplified


def naive_line(r0, c0, r1, c1):
    """Another possibility to draw lines"""
    # The algorithm below works fine if c1 >= c0 and c1-c0 >= abs(r1-r0).
    # If either of these cases are violated, do some switches.
    if abs(c1-c0) < abs(r1-r0):
        # Switch x and y, and switch again when returning.
        xx, yy, val = naive_line(c0, r0, c1, r1)
        return (yy, xx, val)

    # At this point we know that the distance in columns (x) is greater
    # than that in rows (y). Possibly one more switch if c0 > c1.
    if c0 > c1:
        return naive_line(r1, c1, r0, c0)

    # We write y as a function of x, because the slope is always <= 1
    # (in absolute value)
    x = np.arange(c0, c1+1, dtype=float)
    print(x)
    y = x * (r1-r0) / (c1-c0) + (c1*r0-c0*r1) / (c1-c0)
    print(y)

    valbot = np.floor(y)-y+1
    valtop = y-np.floor(y)

    return (np.concatenate((np.floor(y), np.floor(y)+1)).astype(int), np.concatenate((x,x)).astype(int),
            np.concatenate((valbot, valtop)))


def trapez(y,y0,w):
    """Function used in weighted_lines"""
    return np.clip(np.minimum(y+1+w/2-y0, -y+1+w/2+y0),0,1)


def weighted_line(r0, c0, r1, c1, w, rmin=0, rmax=np.inf):
    """Calculates the points of a line between the two given points"""

    # The algorithm below works fine if c1 >= c0 and c1-c0 >= abs(r1-r0).
    # If either of these cases are violated, do some switches.
    if abs(c1-c0) < abs(r1-r0):
        # Switch x and y, and switch again when returning.
        xx, yy, val = weighted_line(c0, r0, c1, r1, w, rmin=rmin, rmax=rmax)
        return (yy, xx, val)

    # At this point we know that the distance in columns (x) is greater
    # than that in rows (y). Possibly one more switch if c0 > c1.
    if c0 > c1:
        return weighted_line(r1, c1, r0, c0, w, rmin=rmin, rmax=rmax)

    # The following is now always < 1 in abs
    slope = (r1-r0) / (c1-c0)

    # Adjust weight by the slope
    w *= np.sqrt(1+np.abs(slope)) / 2

    # We write y as a function of x, because the slope is always <= 1
    # (in absolute value)
    x = np.arange(c0, c1+1, dtype=float)
    y = x * slope + (c1*r0-c0*r1) / (c1-c0)

    # Now instead of 2 values for y, we have 2*np.ceil(w/2).
    # All values are 1 except the upmost and bottommost.
    thickness = np.ceil(w/2)
    yy = (np.floor(y).reshape(-1,1) + np.arange(-thickness-1,thickness+2).reshape(1,-1))
    xx = np.repeat(x, yy.shape[1])
    vals = trapez(yy, y.reshape(-1,1), w).flatten()

    yy = yy.flatten()

    # Exclude useless parts and those outside of the interval
    # to avoid parts outside of the picture
    mask = np.logical_and.reduce((yy >= rmin, yy < rmax, vals > 0))

    return (yy[mask].astype(int), xx[mask].astype(int), vals[mask])


def draw_segment(img, p1, p2):
    """Draw a segment between the given two points"""

    linecolor = 255 # TODO color
    # Draw the segment to the image
    (xx, yy, val) = weighted_line(p1[0], p1[1], p2[0], p2[1], 0)
    img[xx, yy] = linecolor

    # pad the array to 3D - later might be needed
    #img = np.dstack([img]*3)


def draw_line(img, line):
    """ Draws the line( / broken line) on img
        img: image to draw on
        line: Line object
    """

    # Calls draw_segment with each segment
    for i in range(1, len(line.points)):
        draw_segment(img, line.points[i-1], line.points[i])


#######################################################
#                       TESTS                         #
#######################################################

# TEST 1
points1 = [[0, 0], [30, 20], [0, 40], [60, 10]]
sign = 1
line1 = Line(points1, sign)
x = 100
y = 100
img = np.zeros((x,y))

draw_line(img, line1)
fig, ax = plt.subplots()
ax.imshow(img, cmap='gray',interpolation='nearest', origin='upper')

plt.show()

# TEST 2
img2 = mpimg.imread('lena.jpg')
print(img2[10:20, 40:50])
draw_line(img2, line1)
fig2, ax2 = plt.subplots()
ax2.imshow(img2,cmap='gray', interpolation='nearest', origin='upper')

plt.show()
