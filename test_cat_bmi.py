import unittest
from main import categorizeBMI

class BmiCatTestCase(unittest.TestCase):

    def testLowerBound(self):
        result = categorizeBMI(18.4)
        self.assertEqual(result, "Underweight")

    def testMidLowerBound(self):
        result = categorizeBMI(18.5)
        self.assertEqual(result, "Normal weight")

    def testMidUpperBound(self):
        result = categorizeBMI(24.9)
        self.assertEqual(result, "Normal weight")
        
    def testMidBound(self):
        result = categorizeBMI(20)
        self.assertEqual(result, "Normal weight")

    def testOverweightLowerBound(self):
        result = categorizeBMI(25)
        self.assertEqual(result, "Overweight")

    def testOverweightUpperBound(self):
        result = categorizeBMI(29.9)
        self.assertEqual(result, "Overweight")

    def testOverweightNormalBound(self):
        result = categorizeBMI(27.5)
        self.assertEqual(result, "Overweight")

    def testObeseBound(self):
        result = categorizeBMI(30)
        self.assertEqual(result, "Obese")
