# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pps.demos.demo_named_tuples as demo_named_tuples
import pytest


@pytest.mark.usefixtures("initloggers")
def test_module():
    try:
        res = demo_named_tuples.demo()
    except Exception:
        res = False
    assert res
