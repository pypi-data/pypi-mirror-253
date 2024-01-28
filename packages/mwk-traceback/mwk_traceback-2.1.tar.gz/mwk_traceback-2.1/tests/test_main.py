
def func_func_func():
    x = 1 / 0


def func_func():
    try:
        func_func_func()
    except Exception as exc:
        raise AttributeError('error in func_func') from exc


def func():
    try:
        func_func()
    except Exception as exc:
        raise NameError('error in func') from exc


def main():

    func()

if __name__ == '__main__':
    # from mwk_traceback import compact_tb
    # compact_tb.activate()
    # main()

    from mwk_traceback import super_compact_tb
    super_compact_tb.activate()
    main()