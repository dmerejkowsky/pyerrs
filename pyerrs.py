from __future__ import print_function

def print_error(func):
    try:
        func()
    except Exception as e:
        print(e)


def syntax_error(code):
    try:
        exec(code)
    except Exception as e:
        print(e.msg)


syntax_error("""
print hello
""")


@print_error
def bad_str():
    class BadStr():
        def __str__(self):
            return 42

    str(BadStr())

@print_error
def bad_args_1():
    def foo(x, a=2, b=3):
        pass
    foo(42, 43, 44, 45)

@print_error
def bad_args_2():
    def foo(x, a=2, b=3):
        pass
    foo()

@print_error
def bad_args_3():
    def foo():
        pass
    foo(42)

@print_error
def bad_args_4():
    def foo(a, b):
        pass
    foo(42)

@print_error
def bad_args_5():
    def foo(a, b=None):
        pass

    foo(42, c=None)

@print_error
def bad_init():
    class BadInit():
        def __init__(self):
            return 42

    BadInit()

@print_error
def wrong_exception_type():
    raise 42


@print_error
def bad_unpack():
    a, b = (1, 2, 3)
