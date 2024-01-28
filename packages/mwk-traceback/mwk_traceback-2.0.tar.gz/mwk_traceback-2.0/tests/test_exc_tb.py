import sys

from mwk_traceback import compact_tb as c_tb
from mwk_traceback import super_compact_tb as sc_tb
from test_main import main


def test_chain():
    test_prints = (c_tb, sc_tb)
    for t in test_prints:
        try:
            main()
        except Exception as exc:
            t.print_exception(exc)

    # sys.excepthook = c_tb.exception_hook
    # main()

    sys.excepthook = sc_tb.exception_hook
    main()

