import pps.demos.demo_decimal as demo_decimal


def test_module():
    try:
        res = demo_decimal.demo()
    except Exception:
        res = False
    assert res
