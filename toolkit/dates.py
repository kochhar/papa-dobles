"""Calendar helpers, all on datetime.date."""

from __future__ import annotations

import calendar
from datetime import date, timedelta


def parse_iso_date(text):
    """Parse an ISO 8601 calendar date, ignoring surrounding whitespace.

    Delegates to date.fromisoformat, so anything that is not YYYY-MM-DD
    (or an accepted variant) still raises ValueError.
    """
    return date.fromisoformat(text.strip())


def days_between(start, end):
    """Return the absolute number of days between two dates.

    Order does not matter: the result is always non-negative.
    """
    return abs((end - start).days)


def add_business_days(start, count):
    """Shift a date by `count` weekdays, skipping Saturday and Sunday.

    A positive count moves forward and a negative count moves backward.
    The start date itself is not counted; the first step is always taken.
    """
    current = start
    remaining = count
    step = 1 if count >= 0 else -1
    while remaining != 0:
        current = current + timedelta(days=step)
        if current.weekday() < 5:
            remaining -= step
    return current


def month_bounds(day):
    """Return the first and last dates of the month that contains `day`.

    February in a leap year ends on the 29th; otherwise the last day is
    whatever calendar.monthrange reports.
    """
    last = calendar.monthrange(day.year, day.month)[1]
    return date(day.year, day.month, 1), date(day.year, day.month, last)
