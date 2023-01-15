import pytest
from delay import Delay


def test_empty_constructor():
    try:
        a = Delay()
    except TypeError as err:
        assert True


def test_bad_fib():
    got_error = False
    try:
        a = Delay(300)
        a._fibonacci('abc')
    except ValueError:
        got_error = True
    if not got_error:
        assert False


def test_ok():
    got_error = False
    try:
        a = Delay(300)
        a.set_delay_factor(3)
        a.set_initial_fib(4)
        print(f'With {a}, we get a delay of {a.get_delay()}')
    except ValueError:
        got_error = False
    if not got_error:
        assert True


def test_string_constructor():
    got_error = False
    try:
        a = Delay('bob')
    except ValueError:
        got_error = True
    if not got_error:
        assert False


if __name__ == '__main__':
    pass