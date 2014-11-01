# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pps.demos.demo_decimal as demo_decimal
import pytest


@pytest.mark.usefixtures("initloggers")
def test_module(confborg):
    try:
        print " "
        res = demo_decimal.demo()
    except Exception:
        res = False
    assert res
