# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import namedtuple
import logging


logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** Named tuples demo *******")

        Point = namedtuple('Point', 'x, y')

        i = Point(1, 2)
        logger.info(i)
        logger.info(i.x)
        logger.info("x value: %s", i.x)

        j = Point(y=6, x=5)
        x, y = j
        logger.info(str((x, y)))

    except Exception:

        logger.exception("Named tuples demo failed")
        raise

    else:
        res = True

    finally:
        return res
