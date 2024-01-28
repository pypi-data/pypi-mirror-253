# Custom exception and warning formatter [![PyPI](https://img.shields.io/pypi/v/mwk-traceback)](https://pypi.org/project/mwk-traceback/) 

---

## Exceptions
### Define exception format by subclassing **CustomTraceback**
```python
class MyTracebackFormatter(CustomTraceback):
    _EXC_FORMAT = '| {traceback}>> {type}: {exception}.\n'
    _TB_FORMAT = '[{file}::{func}]@{line} "{code}" | '
    _EXC_HOOK_HEAD_TEXT = 'Error:'
```
*1. **_EXC_FORMAT** used for formatting single exception in exceptions chain:*  
**_EXC_FORMAT** should be *python formatted string literal* with values in **{}** brackets.
Available values for **_EXC_FORMAT** *formatted string literal*:
- **traceback**: formatted traceback goes here (see below)
- **type**: exception class name
- **exception**: exception message  

*2. **_TB_FORMAT** used for formatting single traceback frame in traceback chain:*  
**_TB_FORMAT** should be *python formatted string literal* with values in **{}** brackets.
Available values for **_TB_FORMAT** *formatted string literal*:
- **file**: python .py file stem where error occurred
- **func**: function or module where error occurred
- **line**: number of the line of code where error occurred  
- **code**: line of code itself

*3. **_EXC_HOOK_HEAD_TEXT** used as header for exceptions*  
**_EXC_HOOK_HEAD_TEXT** should be python string

*4. Additional variables to define:*
- **_EXC_OUT**: output for exceptions, **sys.stderr**  by default
- **_EXC_CHAIN**: **True** - chain exceptions, **False** - only last exception, by default **True**
- **_EXC_REVERSE**: order of chained exceptions, **True** - show like default python exception hook, by default **False**
### Usage:
1. Definition
```python
class MyTracebackFormatter(CustomTraceback):
    _TB_FORMAT = '[{file}::{func}]@{line} "{code}" | '
    _EXC_FORMAT = '| {traceback}>> {type}: {exception}.\n'
    _EXC_HOOK_HEAD_TEXT = 'Error:'
    _EXC_OUT = sys.stderr
    _EXC_CHAIN = True
    _EXC_REVERSE = False
```
2. Get formatted exception string
```python
exc_str = MyTracebackFormatter(exc)
```
3. Print formatted exception
```python
MyTracebackFormatter.print_exception(exc)
```
4. Use **actvate()** method to alter way of presenting tracebacks for system, modules(i.e. logging) and apps:
```python
MyTracebackFormatter.activate()
```
It is equivalent of executing these statements:
```python
sys.excepthook = MyTracebackFormatter.exception_hook
traceback.print_exception = MyTracebackFormatter.traceback_print_exception_hook
traceback.format_exception = MyTracebackFormatter.traceback_format_exception_hook
```
### Predefined traceback formatters
1. **compact_tb**
```python
from mwk_traceback import compact_tb

compact_tb.activate()

main()  # ! check test_main.py for code !
test_tb_pr_exc()  # ! check test_traceback_print_exception.py for code !
```
Output:
```commandline
! Error(s):
| Error in [test_main.py] in [<module>] at line (27) while executing "main()"
| Error in [test_main.py] in [main] at line (22) while executing "func()"
| Error in [test_main.py] in [func] at line (17) while executing "raise"
   >> NameError: error in func.
| Error in [test_main.py] in [func] at line (15) while executing "func_func()"
| Error in [test_main.py] in [func_func] at line (10) while executing "raise"
   >> AttributeError: error in func_func.
| Error in [test_main.py] in [func_func] at line (8) while executing "func_func_func()"
| Error in [test_main.py] in [func_func_func] at line (3) while executing "x = 1 / 0"
   >> ZeroDivisionError: division by zero.
 ----------------------------------------------------------------------------------------------------------  
ERROR:root:logging error
ERROR:root:logging exception
| Error in [test_traceback_print_exception.py] in [test_tb_pr_exc] at line (13) while executing "x = 1 / 0"
   >> ZeroDivisionError: division by zero.

ERROR:root:There was no exception
No exception is being handled.
```
2. **super_compact_tb**
```python
from mwk_traceback import super_compact_tb

super_compact_tb.activate()

main()  # ! check test_main.py for code !
test_tb_pr_exc()  # ! check test_traceback_print_exception.py for code !
```
Output:
```commandline
! Error:
| [test_main::<module>]@31 "main()" | [test_main::main]@22 "func()" | [test_main::func]@17 "raise" | >> NameError: error in func.
| [test_main::func]@15 "func_func()" | [test_main::func_func]@10 "raise" | >> AttributeError: error in func_func.
| [test_main::func_func]@8 "func_func_func()" | [test_main::func_func_func]@3 "x = 1 / 0" | >> ZeroDivisionError: division by zero.
 ----------------------------------------------------------------------------------------------------------
ERROR:root:logging error
ERROR:root:logging exception
| [test_traceback_print_exception::test_tb_pr_exc]@14 "x = 1 / 0" | >> ZeroDivisionError: division by zero.

ERROR:root:There was no exception
No exception is being handled
```
## Warnings
### Define warning format by subclassing **CustomWarningFormatter**:
```python
class MyWarningFormatter(CustomWarningFormatter):
    _WARN_FORMAT = '[{file}]@{line} >> {type}: {message}\n'
```
**_WARN_FORMAT** should be *python formatted string literal* with values in **{}** brackets.  
Available values for **_WARN_FORMAT** *formatted string literal*:
- **message**: warning message
- **type**: warning class name
- **file**: python .py file stem where warning occurred
- **line**: number of the line of code where warning occurred
### Usage:
```python
import warnings
warnings.formatwarning = MyWarningFormatter

warnings.warn('This is warning', UserWarning)
```
### Predefined warning formatters (classes)
1. **compact_warn**
```python
import warnings
from mwk_traceback import compact_warn
warnings.formatwarning = compact_warn

warnings.warn('This is warning', RuntimeWarning)
```
Output:
```commandline
Warning in [test_warn.py] at line (9)
   >> RuntimeWarning: This is warning
```
2. **super_compact_warn**
```python
import warnings
from mwk_traceback import super_compact_warn
warnings.formatwarning = super_compact_warn

warnings.warn('This is another warning', UserWarning)
```
Output:
```commandline
[test_warn]@13 >> UserWarning: This is another warning
```

