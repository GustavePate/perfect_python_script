# -*- coding: utf-8 -*-
import pps.demos.demo_csv as demo_csv
import pytest


@pytest.mark.usefixtures("initloggers")
def test_module(confborg):
    try:
        res = demo_csv.demo()
        assert len(res) == 11
    except Exception:
        assert False
