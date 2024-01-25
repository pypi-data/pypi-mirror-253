# -*- coding: utf-8 -*-

#  Copyright © 1995-2024. anonymous.

# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License  along with this
# program. If not, see <https://www.gnu.org/licenses/>.

"""
Base class for OdoMeter classes.
"""
from abc import abstractmethod
from typing import Any, Iterable


class OdoMeter:
    """
    Base class for odometer objects.
    """

    def __init__(self):
        pass

    @abstractmethod
    def __other_to_int__(self, other: Any) -> int:
        """
        Attempt to convert <other> to an integer value.

        :param other: the object that needs to be converted to an integer
        :type other: Any
        :return: the integer value of <other>
        :rtype: int
        """

    @abstractmethod
    def __add__(self, other: Any) -> "OdoMeter":
        """
        Returns a new object that represents the sum of two objects.
        It implements the addition operator + in Python.

        :param other: the object whose value should be added
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: a new OdoMeter object with the value of <other> added
        :rtype: OdoMeter
        """

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        """
        Rich comparison: x==y calls x.__eq__(y)

        :param other: the object with which to compare
        :type other: Any
        :return: True if equal, False otherwise
        :rtype: bool
        """

    @abstractmethod
    def __ge__(self, other: Any) -> bool:
        """
        Return whether x is greater than or equal y

        :param other: the object with which to compare
        :type other: Any
        :return: True if greater or equal, False otherwise
        :rtype: bool
        """

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        """
        Returns the result of the greater than operation x > y

        :param other: the object with which to compare
        :type other: Any
        :return: True if greater than <other>, False otherwise
        :rtype: bool
        """

    def __iadd__(self, other: Any) -> "OdoMeter":
        """
        Implements in-place addition x += y that adds together the operands
        and assigns the result to the left operand.
        This operation is also called augmented arithmetic assignment.
        The method simply returns the new value to be assigned to the first
        operand.

        :param other: the object whose value should be added
        :type other: Any
        :return: a new OdoMeter object with <other> added to it
        :rtype: OdoMeter
        """
        return self.__add__(other)

    def __isub__(self, other: Any) -> "OdoMeter":
        """
        Implements in-place subtraction x -= y that subtracts the operands
        from each other and assigns the result to the left operand.
        This operation is also called augmented arithmetic assignment.
        The method simply returns the new value to be assigned to the first
        operand.

        :param other: the object whose value should be subtracted
        :type other: Any
        :return: a new OdoMeter object with <other> subtracted from it
        :rtype: OdoMeter
        """
        return self.__sub__(other)

    def __iter__(self) -> Iterable:
        """
        An iterator object is an object that implements the __next__() dunder
        method that returns the next element of the iterable object and raises
        a StopIteration error if the iteration is done.

        :return: a new iterator object
        :rtype: Iterable
        """
        return self

    @abstractmethod
    def __le__(self, other: Any) -> bool:
        """
        Returns True if the former is less than or equal to the latter argument
        i.e., x <= y

        :param other: the object with which to compare
        :type other: Any
        :return: True if less or equal, False otherwise
        :rtype: bool
        """

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        """
        Returns the result of the less than operation x < y

        :param other: the object with which to compare
        :type other: Any
        :return: True if less than <other>, False otherwise
        :rtype: bool
        """

    @abstractmethod
    def __ne__(self, other: Any) -> bool:
        """
        Rich comparison: x!=y and x<>y call x.__ne__(y)

        :param other: the object with which to compare
        :type other: Any
        :return: True if not equal, False otherwise
        :rtype: bool
        """

    @abstractmethod
    def __next__(self):
        """
        Returns the “next” element when you iterate over the object.

        :return: the “next” element
        :rtype: Any
        """

    def __radd__(self, other: "OdoMeter") -> "OdoMeter":
        """
        Implements the reverse addition operation that is addition with
        reflected, swapped operands.

        :param other: an OdoMeter object from which to subtract self
        :type other: OdoMeter
        :return: a new OdoMeter object incremented by self
        :rtype: OdoMeter
        """
        return self.__add__(other)

    def __repr__(self) -> str:
        """
        Returns a string representation of the OdoMeter object.

        :return: a string representation of the OdoMeter object
        :rtype: str
        """
        return self.__str__()

    def __rsub__(self, other: "OdoMeter") -> "OdoMeter":
        """
        Implements the reverse subtraction operation that is subtraction with
        reflected, swapped operands.

        :param other: a OdoMeter object from which to subtract self
        :type other: OdoMeter
        :return: a new OdoMeter object with self subtracted from it
        :rtype: OdoMeter
        """
        return self.__sub__(other)

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the OdoMeter

        :return: a  formatted string representation of th OdoMeter object
        :rtype: str
        """

    @abstractmethod
    def __sub__(self, other: Any) -> "OdoMeter":
        """
        Returns a new object that represents the difference of two objects.
        It implements the subtraction operator - in Python.

        :param other: the object whose value should be subtracted
        :type other: Any
        :return: a new OdoMeter object with <other> subtracted from it
        :rtype: OdoMeter
        """

    @abstractmethod
    def incr(self):
        """
        Override this method with the code needed to increment the value of the meter.
        """

    @abstractmethod
    def decr(self):
        """
        Override this method with the code needed to decrement the value of the meter.
        """
