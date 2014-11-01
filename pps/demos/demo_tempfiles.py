# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tempfile
import logging

logger = logging.getLogger(__name__)


def demo(test_str='blabla'):

    res =  None
    try:

        logger.info("****** tempfiles *******")

        temp = tempfile.TemporaryFile()
        temp.write(test_str.encode('utf-8'))
        temp.seek(0)
        res = temp.read()
        res = res.decode('utf-8')
        logger.info(res)

    except Exception:
        logger.exception("tempfiles demo failed")
        raise

    finally:
        temp.close()
        return res
