import unittest

from toolkit import parsing


class ParseKeyValuesTests(unittest.TestCase):
    def test_space_around_pairs_is_ignored(self):
        self.assertEqual(parsing.parse_key_values("a=1, b = 2 "), {"a": "1", "b": "2"})

    def test_a_bare_word_is_an_error(self):
        with self.assertRaises(ValueError):
            parsing.parse_key_values("a")


class ParseCsvLineTests(unittest.TestCase):
    def test_quoted_commas_stay_in_their_field(self):
        self.assertEqual(parsing.parse_csv_line('a,"b,c",d'), ["a", "b,c", "d"])


class ParseDurationTests(unittest.TestCase):
    def test_compound(self):
        self.assertEqual(parsing.parse_duration("1h30m"), 5400)

    def test_single_unit(self):
        self.assertEqual(parsing.parse_duration("45s"), 45)

    def test_nonsense_is_an_error(self):
        with self.assertRaises(ValueError):
            parsing.parse_duration("abc")


class ParseBoolTests(unittest.TestCase):
    def test_case_is_ignored(self):
        self.assertTrue(parsing.parse_bool("YES"))
        self.assertFalse(parsing.parse_bool("off"))

    def test_anything_else_is_an_error(self):
        with self.assertRaises(ValueError):
            parsing.parse_bool("maybe")


if __name__ == "__main__":
    unittest.main()
