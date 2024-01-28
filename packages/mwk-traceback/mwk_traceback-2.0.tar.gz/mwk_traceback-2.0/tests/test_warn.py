import warnings
from mwk_traceback import compact_warn, super_compact_warn


def test_warn():

    warnings.formatwarning = compact_warn

    warnings.warn('This is warning', RuntimeWarning)

    warnings.formatwarning = super_compact_warn

    warnings.warn('This is another warning', UserWarning)

if __name__ == '__main__':
    test_warn()
