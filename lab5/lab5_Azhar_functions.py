"""
Mohammed Azhar
functions file
Sep 15, 2025
lab 5, function
"""

# example 1: define function that pass two numbers and return the product of it
def product(a = 0, b = 0):
    c = a*b
    return c

# Example 2: function ro calculate the hypotennuse 
def hypotenuse(side1, side2):
    return (side1**2 + side2**2)**0.5

# Example 3: function to check if a number is positive, negative, or zero.
# the function returns a string
def check_number(num):
    if (num>0):
        return "POSITIVE"
    elif (num<0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
    # Example 4: function to calculate the average of a list of grades and return 'true' if the average is greater than 60, otherwise, it returns 'false'

def check_grades(grades):
    # initialize the average grade value
    avg = 0
    # sum the individual 'g' from list 'grades' into 'avg'
    for g in grades:
        avg += g
    avg /= len(grades)
    return avg

def check_pass(avg_grade):
    # check if average is greater than 60
    if avg_grade >= 60:
        return True
    else:
        return False
    
# LAB EXERCISE

import random

def gen_rand(min_n, max_n):
    return random.randint(min_n, max_n)

GUESS_NUM = 7

def check_guess(rand_num):
    if rand_num < GUESS_NUM:
        print("The number is smaller than the guess number")
    elif rand_num > GUESS_NUM:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")


