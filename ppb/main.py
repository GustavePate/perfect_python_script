#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging.config
import os
import json
import time
import sys
import click
import demos.demo_decimal as demo_decimal
import demos.demo_named_tuples as demo_named_tuples
from utils.Configuration import ConfBorg
from pprint import pformat


logger = logging.getLogger(__name__)


@click.command()
@click.option('--verbose', '-v', default=False, help='Program verbosity.')
@click.option('-m1', '--mode1', 'exclusive_mode', flag_value='mode1',
              default=True, help='functionnal mode 1, exclusive with mode 2')
@click.option('-m2', '--mode2', 'exclusive_mode', flag_value='mode2',
              help='functionnal mode 2, exclusive withe mode 1')
@click.option('-s', '--string', help='A simple string')
@click.option('-x', '--closed_choice', type=click.Choice(['md5', 'sha1']), help='a closed value choice')
@click.argument('file1', type=click.Path(resolve_path=True))
# checks file existence and attributes
# @click.argument('file2', type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False, readable=True, resolve_path=True))
def main(verbose, string, exclusive_mode, closed_choice, file1):
    """The perfect python script.

    A template and technology demonstrator
    for running really good python scripts.
    """

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

    logger.info(".......parametrers: ")
    logger.info("verbose: " + str(verbose))
    logger.info("string: " + str(string))
    logger.info("exclusive_mode: " + str(exclusive_mode))
    logger.info("closed_choice: " + str(closed_choice))
    logger.info("file1: " + str(file1))

    # read applictaion configuration
    conf_path = os.path.join(full_path, "..", "ressources", "conf", 'conf.json')
    if os.path.exists(conf_path):
        with open(conf_path, 'rt') as f:
            conf = json.load(f)

    logger.info(".......conf: ")
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
        with click.progressbar([None]*100, label='Beautifull progress bar') as bar:
            for i in bar:
                time.sleep(0.002)

        if ERROR:
            logger.error("..............script ended with errors...............")
        else:
            logger.info("...............script successfully ended..............")


if __name__ == '__main__':
    main()
