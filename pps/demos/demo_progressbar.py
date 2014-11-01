#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import click
import logging


logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** Progress bar demo *******")
        # click progressbar demo
        with click.progressbar([None] * 100, label='Beautifull progress bar') as bar:
            for i in bar:
                time.sleep(0.002)

    except Exception:

        logger.exception("Progress bar demo failed")
        raise

    else:
        res = True

    finally:
        return res
