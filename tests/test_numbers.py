import unittest

from toolkit import numbers


class ClampTests(unittest.TestCase):
    def test_confines_to_the_range(self):
        self.assertEqual(numbers.clamp(5, 1, 3), 3)
        self.assertEqual(numbers.clamp(0, 1, 3), 1)
        self.assertEqual(numbers.clamp(2, 1, 3), 2)

    def test_reversed_bounds_are_refused(self):
        with self.assertRaises(ValueError):
            numbers.clamp(1, 3, 1)


class MeanTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(numbers.mean([1, 2, 3]), 2)

    def test_no_values_is_an_error(self):
        with self.assertRaises(ValueError):
            numbers.mean([])


class MedianTests(unittest.TestCase):
    def test_odd_count_takes_the_middle(self):
        self.assertEqual(numbers.median([3, 1, 2]), 2)

    def test_even_count_averages_the_pair(self):
        self.assertEqual(numbers.median([1, 2, 3, 4]), 2.5)


class PercentileTests(unittest.TestCase):
    def test_nearest_rank(self):
        values = [1, 2, 3, 4, 5]
        self.assertEqual(numbers.percentile(values, 0.0), 1)
        self.assertEqual(numbers.percentile(values, 0.5), 3)
        self.assertEqual(numbers.percentile(values, 1.0), 5)

    def test_q_outside_zero_to_one_is_refused(self):
        with self.assertRaises(ValueError):
            numbers.percentile([1], 1.5)


if __name__ == "__main__":
    unittest.main()
