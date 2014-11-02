# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import sqlite3
import os
from pps.utils.configuration import ConfBorg


logger = logging.getLogger(__name__)


def demo(rownumber=10000):

    res = False
    try:

        logger.info("****** SQLLite demo *******")

        borg = ConfBorg()
        db_filename = os.path.join(borg.conf['data_path'], "sqllite.db")

        # drop db if exists
        if os.path.exists(db_filename):
            os.remove(db_filename)

        # create db
        conn = sqlite3.connect(db_filename)
        cur = conn.cursor()

        # log version
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        logger.info("SQLite version: " + str(data[0]))

        # create a table
        cur.execute('''CREATE TABLE inc (value integer)''')
        conn.commit()

        # insert 10.000 rows
        for i in range(1, rownumber + 1):
            # takes a sequence as input
            cur.execute("INSERT INTO inc VALUES (?)", (i,))

        conn.rollback()

        to_insert = []
        for i in range(1, rownumber + 1):
            # takes a list of sequence as input
            to_insert.append((i,))
        cur.executemany("INSERT INTO inc VALUES (?)", to_insert)

        conn.commit()

        # select sum() rows
        cur.execute('SELECT sum(value) from inc')
        data = cur.fetchone()
        logger.info("Sum value in table: " + str(data[0]))

        # select each 10000 rows
        for i, row in enumerate(cur.execute('SELECT value from inc'), start=1):
            if ((i % 1000) == 0):
                logger.info(row)

        # count row number
        nbrows = i
        logger.info('nb rows: ' + str(nbrows))

        # drop db if exists
        if os.path.exists(db_filename):
            os.remove(db_filename)

        # return row number
        res = nbrows

    except Exception:
        logger.exception("SQLLite demo failed")
        raise

    finally:
        return res
