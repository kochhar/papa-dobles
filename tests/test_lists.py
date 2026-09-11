import unittest

from toolkit import lists


class ChunkTests(unittest.TestCase):
    def test_last_chunk_is_short(self):
        self.assertEqual(lists.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_size_must_be_positive(self):
        with self.assertRaises(ValueError):
            lists.chunk([1], 0)


class FlattenTests(unittest.TestCase):
    def test_one_level_only(self):
        self.assertEqual(lists.flatten([[1, 2], [3]]), [1, 2, 3])


class DedupeTests(unittest.TestCase):
    def test_first_occurrence_wins(self):
        self.assertEqual(lists.dedupe([1, 2, 1, 3, 2]), [1, 2, 3])


class PartitionTests(unittest.TestCase):
    def test_order_is_preserved_in_both_halves(self):
        even, odd = lists.partition([1, 2, 3, 4], lambda n: n % 2 == 0)
        self.assertEqual(even, [2, 4])
        self.assertEqual(odd, [1, 3])


if __name__ == "__main__":
    unittest.main()
