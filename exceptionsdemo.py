# exceptionsdemo.py

# line-by-line check
# try-catch

# What is an Exception?
'''
try
    the test of block code
except
    handling of errors
finally (opt)
    excecution despite results
'''

try:
    file = open("demo")
except:
    print("The file to open does not exist")

divident = 50
divisor = 0

try:
    result = divident / divisor # division by zero
    print("Result: ", result)
except ZeroDivisionError as e:
    print("Error: You cannot divide by 0, Will")

try:
    f = open("non")
except FileNotFoundError:
    print("The file does not exist!")        
except Exception as e:
    print(e)
finally:
    print("This message")

def calculate_square_root(number):
    if number < 0:
        raise Exception("number cannot be negative")
    if type(number) is not int:
        raise Exception("number must be an integer")
    return number ** 0.5



try:
    num = int(input("Enter a number to calculate square root: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result:.2f}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print(e)
            
# assertions

# upon failure, exceptions is raised and program stops immediately
a = 0
assert(a != 0)
print(5//a)

print("Hello World")