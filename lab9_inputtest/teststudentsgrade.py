"""
Mohammed Azhar
Oct 8, 2025
Lab 9, test input and output
"""

import unittest
from unittest.mock import patch
import io
import studentsgrade


class TestMainFunction(unittest.TestCase):
    # test with valid input with 3 students and three grades
    @patch("builtins.input", side_effect=["3", "35", "90", "75"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("The class average is 66.67", output)  # 200/3 = 66.67

    # test with invalid student count, then valid grades
    @patch("builtins.input", side_effect=["-1", "0", "2", "95", "110", "80"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn(
            "Number of students must be greater than 0. Please try again.", output
        )
        self.assertIn("Invalid input. Enter a grade between 0 and 100.", output)
        self.assertIn("The class average is 87.50", output)  # (95 + 80) / 2

    # NEW TEST: invalid data type (strings instead of numbers)
    @patch("builtins.input", side_effect=["two", "3", "abc", "50", "70", "90"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_datatype_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()

        # check if error message for invalid input is shown
        self.assertIn("Invalid input. Please enter a positive number.", output)
        self.assertIn("Invalid input! Enter a numerical value.", output)
        self.assertIn("The class average is 70.00", output)  # (50+70+90)/3 = 70.0


if __name__ == "__main__":
    unittest.main()
