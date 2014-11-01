# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tempfile
import logging

logger = logging.getLogger(__name__)


def demo(test_str=u'blabla'):

    res =  None
    try:

        logger.info("****** tempfiles *******")

        temp = tempfile.TemporaryFile()
        temp.write(bytes(test_str))
        temp.seek(0)
        res = temp.read()
        logger.info(res)

    except Exception:
        logger.exception("tempfiles demo failed")
        raise

    finally:
        temp.close()
        return res
