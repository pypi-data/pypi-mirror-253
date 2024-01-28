"""
--------------------------------------------------------------------------------

    ext_decimal.py

--------------------------------------------------------------------------------
Copyright 2013-2024 Pierre Denis

This file is part of Lea.

Lea is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lea is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Lea.  If not, see <http://www.gnu.org/licenses/>.
--------------------------------------------------------------------------------
"""

from .number import Number
from decimal import Decimal
from fractions import Fraction

class ExtDecimal(Number, Decimal):
    """
    A ExtDecimal instance represents a number as a decimal.
    It inherits Number and Decimal, overloading methods to improve usability.
    It has a boolean _display_as_percentage attribute indicating whether it
    has to display as a percentage.
    """

    class Error(Exception):
        pass

    _display_nb_decimals = None

    def __new__(cls, val=0):
        """ returns a new instance of ExtDecimal
            following signatures of Decimal constructor
            + allowing a percentage in val as a string 'xxx %'
              with xxx being a float literal
            Note that the constructor does NOT check that the decimal
            is in the range 0 to 1; this is so to allow intermediate
            results in expressions to go beyond that range;
            the range is verified when string representation is required
            (method str) or by explicit call to check() method
        """
        is_percentage = False
        if isinstance(val, str):
            val = val.strip()
            if val.endswith('%'):
                val = val[:-1]
                is_percentage = True
        elif isinstance(val, Fraction):
            val = float(val)
        new_decimal = Decimal(val)
        if is_percentage:
            new_decimal /= 100
        new_ext_decimal = cls._from_decimal(new_decimal, is_percentage)
        return new_ext_decimal

    __slots__ = ('_display_as_percentage',)

    @classmethod
    def _from_decimal(cls, decimal, display_as_percentage):
        """ static method, returns a ExtDecimal numerically equivalent to
            the given Decimal instance;
            if decimal is not an instance of Decimal then it is returned as-is
        """
        if not isinstance(decimal, Decimal):
            return decimal
        new_ext_decimal = Decimal.__new__(cls, decimal)
        new_ext_decimal._display_as_percentage = display_as_percentage
        return new_ext_decimal

    def __str__(self):
        if not Number.use_overloaded_str_method:
            return Decimal.__str__(self)
        n = (Decimal(100.)*self) if self._display_as_percentage else self
        if ExtDecimal._display_nb_decimals is None:
            res = Decimal.__str__(n)
        else:
            fmt = "%%.%df" % (ExtDecimal._display_nb_decimals,)
            res = fmt % (n,)
        if self._display_as_percentage:
            res += " %"
        return res

    __repr__ = __str__

    @staticmethod
    def coerce(value, display_as_percentage=False):
        """ static method, returns a ExtDecimal instance corresponding the given value:
            if the value is a ExtDecimal instance with given display_as_percentage,
            then it is returned, otherwise, a new ExtDecimal instance is returned
            corresponding to given value and display_as_percentage
        """
        if isinstance(value, ExtDecimal) \
                and value._display_as_percentage == display_as_percentage:
            return value
        new_ext_decimal = ExtDecimal(value)
        new_ext_decimal._display_as_percentage =  display_as_percentage
        return new_ext_decimal

    def __coerce_func_1(func):
        """ internal utility function;
            returns a function returning a ExtDecimal
            equivalent to the given function 1-arg func returning Decimal;
            the result inherits the display attributes of the argument
        """
        def new_func(arg):
            return arg.__class__._from_decimal(func(arg), arg._display_as_percentage)
        return new_func

    def __coerce_func_2(func):
        """ internal utility function;
            returns a function returning a ExtDecimal
            equivalent to the given function 2-args func returning Decimal;
            the display attributes of the result is determined according to
            the display attributes of the arguments
        """
        def new_func(arg1, arg2):
            display_as_percentage = arg1._display_as_percentage
            if isinstance(arg2, ExtDecimal):
                display_as_percentage = display_as_percentage and arg2._display_as_percentage
            return  arg1.__class__._from_decimal(func(arg1, arg2), display_as_percentage)
        return new_func

    # overloading arithmetic magic methods of Decimal
    # to convert Decimal result into ExtDecimal result
    # Note: do not overwrite __floordiv__, __rfloordiv__, __pow__
    # since these methods do not return Decimal instances
    __pos__ = __coerce_func_1(Decimal.__pos__)
    __neg__ = __coerce_func_1(Decimal.__neg__)
    __pow__ = __coerce_func_2(Decimal.__pow__)
    __add__ = __coerce_func_2(Decimal.__add__)
    __radd__ = __coerce_func_2(Decimal.__radd__)
    __sub__ = __coerce_func_2(Decimal.__sub__)
    __rsub__ = __coerce_func_2(Decimal.__rsub__)
    __mul__ = __coerce_func_2(Decimal.__mul__)
    __rmul__ = __coerce_func_2(Decimal.__rmul__)
    __truediv__ = __coerce_func_2(Decimal.__truediv__)
    __rtruediv__ = __coerce_func_2(Decimal.__rtruediv__)
    __abs__ = __coerce_func_1(Decimal.__abs__)

    del __coerce_func_1, __coerce_func_2

