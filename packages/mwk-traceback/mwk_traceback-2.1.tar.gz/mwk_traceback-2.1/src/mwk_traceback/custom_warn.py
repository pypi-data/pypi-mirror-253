from pathlib import Path


class CustomWarningFormatter:
    """
    Helper class for formatting custom warning message
    """

    _WARN_FORMAT = 'Warning in [{file}.py] at line ({line})\n   >> {type}: {message}\n'

    def __new__(cls, message, category, filename, lineno, line=None):
        warn_dict = dict(message=message,
                         type=category.__name__,
                         file=Path(filename).stem,
                         line=str(lineno))
        return cls._WARN_FORMAT.format(**warn_dict)
