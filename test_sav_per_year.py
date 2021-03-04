import unittest
from main import calcSavingsPerYear

class SavPerYearTestCase(unittest.TestCase):

    def testNormalSalary(self):
        result = calcSavingsPerYear(100000, .25)
        self.assertEqual(result, 33750)

    def testAbnormalSalary(self):
        result = calcSavingsPerYear(96000, .21)
        self.assertEqual(result, 27216)
