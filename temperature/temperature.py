"""
Module for the Temperature class
"""

# from typing import (
#     Union,
#     # Literal, # python > 3.8 :(
#     Type,
#     TypeVar,
#     NewType,
#     overload,
# )

from multimethod import multimethod, multimeta


from meta import (
    TemperatureMeta,
    Kelvin,
    Celsius,
    Fahrenheit,
)
from abs_zero import abs_zero




class Temperature(
    # metaclass = multimeta
):
    """
    Factory to facilitate easy conversions between temperature scales
    """
    def __init__(
        self, 
        value: TemperatureMeta,
    ):
        self.value = value

    

    @property
    def K(self):
        ...

    @K.setter
    def K(self, x):
        ...

    @property
    def C(self):
        ...

    @C.setter
    def C(self, x):
        ...

    @property
    def F(self):
        ...

    @F.setter
    def F(self, x):
        ...
    
    


    


@multimethod
def convert(
    temp: None
) -> None:
    ...

# @convert.register
# def _(
#     temp: Fahrenheit,
# ) -> Celsius:
#     return Celsius((temp - 32)*5/9)

# @convert.register
# def _(
#     temp: Celsius,
# ) -> Kelvin:
#     return Kelvin(temp + _abs_zero)

# @convert.register
# def _(
#     temp: Fahrenheit,
# ) -> Kelvin:
#     return convert(convert(temp))



    

if __name__ == '__main__':

    temp_f1 = Fahrenheit(212)
    temp_c1 = Celsius(270)