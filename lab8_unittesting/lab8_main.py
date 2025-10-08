"""
Mohammed Azhar
Lab 8, unittest
Oct 6, 2025
"""

import unittest
import calculations
from employee import Employee  # import class 'Employee' from 'employee.py'
from BankAccount import BankAccount


# function to add and return the sum of two numbers
def addtwonumbers(a, b):
    return a + b


print("\n----- Example 1: test for equality -----")
# create a code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addtwonumbers(2, 3), 5)


print("\n----- Example 2: unittest for calculations -----")
class TestCalculation(unittest.TestCase):

    def test_multiplythreenumbers(self):
        self.assertEqual(calculations.multiplythreenumbers(5), 5)
        self.assertEqual(calculations.multiplythreenumbers(2, 3), 6)  # fixed expected value from 5 to 6
        self.assertEqual(calculations.multiplythreenumbers(2, 3, 4), 24)
        self.assertEqual(calculations.multiplythreenumbers(0), 0)

    def test_dividetwonumbers(self):
        self.assertEqual(calculations.dividtwonumbers(8, 4), 2)  # fixed function name
        self.assertAlmostEqual(calculations.dividtwonumbers(9, 2), 4.5)
        self.assertEqual(calculations.dividtwonumbers(9, 0), -1)
        self.assertIsNone(calculations.dividtwonumbers("a", 2))


print("\n----- Example 3: Employee class tests -----")
class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('Peter', 'Pan', 50000)

    def test_emailemployee(self):
        self.assertEqual(self.emp1.email, "Peter.Pan@email.com")  # fixed attribute name

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")

        # update the first name
        self.emp1.first = "Will"

        # re-test full name 
        self.assertEqual(self.emp1.fullname, 'Will Pan')

    def test_salary(self):
        # test salary before the raise
        self.assertEqual(self.emp1.salary, 50000)

        # first, raise the salary
        self.emp1.apply_raise()

        # second, test salary
        self.assertEqual(self.emp1.salary, 52500)


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


if __name__ == "__main__":
    unittest.main()