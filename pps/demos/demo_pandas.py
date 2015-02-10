# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import pandas as pd
import pandas.stats.moments as stat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pps.utils.configuration import ConfBorg
import os
from datetime import datetime

logger = logging.getLogger(__name__)


def super_date_parser(datestr):
    dt = datetime.strptime(datestr, '%d/%b/%Y:%H:%M:%S')
    return dt


def demo():

    res = False
    try:
        borg = ConfBorg()
        logger.info("****** Pandas demo *******")
        # s = pd.Series([1, 3, 5, np.nan, 6, 8])
        infile = os.path.join(borg.conf['data_path'], 'access.csv')
        df = pd.read_csv(
            infile,
            sep=';',
            # header index
            header=0,
            # date parser
            date_parser=super_date_parser,
            # limit nb line to read
            # nrows=8000,
            # which column to parse (based on column name)
            parse_dates=['date']
            )
        print('###### head')
        print(df.head())
        serie1 = df.loc[0]
        print serie1

        # get size
        df_data_size = df.data_size
        print df_data_size

        #################################
        # OP on data of the same type
        #################################

        # transpose to series
        serie_data_size = df_data_size.T
        # same dat in a serie == mathematical operation allowed
        print(serie_data_size.mean())
        print(serie_data_size.describe())
        # somme cumulée
        print(serie_data_size.cumsum().tail(1))

        #  call number / date

        # keep just relevant data (date + data_size)

        df2 = df[['date', 'data_size']]
        print(df2.head())
        # group by
        df3 = df2.groupby('date')
        # number of call per timestamp
        df_call = df3.count()
        print (df_call)

        # sum datasize / timestamp
        df_sum = df3.sum()

        # synthax for joing on fields, here we are joining on indexes
        # df_call.merge(df_sum, how='inner', on='date')
        df_res = df_call.merge(df_sum, how='inner', left_index=True, right_index=True)
        print(df_res.head())

        # add a column to df_res per minutes range
        # col = df_res.columns
        # col.append('round_2_minutes')
        # df_res.colums = col
        # print(df_res.head())

        # rename columns
        df_res.columns = ['nb_call', 'data_size']
        print(df_res.head())

        # create a third column based on date
        # ie. remove date from index
        df_res.reset_index(level=0, inplace=True)
        print(df_res.head())

        # make a DatetimeIndex reverse of previous operation
        df_res.set_index(pd.DatetimeIndex(df_res['date']), inplace=True)
        df_res.index.names = ['DatetimeIndex']

        # df_res['round_2_minutes'] = df_res['date'].replace(second=0)
        print(df_res.head())

        # resample (millisecond) => sum per minute
        df_rs = df_res.resample('60000L', how=np.sum)
        print(df_rs.head())

        # Warn: previous op maybe inserted NaN values
        # this replace it with zeros
        df_rs.fillna(value=0)

        # Quick plotting: Naive working example
        # plot = df_rs.head(200).plot()
        # fig = plot.get_figure()
        # fig.savefig("output.png")

        # create separate df

        CUTOFF = 100000

        df_size = df_rs.loc[:, ['data_size']]
        print(df_size)
        df_call = df_rs.loc[:, ['nb_call']]

        # apply cutoff
        print(df_size)
        df_size[df_size.data_size > CUTOFF] = CUTOFF

        # compute rolling mean




        print("Plot1")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
        loc = mdates.AutoDateLocator(minticks=4, maxticks=16, interval_multiples=True)
        plt.gca().xaxis.set_major_locator(loc)
        # plot
        plt.plot(df_size.index.to_pydatetime(), df_size.data_size)
        plt.gcf().autofmt_xdate()
        plt.savefig("size.png")
        plt.close()

        print("Plot2")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
        loc = mdates.AutoDateLocator(minticks=4, maxticks=16, interval_multiples=True)
        plt.gca().xaxis.set_major_locator(loc)
        # plot
        plt.plot(df_call.index.to_pydatetime(), df_call.nb_call)
        plt.gcf().autofmt_xdate()
        plt.savefig("call.png")

        # WARNING: native pandas is VERY slow

        # plot = df_size.plot()
        # fig = plot.get_figure()
        # fig.savefig("size.png")

        # print(df.T)
        # print('###### index')
        # print(df.index)
        #
        # print('###### columns')
        # print(df.columns)
        # print('###### sort')
        # print(df.sort('size'))
        # print(df.http_code.head())
        #
        # print('#### Simple query all column for index value')
        # df2 = df.loc['20141219']
        # print(df2.head())
        #
        # print('#### Simple query one column for index value')
        # df2 = df.loc['20141219', ['http_code']]
        # print(df2.head())
        #
        # print('#### Simple query multiple column for multiple index value')
        # df2 = df.loc['20141218':'20141219', ['http_code', 'ip']]
        # print(df2)
        #
        # print('#### Simple query: 200 http code')
        # df2 = df[df.http_code == 200]
        # print(df2.head())
        #
        # print('#### Simple query: 200 and 404 http code')
        # df2 = df[df.http_code.isin([200, 201])]
        # print(df2.head(20))

    except Exception:
        logger.exception("Pandas demo failed")
        res = False
        raise

    else:
        res = True

    finally:
        return res
