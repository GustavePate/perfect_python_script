#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import logging.config
import os
import json
import sys
from demos.demo_decimal import demo as demo_decimal
from pprint import pformat


logger = logging.getLogger(__name__)


def main(args):

    ERROR = False

    # compute log file absolute path
    pathname = os.path.dirname(sys.argv[0])
    full_path = os.path.abspath(pathname)
    log_conf_path = os.path.join(full_path, "..", "ressources", "conf", 'logging.json')

    # read log configuration
    if os.path.exists(log_conf_path):
        with open(log_conf_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        # default value
        logging.basicConfig(level=logging.INFO)

    logger.info("................start...............")

    # read applictaion configuration
    conf_path = os.path.join(full_path, "..", "ressources", "conf", 'conf.json')
    if os.path.exists(conf_path):
        with open(conf_path, 'rt') as f:
            conf = json.load(f)

    logger.info("conf: ")
    logger.info(pformat(conf))
    logger.info("args: " + str(args))

    try:

        demo_decimal()

        Point = namedtuple('Point', 'x, y')

        i = Point(1, 2)
        logger.info(i)
        logger.info("x value: %s", i.x)
        j = Point(y=6, x=5)
        x, y = j
        # x = 10 / 0

    except Exception:
        logger.exception('Failed to run batch')
        ERROR = True
    else:
        logger.info("Sucess !!!")

    finally:
        if ERROR:
            logger.error("..............script ended with errors...............")
        else:
            logger.info("...............script successfully ended..............")


if __name__ == '__main__':
    main(sys.argv)
