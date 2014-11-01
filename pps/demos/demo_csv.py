# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import logging
from pps.utils.configuration import ConfBorg
import os
import tempfile

logger = logging.getLogger(__name__)


def demo():

    res = False
    try:

        logger.info("****** csv demo *******")

        borg = ConfBorg()
        data_path = borg.conf.get("data_path")
        filename = os.path.join(data_path, 'opendata2.csv')

        ouput_rows = []

        # Read a file
        with open(filename, 'r') as f:
            dia = csv.Sniffer().sniff(f.read(1024))
            f.seek(0)
            reader = csv.DictReader(f, dialect=dia)
            try:
                for row in reader:
                    # pass everything in utf-8
                    unirow =  row
                    logger.info(unirow)
                    ouput_rows.append(unirow)
                    if reader.line_num > 10:
                        break

            except csv.Error:
                logger.exception('file %s, line %d: %s' % (filename, reader.line_num))
                raise
            except Exception:
                raise

        # Write a file
        temp_csv = tempfile.TemporaryFile(mode='w+t')

        field_names = ouput_rows[-1]
        field_names = field_names.keys()

        try:
            dictwriter = csv.DictWriter(temp_csv, fieldnames=field_names, dialect=dia)
            dictwriter.writeheader()
            dictwriter.writerows(ouput_rows)

            res = []
            temp_csv.seek(0)
            for l in temp_csv:
                logger.info(l.strip())
                res.append(l.strip())

        finally:
            temp_csv.close()

    except Exception:
        res = False
        logger.exception("Csv demo failed")
    finally:
        return res
