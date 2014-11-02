# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging


logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** Template demo *******")

    except Exception:
        logger.exception("Template demo failed")
        raise

    else:
        res = True

    finally:
        return res
