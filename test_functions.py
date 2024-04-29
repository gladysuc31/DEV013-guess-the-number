"""Tests"""
import unittest
from unittest.mock import patch
import main

class TestFunctions(unittest.TestCase):
    """tests for main.py functions"""
    
    def test_compare_number(self):
        """test to check if the result is false"""
        result, message = main.compare_number(3, 5)
        self.assertFalse(result)

    @patch('builtins.input', return_value='42')
    def test_user_guess_returns_int(self, mock_input):
        """test to verify the user's input is an interger"""
        user_input = main.user_guess()
        self.assertIsInstance(user_input, int)

    @patch('main.random.randint', return_value=42)
    def test_computer_guess_in_range(self, mock_randint):
        """test to verify the random interger is between 1-100"""
        computer_input = main.computer_guess()
        self.assertLessEqual(computer_input, 100)
        self.assertGreaterEqual(computer_input, 1)

if __name__ == '__main__':
    unittest.main()