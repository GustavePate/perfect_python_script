#!/usr/bin/python
# -*- coding: utf-8 -*-
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
        getcontext().prec = 0
        z = x + x + x - y
        logger.info("Decimal:" + str(z))
        res = z
    except Exception:
        res = False
        logger.exception("Decimal demo failed")
    finally:
        return res
