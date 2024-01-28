import sys
import traceback
from pathlib import Path
from linecache import getline
from typing import Dict, Generator, TextIO, Optional, Union
from types import TracebackType

ExceptionType = type
FrameInfo = Dict[str, str]


class CustomTraceback:
    """
    Helper class for exceptions traceback handling. Doesn't create any instances of itself!!!

    General info:
    It goes down exceptions chain and gets traceback for each exception than format string with that.

    Usage:
    CustomTraceback(exc) -> get exception formatted string
    CustomTraceback.print_exception(exc) -> print formatted exception
    CustomTraceback.exception_hook -> to be used with sys.excepthook
    """
    __slots__ = ()

    """Subclass CustomTraceback and change these variables to get another way of printing exceptions"""
    _TB_FORMAT = '| Error in [{file}.py] in [{func}] at line ({line}) while executing "{code}"\n'  # format for traceback frames
    _EXC_FORMAT = '{traceback}   >> {type}: {exception}.\n'  # format for exception in chain
    _EXC_HOOK_HEAD_TEXT = '! Error(s):'  # Header text for exception hook
    _EXC_OUT = sys.stderr  # default output for exceptions
    _EXC_CHAIN = True  # True - chain exceptions, False - only last exception
    _EXC_REVERSE = False  # order of chained exceptions, True -> show like default python exception hook

    def __new__(cls,
                exc: BaseException, *,
                chain: bool = _EXC_CHAIN,
                reverse: bool = _EXC_REVERSE) -> str:
        """
        Doesn't create instances. Returns formatted exception string.
        :param exc: exception
        :param chain: chain exceptions or not
        :param reverse: reverse order of exceptions
        :return: formatted exception string
        """
        return cls._format_exception(exc, chain=chain, reverse=reverse)

    @staticmethod
    def _get_exception_chain(exc: BaseException) -> Generator[BaseException, None, None]:
        """
        Generator for exceptions chain starting from given exception (exc)
        Need to be reversed to got most last exception at the end
        :param exc: exception
        :return: generator for exceptions chain
        """
        while True:
            yield exc
            exc = exc.__context__
            # exc = getattr(exc, '__context__', None)
            if not exc:
                break

    @staticmethod
    def _get_traceback_chain(tb) -> Generator[FrameInfo, None, None]:
        """
        Generator of traceback frames info for given traceback - as dicts
        :param tb: traceback
        :return: generator for traceback frames info
        """
        while tb is not None:
            file = tb.tb_frame.f_code.co_filename  # full file name
            file_name = Path(file).stem  # only stem of the file
            func_name = tb.tb_frame.f_code.co_name  # function name
            code_line = getline(file, tb.tb_lineno).strip()
            # if 'raise' in code skip error description, it is in the exception
            code_line = ('raise' if code_line.startswith('raise') else code_line)  # line of code
            line_no = str(tb.tb_lineno)  # line number
            yield dict(file=file_name, func=func_name, line=line_no, code=code_line)
            tb = tb.tb_next

    @classmethod
    def _format_traceback(cls, tb: TracebackType) -> str:
        """
        Format traceback string
        :param tb: traceback
        :return: formatted traceback string
        """
        tb_str = ''.join(cls._TB_FORMAT.format(**fr) for fr in cls._get_traceback_chain(tb))
        return tb_str

    @classmethod
    def _format_exception(cls,
                          exc: BaseException, *,
                          chain: bool = True, reverse: bool = False) -> str:
        """
        Format exception string
        :param exc: exception
        :param chain: chain exceptions or not
        :param reverse: reverse order of exceptions
        :return: formatted exception string
        """
        if chain:
            chain_tuple = tuple(cls._get_exception_chain(exc))
            if reverse:
                chain_tuple = reversed(chain_tuple)
        else:
            chain_tuple = (exc,)

        exc_str = ''.join(
            (cls._EXC_FORMAT.format(exception=e,
                                    type=type(e).__name__,
                                    traceback=cls._format_traceback(e.__traceback__)) for e in chain_tuple))
        return exc_str

    @classmethod
    def print_exception(cls,
                        exc: BaseException, *,
                        chain: bool = _EXC_CHAIN, reverse: False = _EXC_REVERSE, file: TextIO = _EXC_OUT) -> None:
        """
        Just print formatted exception to the given io object (stdout, stderr, ...)
        :param exc: exception
        :param chain: chain exceptions or not
        :param reverse: reverse order of exceptions
        :param file: io object file
        :return: None
        """
        print(cls._format_exception(exc, chain=chain, reverse=reverse), file=file)

    @classmethod
    def traceback_print_exception_hook(cls,
                                       exc: Union[ExceptionType, BaseException, None], /,
                                       value: Optional[BaseException], tb='', limit=None,
                                       file: TextIO = _EXC_OUT,
                                       chain: bool = _EXC_CHAIN) -> None:
        """
        Some modules and apps (logging for example) are using traceback.print_exception to show exception traceback.
        This method is to be used as traceback module print_exception method hook:
            'traceback.print_exception = CustomTraceback.traceback_print_exception_hook'
        :param exc: exception type
        :param value: exception
        :param tb: traceback - not used in this implementation
        :param limit: not used - not used in this implementation
        :param chain: chain exceptions or not
        :param file: io object file
        :return: None
        """
        if isinstance(value, BaseException):
            cls.print_exception(value, chain=chain, reverse=cls._EXC_REVERSE, file=file)
        else:
            if isinstance(exc, BaseException):
                cls.print_exception(exc, chain=chain, reverse=cls._EXC_REVERSE, file=file)
            else:
                print('No exception is being handled.\n', file=file)

    @classmethod
    def traceback_format_exception_hook(cls,
                                        exc: Union[ExceptionType, BaseException, None], /,
                                        value: Optional[BaseException], tb='', limit=None,
                                        file: TextIO = _EXC_OUT,
                                        chain: bool = _EXC_CHAIN) -> str:
        """
        This method is to be used as traceback module format_exception method hook:
            'traceback.format_exception = CustomTraceback.traceback_format_exception_hook'
        :param exc: exception type
        :param value: exception
        :param tb: traceback - not used in this implementation
        :param limit: not used - not used in this implementation
        :param chain: chain exceptions or not
        :param file: io object file
        :return: None
        """
        if isinstance(value, BaseException):
            return cls._format_exception(value, chain=chain, reverse=cls._EXC_REVERSE)
        else:
            if isinstance(exc, BaseException):
                return cls._format_exception(exc, chain=chain, reverse=cls._EXC_REVERSE)
            else:
                return 'No exception is being handled.\n'

    @classmethod
    def exception_hook(cls,
                       exc_type: ExceptionType,
                       exc_value: BaseException,
                       trace_back: TracebackType) -> None:
        """
        Method to be used as system exception hook: 'sys.excepthook = CustomTraceback.exception_hook'
        :param exc_type: sys.excepthook signature
        :param exc_value: sys.excepthook signature
        :param trace_back: sys.excepthook signature
        :return: None
        """
        print(cls._EXC_HOOK_HEAD_TEXT, file=cls._EXC_OUT)
        cls.print_exception(exc_value, chain=cls._EXC_CHAIN, reverse=cls._EXC_REVERSE, file=cls._EXC_OUT)

    @classmethod
    def activate(cls):
        sys.excepthook = cls.exception_hook
        traceback.print_exception = cls.traceback_print_exception_hook
        traceback.format_exception = cls.traceback_format_exception_hook
