# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import os
from PIL import Image
from pps.utils.configuration import ConfBorg

logger = logging.getLogger(__name__)


def demo(size=(200, 200)):

    res = None
    logger.info("****** Pillow demo *******")

    try:
        borg = ConfBorg()
        infile = os.path.join(borg.conf['data_path'], 'why.jpg')
        outfile = os.path.splitext(infile)[0] + ".thumbnail.jpg"

        if os.path.exists(outfile):
            os.remove(outfile)

        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size)
                im.save(outfile, "JPEG")
            except IOError:
                logger.exception("cannot create thumbnail for" + infile)
                raise
        res = outfile
        logger.info(res + "created")

    except Exception:
        logger.exception("Pillow demo failed")
    finally:
        return res
