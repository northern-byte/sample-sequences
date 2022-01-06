import unittest

from reverse_complement import translate


class ReverseComplementTests(unittest.TestCase):
    def test_translate_ok(self):
        self.assertEqual("GGCCAATT", translate("AATTGGCC"))