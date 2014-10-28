from decimal import Decimal
from decimal import getcontext
import logging


logger = logging.getLogger(__name__)


def demo():

    z = 0.1 + 0.1 + 0.1 - 0.3
    print z

    x = Decimal(0.1)
    y = Decimal(0.3)
    getcontext().prec = 2
    z = x + x + x - y
    print "Decimal:" + str(z)
