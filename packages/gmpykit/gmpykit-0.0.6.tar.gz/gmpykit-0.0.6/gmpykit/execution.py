from IPython.core.magic import register_cell_magic
import threading

def deco_interval(sec=3600):
    def inner(fct):
        def wrapper(*args, **kwargs):
            set_interval(fct, sec, args, kwargs)
        return wrapper
    return inner

def set_interval(func, sec, *args, **kwargs):
    def func_wrapper():
        set_interval(func, sec)
        func(*args, **kwargs)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


@register_cell_magic
def magic_run(line, cell):
    if eval(line):
        get_ipython().ex(cell)
    else:
        print("Cell execution skipped by run magic.")
