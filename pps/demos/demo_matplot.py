# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** Matplot demo *******")

        # get a date axis
        x = pd.date_range('1/1/2015', periods=72, freq='H')
        y = np.arange(72)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))

        # date x axis tuning: every 4 hours
        # loc = mdates.HourLocator(interval=4)

        # date x axis tuning: full auto (between x and y tick, be regular and go !)
        loc = mdates.AutoDateLocator(minticks=4, maxticks=16, interval_multiples=True)
        plt.gca().xaxis.set_major_locator(loc)

        # plot
        plt.plot(x, y)
        plt.gcf().autofmt_xdate()
        plt.show()

    except Exception:
        logger.exception("Matplot demo failed")
        raise

    else:
        res = True

    finally:
        return res
