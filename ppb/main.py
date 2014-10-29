#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging.config
import os
import json
import sys
import click
import demos.demo_decimal as demo_decimal
import demos.demo_named_tuples as demo_named_tuples
from utils.Configuration import ConfBorg
from pprint import pformat


logger = logging.getLogger(__name__)


@click.command()
@click.option('--verbose', default=1, help='Program verbosity.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def main(verbose, name):

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

    logger.info("................init...............")

    # read applictaion configuration
    conf_path = os.path.join(full_path, "..", "ressources", "conf", 'conf.json')
    if os.path.exists(conf_path):
        with open(conf_path, 'rt') as f:
            conf = json.load(f)

    logger.info("conf: ")
    borg = ConfBorg(conf)
    logger.info(pformat(borg.conf))
    logger.info("args: " + str(sys.argv))

    logger.info("................start...............")
    try:

        demo_decimal.demo()
        demo_named_tuples.demo()

    except Exception:
        logger.exception('Failed to run batch')
        ERROR = True
    else:
        logger.debug("Sucess !!!")

    finally:
        if ERROR:
            logger.error("..............script ended with errors...............")
        else:
            logger.info("...............script successfully ended..............")

if __name__ == '__main__':
    main()
