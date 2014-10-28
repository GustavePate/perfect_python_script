from collections import namedtuple
import logging


logger = logging.getLogger(__name__)

def demo():

    Point = namedtuple('Point', 'x, y')

    i = Point(1, 2)
    print i
    print i.x

    j = Point(y=6, x=5)
    x, y = j
    print x, y
