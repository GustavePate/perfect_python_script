from decimal import Decimal
from decimal import getcontext
import logging


logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** Decimal demo *******")

        z = 0.1 + 0.1 + 0.1 - 0.3
        logger.info(z)

        x = Decimal(0.1)
        y = Decimal(0.3)
        getcontext().prec = 2
        z = x + x + x - y
        logger.info("Decimal:" + str(z))

    except Exception:
        res = False
        logger.exception("Decimal demo failed")
        raise
    else:
        res = True
    finally:
        return res
