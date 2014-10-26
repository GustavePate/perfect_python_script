from collections import namedtuple
import logging.config
import os
import json


logger = logging.getLogger(__name__)


if __name__ == '__main__':

    path = 'logging.json'
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

    try:

        logger.info("................start...............")
        Point = namedtuple('Point', 'x, y')

        i = Point(1, 2)
        logger.info(i)
        logger.info("x value: %s", i.x)
        j = Point(y=6, x=5)
        x, y = j
        x = 10 / 0

    except Exception, e:
        logger.exception('Failed to run batch')

    else:
        logger.info("Sucess !!!")

    finally:
        logger.info("................end.................")
