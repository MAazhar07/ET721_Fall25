"""
Mohammed Azhar
sep 17, 2025
Lab 6: objects and classes
"""

print("\n----- Example 1: create a class -----")
class Circle(object):
    def __init_(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius += r
        return self.radius


class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    # mwthod to calculate the area
    def area(self):
        return self.width * self.height
    
    # method to calculate the perimeter
    def perimeter(self):
        return 2*self.width + 2*self.height
    

#create an instance of the cklass, which is an object
circle1 = Circle(5, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2,5,"magenta")
rectangle2 = Rectangle(7,3, "blue")

# Accessing information in an object
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

# updating data in an object
# change circle1 color form 'red' to 'yellow'
print(f"The clor of circle1 before the update = {circle1.color}")
circle1.color = "yellow"
print(f"The clor of circle1 after the update = {circle1.color}")

# Accessing a mthod
print(f"Radius of circle2 = {circle2.radius}")
# update the radius by adding 5
circle2.add_radius(5)
print(f"Radius of circle2 after method add_radius = {circle2.radius}")

# accessing method in Rectangle
print(f"The area of the rectangle with width {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}")
print(f"the perimeter of rectnagle2 = {rectangle2.perimeter()}")

#Lab Exercise
class BankAccount(object):
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance. Withdrawal cannot be made.")


useraccount = BankAccount("123456789", "Student's name")

print(f"Account holder: {useraccount.account_holder}")
print(f"Account number: {useraccount.account_number}")
print(f"Initial balance: {useraccount.balance}")

print("\n--- Performing Transactions ---")
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)

print(f"\nFinal balance = {useraccount.balance}")

        
    
