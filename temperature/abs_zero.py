"""
this module probably isnt needed
"""

from typing import (
    overload,
)

# from multimethod import multimethod

from .meta import (
    Kelvin,
    Celsius,
    Fahrenheit,
)

from constants import _abs_zero_K, _abs_zero_C, _abs_zero_F


@overload
def abs_zero(
    scale = 'K',
) -> Kelvin:
    ...

@overload
def abs_zero(
    scale = 'C',
) -> Celsius:
    ...

@overload
def abs_zero(
    scale = 'F',
) -> Fahrenheit:
    ...

# @multimethod
def abs_zero(
    scale: str = 'K',
):
    # just doing this with if/then for now
    # cant get multidispatch to work with typing
    if scale == 'K':
        return Kelvin(_abs_zero_K)
    elif scale == 'C':
        return Celsius(_abs_zero_C)
    elif scale == 'F':
        return Fahrenheit(_abs_zero_F)
    else:
        raise NotImplementedError('scale must be one of K, C or F')

# @abs_zero.register
# def _(
#     scale: Type[Kelvin],
# ) -> Kelvin:
#     return Kelvin(-273.15)


if __name__ == '__main__':

    ...