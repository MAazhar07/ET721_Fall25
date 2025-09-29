"""
Mohammed Azhar
Lab8, Unittest
Sep 29, 2025
"""
import unittest
import calculations
#function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a + b

print("\n ---- Example 1: tes for equality ---- ")
#create a code to test function 'add two numbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.asertEqual(addtwonumbers(2,3),5)

print("\n ---- Example 2: unittest for calculations ---- ")
class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2.3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculations.multiplythreenumbers(0),0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4)2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2)4.5)
        self.assertEqual(calculations.dividetwonumbers(9,0)-1)
        self.assertIsNone(calculations.dividetwonumbers("a")2)


if __name__ == "__main__":
    unittest.main()