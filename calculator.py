'''
Create a function that takes two parameters and returns their sum.
Create a function that takes two parameters and returns their difference.
Create a function that takes two parameters and returns their product.
Create a function that takes two parameters and returns their quotient.
Create tests in you main function showing the results of each function printed.
'''


def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    print(a / b)

def square_root(a, b):
    print(a ** 0.5, b ** 0.5)
    


def arithmetic_operations(num1, num2):
    add(num1, num2)
    subtract(num1, num2)
    multiply(num1, num2)
    divide(num1, num2) 
    square_root(num1, num2)
try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    arithmetic_operations(num1, num2)
except ZeroDivisionError:
    print("Error: You cannot divide by 0.")
finally:
    print("You have used the artithmetic calculator!")
            
