import unittest

from toolkit import dicts


class DeepGetTests(unittest.TestCase):
    def test_walks_a_dotted_path(self):
        self.assertEqual(dicts.deep_get({"a": {"b": {"c": 1}}}, "a.b.c"), 1)

    def test_missing_key_returns_the_default(self):
        self.assertEqual(dicts.deep_get({"a": 1}, "a.b", "fallback"), "fallback")


class InvertTests(unittest.TestCase):
    def test_values_become_keys(self):
        self.assertEqual(dicts.invert({"a": 1, "b": 2}), {1: "a", 2: "b"})


class GroupByTests(unittest.TestCase):
    def test_groups_keep_input_order(self):
        grouped = dicts.group_by(["ant", "bee", "ape"], lambda word: word[0])
        self.assertEqual(grouped, {"a": ["ant", "ape"], "b": ["bee"]})


class MergeTests(unittest.TestCase):
    def test_nested_dicts_are_merged_not_replaced(self):
        merged = dicts.merge({"a": {"x": 1}, "b": 2}, {"a": {"y": 2}})
        self.assertEqual(merged, {"a": {"x": 1, "y": 2}, "b": 2})

    def test_the_base_is_not_mutated(self):
        base = {"a": {"x": 1}}
        dicts.merge(base, {"a": {"y": 2}})
        self.assertEqual(base, {"a": {"x": 1}})


if __name__ == "__main__":
    unittest.main()
