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
Exceptions for OdoMeter classes.
"""


class OdoMeterError(Exception):
    """Base class for all OdoMeter errors."""


class DateOdoMeterError(OdoMeterError):
    """Base class for DateOdoMeter errors."""


class DateOdoMeterNegativeValueError(DateOdoMeterError):
    """Raised when a negative date is encountered"""


class DateOdoMeterInvalidDayError(DateOdoMeterError):
    """Raised when an invalid day is selected."""


class DateOdoMeterInvalidMonthError(DateOdoMeterError):
    """Raised when an invalid month is selected."""
