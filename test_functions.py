import unittest
import main

class testFunctions(unittest.TestCase):

    def test_compareNumber(self):
        self.assertFalse(main.compareNumber(3,5))
        self.assertTrue(main.compareNumber(89,89))

    def test_userGuess(self):
        self.assertEqual(type(main.userGuess()), int)

    def test_computerGuess(self):
        self.assertLessEqual(main.computerGuess(), 101)