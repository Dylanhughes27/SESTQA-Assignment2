import unittest
from main import calculateBMI

class BmiCalcTestCase(unittest.TestCase):

    def testNormalCalc(self):
        result = calculateBMI(150, 72)
        self.assertEqual(result, 20.8)

    def testNormalCalc2(self):
        result = calculateBMI(125, 68)
        self.assertEqual(result, 19.5)
