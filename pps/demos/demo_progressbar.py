#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import click


def demo():
    # click progressbar demo
    with click.progressbar([None] * 100, label='Beautifull progress bar') as bar:
        for i in bar:
            time.sleep(0.002)
