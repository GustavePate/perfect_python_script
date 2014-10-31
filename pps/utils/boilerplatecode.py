#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import logging
from utils.configuration import ConfBorg
import sys

logger = logging.getLogger(__name__)


def script_init(cli_args):
    """
    - will initialize a ConfBorg object containing cli arguments, configutation file elements
    - will initialize loggers
    """

    # compute log file absolute path
    pathname = os.path.dirname(sys.argv[0])
    full_path = os.path.abspath(pathname)
    log_conf_path = os.path.join(full_path, "..", "ressources", "conf", 'logging.json')
    data_path = os.path.join(full_path, "..", "ressources", "data")

    # append path to configuration
    cli_args['data_path'] = data_path
    cli_args['full_path'] = full_path

    # read log configuration
    if os.path.exists(log_conf_path):
        with open(log_conf_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        # default value
        logging.basicConfig(level=logging.INFO)

    logger.info("................init...............")
    # read application configuration
    conf_path = os.path.join(full_path, "..", "ressources", "conf", 'conf.json')
    if os.path.exists(conf_path):
        with open(conf_path, 'rt') as f:
            conf = json.load(f)

    # initialize conf with items loaded from conf file AND command lines arguments
    # cli args have priority over configuration file
    z = dict(conf.items() + cli_args.items())
    borg = ConfBorg(z)
    logger.info(".......loaded configuration: ")
    logger.info(borg.pretty)
