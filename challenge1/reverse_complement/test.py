import unittest

from reverse_complement import translate


class TranslatorTests(unittest.TestCase):
    def test_a(self):
        self.assertEqual("GGCCAATT", translate("AATTGGCC"))
