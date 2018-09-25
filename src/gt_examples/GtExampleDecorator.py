import sys


def example(func):
    def func_wrapper(*args, **kwargs):
        getframe_expr = 'sys._getframe({}).f_code.co_name'
        caller = eval(getframe_expr.format(2))
        return func(*args, **kwargs)
    func_wrapper._is_example = True
    func_wrapper._original_method = func
    return func_wrapper
