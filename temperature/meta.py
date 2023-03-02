"""
Module containing temperature scale types
"""

from typing import Union, Type

from constants import _abs_zero_K, _abs_zero_C, _abs_zero_F


class TemperatureMeta(float):
    def __new__(cls,  *args,  **kwargs,):
        return super().__new__(cls, *args, **kwargs,)
    
class Kelvin(TemperatureMeta):
    def __init__(self, x):
        assert x > _abs_zero_K, f'Input must be above absolute zero ({_abs_zero_K} K)'
        super().__init__()

class Celsius(TemperatureMeta): 
    def __init__(self, x):
        assert x > _abs_zero_C, f'Input must be above absolute zero ({_abs_zero_C} C)'
        super().__init__()

class Fahrenheit(TemperatureMeta):
    def __init__(self, x):
        assert x > _abs_zero_F, f'Input must be above absolute zero ({_abs_zero_F} F)'
        super().__init__()


_ALL_UNITS = Union[Fahrenheit, Celsius, Kelvin]
_ALL_META = Union[Type[Kelvin], Type[Celsius], Type[Fahrenheit]]


if __name__ == '__main__':

    k = Fahrenheit(-1000)

    print(k)