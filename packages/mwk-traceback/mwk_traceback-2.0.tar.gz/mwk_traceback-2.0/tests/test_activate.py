import sys

from mwk_traceback import compact_tb as ctb
import logging
import traceback

ctb.activate()


def test_act():
    try:
        x = 1 / 0
    except Exception:
        logging.exception('[activate] logging exception')

    try:
        s = 'xxx' + 0
    except Exception as exc:
        traceback.print_exception(type(exc), exc)

    try:
        d = {}
        i = d['item']
    except Exception as exc:
        print('[activate]:', traceback.format_exception(type(exc), exc, exc.__traceback__), file=sys.stderr)


if __name__ == '__main__':
    test_act()
