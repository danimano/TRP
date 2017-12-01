class Line:
    """Class defining a (broken) line"""
    points = []
    sign = -1 # 0 or 1
    # 0 if the positive sign is to the left when you traverse the points

    def __init__(self, _points=[], _sign=-1):
        self.points = _points
        self.sign = _sign


##############################################################
#                       TESTS                                #
##############################################################
#
# line1 = Line()
# print("Line1\npoints:\n\t", line1.points, "\nsign:\n\t", line1.sign)
# print("-----------------------------------")
#
# points2 = [[1, 1], [2, 2], [3, 3]]
# sign = 1
# line2 = Line(points2, sign)
# print("Line2\n\tpoints:\n\t", line2.points, "\n\tsign:\n\t", line2.sign)
# print("-----------------------------------")
#
# line2.points[1] = [-2, -2]
# print("Line2 mod\n\tpoints:\n\t", line2.points, "\n\tsign:\n\t", line2.sign)
# print("-----------------------------------")