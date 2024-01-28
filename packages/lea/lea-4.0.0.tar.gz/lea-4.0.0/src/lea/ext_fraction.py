"""
--------------------------------------------------------------------------------

    ext_fraction.py

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
from fractions import Fraction
from .toolbox import lcm


class ExtFraction(Number, Fraction):
    """
    A ExtFraction instance represents a number as a fraction
    It inherits Number and Fraction, overloading methods to
    improve usability
    """

    class Error(Exception):
        pass

    def __new__(cls, numerator=0, denominator=None):
        """ returns a new instance of ExtFraction
            following signatures of Fraction constructor
            Note that the constructor does NOT check that the fraction
            is in the range 0 to 1; this is so to allow intermediate
            results in expressions to go beyond that range;
            the range is verified when string representation is required
            (method str) or by explicit call to check() method 
        """
        return cls._from_fraction(Fraction(numerator, denominator))

    @classmethod
    def _from_fraction(cls, fraction):
        """ static method, returns a ExtFraction numerically equivalent to
            the given Fraction instance;
            if fraction is not an instance of Fraction then it is returned
            as-is
        """
        if not isinstance(fraction, Fraction):
            return fraction
        return Fraction.__new__(cls, fraction)

    @staticmethod
    def coerce(value):
        """ static method, returns a ExtFraction instance corresponding the given value:
            if the value is a ExtFraction instance, then it is returned, otherwise, a
            new ExtFraction instance is returned corresponding to given value
        """
        if isinstance(value, ExtFraction):
            return value
        return ExtFraction(value)

    def __coerce_func(func):
        """ internal utility function
            returns a function returning a ExtFraction
            equivalent to the given function func returning Fraction
        """
        def new_func(*args):
            return args[0].__class__._from_fraction(func(*args))
        return new_func

    # overloading arithmetic magic methods of Fraction
    # to convert Fraction result into ExtFraction result
    # Note: do not overwrite __floordiv__, __rfloordiv__, __pow__
    # since these methods do not return Fraction instances
    __pos__ = __coerce_func(Fraction.__pos__)
    __neg__ = __coerce_func(Fraction.__neg__)
    __pow__ = __coerce_func(Fraction.__pow__)
    __add__ = __coerce_func(Fraction.__add__)
    __radd__ = __coerce_func(Fraction.__radd__)
    __sub__ = __coerce_func(Fraction.__sub__)
    __rsub__ = __coerce_func(Fraction.__rsub__)
    __mul__ = __coerce_func(Fraction.__mul__)
    __rmul__ = __coerce_func(Fraction.__rmul__)
    __truediv__ = __coerce_func(Fraction.__truediv__)
    __rtruediv__ = __coerce_func(Fraction.__rtruediv__)
    __abs__ = __coerce_func(Fraction.__abs__)

    del __coerce_func

    @staticmethod
    def convert_to_same_denom(fractions):
        """ static method, returns a tuple of integers
            which are the numerators of given sequence of fractions,
            after conversion to a common denominator  
        """
        denominators = tuple(fraction.denominator for fraction in fractions)
        denominators_lcm = lcm(*denominators)
        return (tuple(fraction.numerator * (denominators_lcm // fraction.denominator) for fraction in fractions),
                denominators_lcm)
