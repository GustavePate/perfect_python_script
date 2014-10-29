import ppb.demos.demo_named_tuples as demo_named_tuples


def test_module():
    try:
        res = demo_named_tuples.demo()
    except Exception:
        res = False
    assert res
