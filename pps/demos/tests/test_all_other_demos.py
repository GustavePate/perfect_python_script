# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import logging
import os


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("initloggers")
class TestClass:

    def test_template(self):
        try:
            assert True
        except Exception:
            logger.exception("Exception !!!")
            assert False

    def test_pillow(self, confborg):

        import pps.demos.demo_pillow as demo_pillow
        from PIL import Image

        try:
            res = demo_pillow.demo((100, 100))
            assert res is not None
            im = Image.open(res)
            assert im.size == (100, 100)
            os.remove(res)
        except Exception:
            logger.exception("Exception !!!")
            assert False
