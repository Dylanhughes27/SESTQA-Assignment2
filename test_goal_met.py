import unittest
from main import isGoalMet

class GoalMetTestCase(unittest.TestCase):

    def testGoalPassed(self):
        result = isGoalMet(35, 64)
        self.assertEqual(result, True)

    def testGoalFailed(self):
        result = isGoalMet(35, 65)
        self.assertEqual(result, False)
