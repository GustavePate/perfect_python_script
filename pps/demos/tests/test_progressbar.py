# -*- coding: utf-8 -*-
import pps.demos.demo_progressbar as demo_progressbar
import pytest


@pytest.mark.usefixtures("initloggers")
def test_module():
    try:
        res = demo_progressbar.demo()
    except Exception:
        res = False
    assert res
