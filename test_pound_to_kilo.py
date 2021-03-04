import unittest
from main import convPoundToKilo

class PoundToKiloTestCase(unittest.TestCase):

    def test_huge_weight_conv(self):
        result = convPoundToKilo(974)
        self.assertEqual(result, 438.3)

    def test_small_weight_conv(self):
        result = convPoundToKilo(30)
        self.assertEqual(result, 13.5)
