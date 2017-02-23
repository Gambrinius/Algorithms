# -*- coding: utf-8 -*-

__author__ = "Ilya Konon"
__email__ = "ilya.konon.95@gmail.com"

"""
Create an analog built-in python range / xrange function.
With one difference - your analogue should skip every third number.
"""


def my_range(stop, start=0, step=1):
    """
    this analogue of build-in func range,
    which skip every third number.
    :param stop: int value, required
    :param start: int value, default 0
    :param step: int value, default 1
    :return: generator object
    """
    if isinstance(stop, int) and isinstance(start, int) and isinstance(step, int):
        counter = 0  # to skip every third number
        i = start

        if step == 0:
            raise ValueError("step argument can not be equal to zero.")
        elif step > 0:
            while i < stop:
                counter += 1
                if counter != 3:
                    yield i
                else:
                    counter = 0
                i += step
        elif step < 0:
            while i > stop:
                counter += 1
                if counter != 3:
                    yield i
                else:
                    counter = 0
                i += step
    else:
        raise TypeError("all arguments must be integer.")


print("built-in range - %s \n" % list(range(10)))
print("my_range - %s \n" % list(my_range(10)))
print("built-in range - %s \n" % list(range(0, -12, -2)))
print("my range - %s \n" % list(my_range(-12, 0, -2)))
