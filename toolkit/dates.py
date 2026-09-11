"""Calendar helpers, all on datetime.date."""

from __future__ import annotations

import calendar
from datetime import date, timedelta


def parse_iso_date(text):
    """Parse a YYYY-MM-DD string into a date, ignoring surrounding space."""
    return date.fromisoformat(text.strip())


def days_between(start, end):
    """Return the absolute number of days between two dates."""
    return abs((end - start).days)


def add_business_days(start, count):
    """Advance or rewind `start` by `count` weekdays.

    Saturday and Sunday are skipped in both directions. A count of zero
    leaves the date unchanged.
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
    """Return the first and last dates of the month that contains `day`."""
    last = calendar.monthrange(day.year, day.month)[1]
    return date(day.year, day.month, 1), date(day.year, day.month, last)
