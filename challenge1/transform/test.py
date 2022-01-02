import unittest

from parameterized import parameterized

from transform.errors import MalformedCSVRow, MalformedIndex1Value
from transform.normalizer import _should_translate, _split_index


class TransformationTests(unittest.TestCase):
    @parameterized.expand([
        [1, "a", "b"],
        [10, "a" * 10, "b" * 10],
        [1000, "a" * 1000, "b" * 1000],
    ])
    def test_should_translate_true(self, length, value1, value2):
        self.assertTrue(_should_translate(length, value1, value2))

    @parameterized.expand([
        [1, "a", "bb"],
        [10, "a" * 5, "b" * 5],
        [1000, "a" * 1000, "b" * 10],
    ])
    def test_should_translate_false(self, length, value1, value2):
        self.assertFalse(_should_translate(length, value1, value2))

    @parameterized.expand([
        [[1, "abc+defg", "", 2], 1, 2, "+", ["abc", "defg"]],
        [["abc+defg", 1, ""], 0, 2, "+", ["abc", "defg"]],
    ])
    def test_split_index_ok(self, row, index1, index2, sep, expected_result):
        self.assertListEqual(expected_result, _split_index(row, index1, index2, sep))

    @parameterized.expand([
        [[1, "abc+defg", "", 2], 1, 5, "+", MalformedCSVRow],
        [[1, "abcdefg", "", 2], 1, 2, "+", MalformedIndex1Value],
        [None, 1, 5, "+", TypeError],

    ])
    def test_split_index_err(self, row, index1, index2, sep, expected_ex):
        self.assertRaises(expected_ex, _split_index, row, index1, index2, sep)
