# encoding: utf-8
""" Parameterized decorator for catching errors and displaying them in an error popup """
from enum import Enum
import npyscreen


class DialogType(Enum):
    """
    Enum defining the type of dialog.

    CONFIRM - the dialog waits until the user clicks OK
    BRIEF - the dialog appears for a few seconds and then vanishes
    """
    CONFIRM = npyscreen.notify_confirm
    BRIEF = npyscreen.notify_wait


# PythonDecorators/decorator_function_with_arguments.py
def error_handler(title, dialog_type=DialogType.CONFIRM):
    """
    Decorator for functions to catch their exceptions and display them in an error popup

    :param title The title of the error pop-up
    :param dialog_type A DialogType enum
    """
    def wrap(original_function):
        def wrapped_f(*args):
            try:
                return original_function(*args)
            except Exception as ex:  # pylint: disable=broad-except
                dialog_type(str(ex), title)
                return None
        return wrapped_f
    return wrap
