from collections import namedtuple


def demo():

    Point = namedtuple('Point', 'x, y')

    i = Point(1, 2)
    print i
    print i.x

    j = Point(y=6, x=5)
    x, y = j
    print x, y
