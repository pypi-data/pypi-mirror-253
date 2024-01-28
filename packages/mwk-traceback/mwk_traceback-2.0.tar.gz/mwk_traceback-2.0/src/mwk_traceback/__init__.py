from .custom_exc_tb import CustomTraceback
from .custom_warn import CustomWarningFormatter

__version__ = '2.0'

__all__ = ('compact_tb', 'super_compact_tb', 'compact_warn', 'super_compact_warn',
           'CustomTraceback', 'CustomWarningFormatter')


class SuperCompactTraceback(CustomTraceback):
    _TB_FORMAT = '[{file}::{func}]@{line} "{code}" | '
    _EXC_FORMAT = '| {traceback}>> {type}: {exception}.\n'
    _EXC_HOOK_HEAD_TEXT = '! Error:'


compact_tb = CustomTraceback
super_compact_tb = SuperCompactTraceback


class SuperCompactWarningFormatter(CustomWarningFormatter):
    _WARN_FORMAT = '[{file}]@{line} >> {type}: {message}\n'


compact_warn = CustomWarningFormatter
super_compact_warn = SuperCompactWarningFormatter
