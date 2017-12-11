import numpy as np

# get an array. Each column contains the coordinates of a non-zero element

class Line_coords:
    points = []
    sign = -1

    def __init__(self, _points=[], _sign=-1):
        self.points = _points
        self.sign = _sign