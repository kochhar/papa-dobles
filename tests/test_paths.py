import unittest

from toolkit import paths


class NormalizeSlashesTests(unittest.TestCase):
    def test_backslashes_and_repeats_collapse(self):
        self.assertEqual(paths.normalize_slashes("a\\b//c"), "a/b/c")


class SplitExtensionTests(unittest.TestCase):
    def test_only_the_last_suffix_is_the_extension(self):
        self.assertEqual(paths.split_extension("dir/file.tar.gz"), ("dir/file.tar", ".gz"))

    def test_no_extension(self):
        self.assertEqual(paths.split_extension("README"), ("README", ""))


class IsHiddenTests(unittest.TestCase):
    def test_dotfile(self):
        self.assertTrue(paths.is_hidden("/a/.env"))

    def test_ordinary_file(self):
        self.assertFalse(paths.is_hidden("/a/b"))


class CommonPrefixTests(unittest.TestCase):
    def test_shared_directories(self):
        self.assertEqual(paths.common_prefix(["a/b/c", "a/b/d"]), "a/b")

    def test_nothing_in_common(self):
        self.assertEqual(paths.common_prefix(["a/b", "x/y"]), "")

    def test_no_paths(self):
        self.assertEqual(paths.common_prefix([]), "")


if __name__ == "__main__":
    unittest.main()
