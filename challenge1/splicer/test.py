import unittest

from parameterized import parameterized
from splicer.normalizer import _should_translate


class SplicerTests(unittest.TestCase):
    @parameterized.expand([
        [1, "a", "b"],
        [10, "a" * 10, "b" * 10],
        [1000, "a" * 1000, "b" * 1000],
    ])
    def test_translate_true(self, length, value1, value2):
        self.assertTrue(_should_translate(length, value1, value2))

    @parameterized.expand([
        [1, "a", "bb"],
        [10, "a" * 5, "b" * 5],
        [1000, "a" * 1000, "b" * 10],
    ])
    def test_translate_false(self, length, value1, value2):
        self.assertFalse(_should_translate(length, value1, value2))
