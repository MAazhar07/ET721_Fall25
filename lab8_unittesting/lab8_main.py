"""
Mohammed Azhar
Lab 8, unittest
Oct 5, 2025
"""

import unittest
from unittest.mock import patch, mock_open
import calculations
from BankAccount import BankAccount


print("\n----- Example 1: test for equality -----")

def addtwonumbers(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addtwonumbers(2, 3), 5)
        self.assertEqual(addtwonumbers(0, 5), 5)
        self.assertNotEqual(addtwonumbers(2, 2), 5)



print("\n----- Example 2: unittest for calculations -----")

class TestCalculation(unittest.TestCase):

    def test_multiplythreenumbers(self):
        self.assertEqual(calculations.multiplythreenumbers(1, 2), 2)
        self.assertEqual(calculations.multiplythreenumbers(1, 2, 3), 6)
        self.assertEqual(calculations.multiplythreenumbers(5), 5)

    def test_addthreenumbers(self):
        self.assertEqual(calculations.addthreenumbers(1, 2), 3)
        self.assertEqual(calculations.addthreenumbers(5), 5)
        self.assertEqual(calculations.addthreenumbers(1, 2, 3), 6)

    def test_subtracttwonumbers(self):
        self.assertEqual(calculations.subtracttwonumbers(5, 2), 3)
        self.assertEqual(calculations.subtracttwonumbers(2, 5), -3)
        self.assertEqual(calculations.subtracttwonumbers(10, 0), 10)

    def test_dividetwonumbers(self):
        self.assertEqual(calculations.dividetwonumbers(10, 2), 5)
        self.assertEqual(calculations.dividetwonumbers(9, 3), 3)
        self.assertAlmostEqual(calculations.dividetwonumbers(7, 2), 3.5)

    def test_dividebyzero(self):
        self.assertIsNone(calculations.dividetwonumbers(10, 0))

    def test_nonnumericvalues(self):
        self.assertIsNone(calculations.dividetwonumbers(10, "a"))
        self.assertIsNone(calculations.dividetwonumbers("b", 5))

    def test_unexpected_exception(self):
        with self.assertRaises(Exception):
            calculations.dividetwonumbers()



print("\n----- Example 3: Employee class tests -----")

class Employee:
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary

    @property
    def emailemployee(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('Peter', 'Pan', 50000)

    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "Peter.Pan@email.com")
        self.emp1.first = "Will"
        self.assertEqual(self.emp1.emailemployee, "Will.Pan@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.salary, 52500)



print("\n----- Example 4: Testing file reading using mock -----")

def process_file(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total


class TestProcessFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="1\n2\n3\n")
    def test_process_file(self, mock_file):
        result = process_file("fake_path.txt")
        self.assertEqual(result, 6)
        mock_file.assert_called_once_with("fake_path.txt", 'r')



print("\n----- Lab Exercise: BankAccount tests -----")

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Fatima", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)
        self.account.deposit(25)
        self.assertEqual(self.account.get_balance(), 175)
        with self.assertRaises(ValueError):
            self.account.deposit(-10)
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdrawal(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)
        self.account.withdraw(20)
        self.assertEqual(self.account.get_balance(), 50)
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_over_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_sequence_operations(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.deposit(25)
        self.account.withdraw(75)
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == '__main__':
    unittest.main()