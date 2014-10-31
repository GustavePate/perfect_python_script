# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tempfile
import logging

logger = logging.getLogger(__name__)


def demo(test_str='blabla'):

    temp = tempfile.TemporaryFile()
    try:
        temp.write(test_str)
        temp.seek(0)
        res = temp.read()
        logger.info(res)
    finally:
        temp.close()
        return res
