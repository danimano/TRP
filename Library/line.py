import numpy as np

# TODO: sign unused, do we need it?

class Line:
    # Each column contains the coordinates of a non-zero element
    points = []
    # Sign is unused so far
    sign = -1

    def __init__(self, _points=[], _sign=-1):
        self.points = _points
        self.sign = _sign



# TODO test