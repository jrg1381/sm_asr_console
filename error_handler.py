# encoding: utf-8
import npyscreen
from enum import Enum


class DialogType(Enum):
    CONFIRM = npyscreen.notify_confirm
    BRIEF = npyscreen.notify_wait


# PythonDecorators/decorator_function_with_arguments.py
def error_handler(title, dialog_type=DialogType.CONFIRM):
    def wrap(f):
        def wrapped_f(*args):
            try:
                return f(*args)
            except Exception as e:
                dialog_type(str(e), title)
                return None
        return wrapped_f
    return wrap 