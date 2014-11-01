# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pps.demos.demo_decimal as demo_decimal
import pytest
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("initloggers")
def test_module(confborg):
    try:
        res = demo_decimal.demo()
        assert res == Decimal(0)
        assert res ==  0
    except Exception:
        logger.exception("Exception!!")
        assert False
