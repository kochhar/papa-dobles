import unittest
from datetime import date

from toolkit import dates


class ParseIsoDateTests(unittest.TestCase):
    def test_surrounding_space_is_ignored(self):
        self.assertEqual(dates.parse_iso_date(" 2026-09-11 "), date(2026, 9, 11))


class DaysBetweenTests(unittest.TestCase):
    def test_order_does_not_matter(self):
        start, end = date(2026, 1, 1), date(2026, 1, 31)
        self.assertEqual(dates.days_between(start, end), 30)
        self.assertEqual(dates.days_between(end, start), 30)


class AddBusinessDaysTests(unittest.TestCase):
    def test_the_weekend_is_skipped(self):
        friday = date(2026, 9, 11)
        self.assertEqual(dates.add_business_days(friday, 1), date(2026, 9, 14))

    def test_counting_backwards_skips_it_too(self):
        monday = date(2026, 9, 14)
        self.assertEqual(dates.add_business_days(monday, -1), date(2026, 9, 11))


class MonthBoundsTests(unittest.TestCase):
    def test_short_month(self):
        first, last = dates.month_bounds(date(2026, 2, 10))
        self.assertEqual(first, date(2026, 2, 1))
        self.assertEqual(last, date(2026, 2, 28))


if __name__ == "__main__":
    unittest.main()
