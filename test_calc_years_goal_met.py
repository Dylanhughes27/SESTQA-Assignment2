import unittest
from main import calcYearsToGoalMet

class CalcYearsTestCase(unittest.TestCase):

    def testYears1(self):
        result = calcYearsToGoalMet(45000, 1000000)
        self.assertEqual(result, 23)

    def testYears2(self):
        result = calcYearsToGoalMet(21000, 400000)
        self.assertEqual(result, 20)
