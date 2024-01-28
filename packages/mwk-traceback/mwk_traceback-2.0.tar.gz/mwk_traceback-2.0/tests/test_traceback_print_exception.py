import traceback
import logging
from mwk_traceback import compact_tb as c_tb
from mwk_traceback import super_compact_tb as sc_tb

traceback.print_exception = sc_tb.traceback_print_exception_hook


def test_tb_pr_exc():

    logging.error('logging error')

    try:
        x = 1 / 0
    except Exception as exc:
        logging.exception('logging exception')

    logging.exception('There was no exception')


if __name__ == '__main__':
    test_tb_pr_exc()
