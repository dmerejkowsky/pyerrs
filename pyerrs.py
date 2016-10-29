from __future__ import print_function

def print_err(func):
    try:
        func()
    except Exception as e:
        print(e)


@print_err
def bad_args():
    def two_args(a, b):
        pass
    two_args(42)


@print_err
def no_self_in_param():
    class Foo(object):
        def no_self():
            pass

    foo = Foo()
    foo.no_self()


@print_err
def print_bad_str():

    class BadStr():
        def __str__(self):
            return 42

    print(BadStr())


@print_err
def bad_init():
    class BadInit():
        def __init__(self):
            return 42

    BadInit()


@print_err
def wrong_exception_type():
    raise 42


@print_err
def bad_kwarg():
    def foo(a, b=None):
        pass

    foo(42, c=None)
