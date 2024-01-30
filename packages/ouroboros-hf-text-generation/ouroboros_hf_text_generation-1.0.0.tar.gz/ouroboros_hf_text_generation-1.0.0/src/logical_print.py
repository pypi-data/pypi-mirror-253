from rich import print as rpirnt
from datetime import datetime

class logical_print():
    def __init__(self) -> None:
        self.first_instance = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        
    def lprint(self, level : str , error_type : str = None, c_class : str | None = None, func : str | None = None, line : int = 0, msg : str = ''):
        if level == 'FATAL':
            if c_class is None and func:
                rpirnt(f'[bold #ea1d3b][FATAL][{error_type}][bold #ffcc00][Func {func}()][bold #ea1d3b](Line {line}): {msg}')
            if c_class and func:
                rpirnt(f'[bold #ea1d3b][FATAL][{error_type}][bold #cd00cd][Class <{c_class}>][bold #ffcc00][Func {func}()][bold #ea1d3b](Line {line}): {msg}')
            if func is None and c_class:
                rpirnt(f'[bold #ea1d3b][FATAl][{error_type}][bold #cd00cd][Class <{c_class}>][bold #ea1d3b](Line {line}): {msg}')
            if not c_class:
                if not func:
                    rpirnt(f'[bold #ea1d3b][FATAl][{error_type}](Line {line}): {msg}')
                    
        
        if level == 'WARN':
            if c_class is None and func:
                rpirnt(f'[bold #d95914][FATAL][{error_type}][bold #ffcc00][Func {func}()][bold #d95914](Line {line}): {msg}')
            if c_class and func:
                rpirnt(f'[bold #d95914][FATAL][{error_type}][bold #cd00cd][Class <{c_class}>][bold #ffcc00][Func {func}()][bold #d95914](Line {line}): {msg}')
            if func is None and c_class:
                rpirnt(f'[bold #d95914][FATAl][{error_type}][bold #cd00cd][Class <{c_class}>][bold #d95914](Line {line}): {msg}')
            if not c_class:
                if not func:
                    rpirnt(f'[bold #d95914][FATAl][{error_type}](Line {line}): {msg}')
                    
        if level == 'OK':
            if c_class is None and func:
                rpirnt(f'[bold #14d959][SUCCESS][bold #ffcc00][Func {func}()][bold #14d959](Line {line}): {msg}')
            if c_class and func:
                rpirnt(f'[bold #14d959][SUCCESS][bold #cd00cd][Class <{c_class}>][bold #ffcc00][Func {func}()][bold #14d959](Line {line}): {msg}')
            if func is None and c_class:
                rpirnt(f'[bold #14d959][SUCCESS][bold #cd00cd][Class <{c_class}>][bold #14d959](Line {line}): {msg}')
            if not c_class:
                if not func:
                    rpirnt(f'[bold #14d959][SUCCESS](Line {line}): {msg}')