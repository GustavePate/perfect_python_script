# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import matplotlib.dates as mdates

import numpy as np
np.random.seed(9221999)
import pandas as pd
from scipy import stats, optimize
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette="Set2")


logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** Seaborn  demo *******")

        def random_walk(n, start=0, p_inc=.2):
            return start + np.cumsum(np.random.uniform(size=n) < p_inc)

        starts = np.random.choice(range(4), 10)
        probs = [.1, .3, .5]
        walks = np.dstack([[random_walk(15, s, p) for s in starts] for p in probs])

        print(walks)
        fig = sns.tsplot(walks)
        plt.show()

    except Exception:
        logger.exception("Seaborn demo failed")
        raise

    else:
        res = True

    finally:
        return res
