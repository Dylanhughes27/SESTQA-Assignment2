import unittest
from main import convInchToMeter

class InchToMeterTestCase(unittest.TestCase):

    def test_huge_height_conv(self):
        result = convInchToMeter(107)
        self.assertEqual(result, 2.675)

    def test_small_height_conv(self):
        result = convInchToMeter(30)
        self.assertEqual(result, 0.75)
