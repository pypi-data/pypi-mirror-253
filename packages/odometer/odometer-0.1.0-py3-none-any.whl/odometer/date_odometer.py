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
OdoMeter class for dates.
"""

from calendar import isleap, monthrange
from datetime import datetime, timedelta
from typing import Union, Literal

from odometer.exceptions import DateOdoMeterInvalidDayError, DateOdoMeterInvalidMonthError, \
    DateOdoMeterNegativeValueError
from odometer.odometer import OdoMeter


class DateOdoMeter(OdoMeter):
    """
    An Odometer class for dates

    """

    def __init__(
            self,
            value: Union[int, tuple[int, int, int], datetime] = 1,
            meter_format: tuple[
                Literal["DMY", "DYM", "MDY", "MYD", "YDM", "YMD"],
                tuple[int, int, int]
            ] = ("YMD", (1, 1, 4)),
            min_date: tuple[int, int, int] = (1, 1, 1),
            max_date: tuple[int, int, int] = (31, 12, 9999),
            iter_direction: Literal["up", "down"] = "up",
    ):
        """

        :param value: the initial value of the DateOdoMeter object.
        :type value: Union[int, tuple[int, int, int], datetime]
        :param meter_format: the format to be used when using print(DateOdoMeter)
        :type meter_format: tuple[Literal["DMY",
                                          "DYM",
                                          "MDY",
                                          "MYD",
                                          "YDM",
                                          "YMD"
                                          ],
                                  tuple[int, int, int]
                                  ]
        :param min_date: the lowest date to consider valid when iteratng
        :type min_date: tuple[int, int, int]
        :param max_date: the highest date to consider valid when iterating
        :type max_date: tuple[int, int, int]
        :param iter_direction: the direction to following when iterating
        :type iter_direction: Literal["up", "down"]
        """
        if isinstance(value, int):
            if value < 0:
                raise DateOdoMeterNegativeValueError
            self.__get_date_from_days__(value)
        elif isinstance(value, tuple):
            if any([item < 1 for item in value]):
                raise DateOdoMeterNegativeValueError
            self.__get_date_from_items__(value)
        elif isinstance(value, datetime):
            beginning_of_time = datetime(year=1, month=1, day=1)
            days = (value - beginning_of_time).days
            if days < 1:
                raise DateOdoMeterNegativeValueError
            self.__get_date_from_days__(days)
        self.__string_format__ = meter_format
        self.__min__ = min_date
        self.__min_date__ = (datetime(year=self.__min__[2],
                                      month=self.__min__[1],
                                      day=self.__min__[0]
                                      ) - datetime(year=1, month=1, day=1)).days
        self.__max__ = max_date
        self.__max_date__ = (datetime(year=self.__max__[2],
                                      month=self.__max__[1],
                                      day=self.__max__[0]
                                      ) - datetime(year=1, month=1, day=1)).days
        self.__iter_direction__ = iter_direction

    def __get_date_from_days__(self, number_of_days: int) -> None:
        """
        Set day, month and year from <number> of days by computing the date
        since year=1, month=1, day=1

        :param number_of_days:
        :type number_of_days: int
        :return: Nothing
        :rtype: None
        """
        initial_date = datetime(year=1, month=1, day=1)
        initial_date += timedelta(days=number_of_days)
        self.__day__ = initial_date.day
        self.__month__ = initial_date.month
        self.__year__ = initial_date.year

    def __get_date_from_items__(self, items: tuple[int, int, int]) -> None:
        """
        Set day, month and year from the individual tuple items provided.

        :param items: day, month, year
        :type items: tuple[int, int, int]
        :return: Nothing
        :rtype: None
        """
        self.__year__ = items[2]
        self.__max_days_february__ = 29 if isleap(self.__year__) else 28
        if 1 > items[1] or items[1] > 12:
            raise DateOdoMeterInvalidMonthError
        self.__month__ = items[1]
        if self.__month__ == 2 and items[0] > self.__max_days_february__:
            raise DateOdoMeterInvalidDayError
        if items[0] < 1 or items[0]> monthrange(self.__year__, self.__month__)[1]:
            raise DateOdoMeterInvalidDayError
        self.__day__ = items[0]

    @property
    def days_since_beginning(self) -> int:
        """
        Return the number of days elapsed since year=1, month=1, day=1 based
        on the current values of day, month, year.

        :return: the number of days since year=1, month=1, day=1
        :rtype: int
        """
        current_date = datetime(year=self.__year__, month=self.__month__, day=self.__day__)
        beginning_of_time = datetime(year=1, month=1, day=1)
        return (current_date - beginning_of_time).days

    @property
    def date(self) -> datetime:
        """
        Return a date object reflecting the value of the OdoMeter.

        :return: the OdoMeter value as datetime object
        :rtype: datetime
        """
        return datetime(year=self.__year__, month=self.__month__, day=self.__day__)

    @property
    def day(self) -> int:
        """
        Retrieve the day of the month.

        :return: the day of the month
        :rtype: int
        """
        return self.__day__

    @property
    def month(self) -> int:
        """
        Retrieve the month of the year.

        :return: The month of the year
        :rtype: int
        """
        return self.__month__

    @property
    def year(self) -> int:
        """
        Retrieve the year.

        :return: the year
        :rtype: int
        """
        return self.__year__

    def incr(self, days: int = 1) -> None:
        """
        Increment the date by <day> days

        :param days: the number of days to add to the date.
        :type days: int
        :return: Nothing
        :rtype: None
        """
        self.__day__ += days
        while self.__day__ > monthrange(self.__year__, self.__month__)[1]:
            days_of_current_month_to_remove = monthrange(self.__year__, self.__month__)[1]
            self.__month__ += 1
            if self.__month__ > 12:
                self.__month__ = 1
                self.__year__ += 1
            self.__day__ -= days_of_current_month_to_remove

    def decr(self, days: int = 1) -> None:
        """
        Decrement the date by <days> days

        :param days: the number of days to subtract from the date.
        :type days: int
        :return: Nothing
        :rtype: None
        """
        self.__day__ -= days
        while self.__day__ < 1:
            days_of_current_month_to_add = monthrange(self.__year__, self.__month__)[1]
            self.__month__ -= 1
            if self.__month__ < 1:
                self.__month__ = 12
                self.__year__ -= 1
            self.__day__ += days_of_current_month_to_add
        try:
            datetime(year=self.__year__, month=self.__month__, day=self.__day__)
        except ValueError:
            raise DateOdoMeterNegativeValueError

    def __other_to_int__(self, other: Union[int, tuple[int, int, int], datetime]) -> int:
        """
        Attempt to convert <other> to an integer value.

        :param other: the object that needs to be converted to an integer
        :type other: Union[int, tuple[int, int, int]
        :return: the integer value of <other>
        :rtype: int
        """
        if isinstance(other, int):
            return other
        if isinstance(other, DateOdoMeter):
            return other.days_since_beginning
        if isinstance(other, datetime):
            return DateOdoMeter(other).days_since_beginning

    def __add__(self, other: Union[int, tuple[int, int, int], datetime]) -> "DateOdoMeter":
        """
        Returns a new object that represents the sum of two objects.
        It implements the addition operator + in Python.

        :param other: the object whose value should be added
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: a new DateOdoMeter object where self.__day__ is incremented by <other>
        :rtype: DateOdoMeter
        """
        temp_date_odometer = DateOdoMeter((self.__day__, self.__month__, self.__year__))
        temp_date_odometer.incr(days=self.__other_to_int__(other))
        return temp_date_odometer

    def __eq__(self, other: Union[int, tuple[int, int, int], datetime]) -> bool:
        """
        Rich comparison: x==y calls x.__eq__(y)

        :param other: the object with which to compare
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: True if equal, False otherwise
        :rtype: bool
        """
        return self.days_since_beginning == self.__other_to_int__(other)

    def __ge__(self, other: Union[int, tuple[int, int, int], datetime]) -> bool:
        """
        Return whether x is greater than or equal y

        :param other: the object with which to compare
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: True if greater or equal, False otherwise
        :rtype: bool
        """
        return self.days_since_beginning >= self.__other_to_int__(other)

    def __gt__(self, other: Union[int, tuple[int, int, int], datetime]) -> bool:
        """
        Returns the result of the greater than operation x > y

        :param other: the object with which to compare
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: True if greater than <other>, False otherwise
        :rtype: bool
        """
        return self.days_since_beginning > self.__other_to_int__(other)

    def __le__(self, other: Union[int, tuple[int, int, int], datetime]) -> bool:
        """
        Returns True if the former is less than or equal to the latter argument
        i.e., x <= y

        :param other: the object with which to compare
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: True if less or equal, False otherwise
        :rtype: bool
        """
        return self.days_since_beginning <= self.__other_to_int__(other)

    def __lt__(self, other: Union[int, tuple[int, int, int], datetime]) -> bool:
        """
        Returns the result of the less than operation x < y

        :param other: the object with which to compare
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: True if less than <other>, False otherwise
        :rtype: bool
        """
        return self.days_since_beginning < self.__other_to_int__(other)

    def __ne__(self, other: Union[int, tuple[int, int, int], datetime]) -> bool:
        """
        Rich comparison: x!=y and x<>y call x.__ne__(y)

        :param other: the object with which to compare
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: True if not equal, False otherwise
        :rtype: bool
        """
        return self.days_since_beginning != self.__other_to_int__(other)

    def __next__(self) -> str:
        """
        Returns the “next” string representation of the DateOdoMeter

        :return: the “next” element
        :rtype: str
        """
        if self.__iter_direction__ == "up":
            self.incr()
        elif self.__iter_direction__ == "down":
            self.decr()
        if (
                self.days_since_beginning < self.__min_date__
                or
                self.days_since_beginning > self.__max_date__
        ):
            raise StopIteration
        return self.__str__()

    def __str__(self) -> str:
        """
        Returns a string representation of the DateOdoMeter

        :return: a string formatted
        :rtype: str
        """
        day_length = self.__string_format__[1][0]
        month_length = self.__string_format__[1][1]
        year_length = self.__string_format__[1][2]
        day_string = f"{self.__day__:0{day_length}}"
        month_string = f"{self.__month__:0{month_length}}"
        year_string = f"{self.__year__:0{year_length}}"
        if self.__string_format__[0] == "DMY":
            odometer_string = f"{day_string}{month_string}{year_string}"
        elif self.__string_format__[0] == "DYM":
            odometer_string = f"{day_string}{year_string}{month_string}"
        elif self.__string_format__[0] == "MDY":
            odometer_string = f"{month_string}{day_string}{year_string}"
        elif self.__string_format__[0] == "MYD":
            odometer_string = f"{month_string}{year_string}{day_string}"
        elif self.__string_format__[0] == "YDM":
            odometer_string = f"{year_string}{day_string}{month_string}"
        elif self.__string_format__[0] == "YMD":
            odometer_string = f"{year_string}{month_string}{day_string}"
        return odometer_string

    def __sub__(self, other: Union[int, tuple[int, int, int], datetime]) -> "DateOdoMeter":
        """
        Returns a new object that represents the difference of two objects.
        It implements the subtraction operator - in Python.

        :param other: the object whose value should be subtracted
        :type other: Union[int, tuple[int, int, int], datetime]
        :return: a new DateOdoMeter object with <other> subtracted from it
        :rtype: DateOdoMeter
        """
        other_as_integer = self.__other_to_int__(other)
        temp_date_odometer = DateOdoMeter((self.__day__, self.__month__, self.__year__))
        temp_date_odometer.decr(days=other_as_integer)
        return temp_date_odometer
