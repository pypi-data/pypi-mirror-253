from mwk_traceback import compact_tb as c_tb
from mwk_traceback import super_compact_tb as sc_tb


def test_one():
    test_prints = (c_tb, sc_tb)
    for t in test_prints:
        try:
            x = 1 / 0
        except Exception as exc:
            t.print_exception(exc)
