import unittest

from toolkit import strings


class SlugifyTests(unittest.TestCase):
    def test_punctuation_becomes_one_hyphen(self):
        self.assertEqual(strings.slugify("Hello, World!"), "hello-world")

    def test_edges_are_trimmed(self):
        self.assertEqual(strings.slugify("  A  B  "), "a-b")


class TruncateMiddleTests(unittest.TestCase):
    def test_short_text_is_untouched(self):
        self.assertEqual(strings.truncate_middle("short", 10), "short")

    def test_middle_is_replaced_and_length_respected(self):
        self.assertEqual(strings.truncate_middle("abcdefghij", 7), "ab...ij")


class TitleCaseTests(unittest.TestCase):
    def test_words_are_capitalised_and_spacing_collapses(self):
        self.assertEqual(strings.title_case("  the quick  brown "), "The Quick Brown")


class CountWordsTests(unittest.TestCase):
    def test_empty_string_has_no_words(self):
        self.assertEqual(strings.count_words(""), 0)

    def test_runs_of_spaces_do_not_count(self):
        self.assertEqual(strings.count_words("a b  c"), 3)


if __name__ == "__main__":
    unittest.main()
