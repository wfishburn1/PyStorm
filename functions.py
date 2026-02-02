# functions.py
 
'''
block of reusable code 
runs when we call it
avoid human errors
'''

# def functionname(args for function)
#   bodyoffunction

# functionname(valuetopasstofunction)

def hello():
    print("Hello from the world of functions")

hello()

def functionReturn():
    return "Hello from functionReturn"

function_is_returned = functionReturn()
print(function_is_returned)

'''pass "x" into a function

But for x to mean something, it has to accept parameter
'''

def functionValuePass(x):
    print("\t{}".format(x))

functionValuePass("parameter")

def functionMultiValue(x1, x2):
    print(x1, x2)

functionMultiValue("x1", (2+1))

# Nested Functions
# Create teh first function
# Then call it into the second with a msg

def nestedFunction():
    print("Hello from nested function")

def nestedCall():
    nestedFunction()
    print("Hello from nested call")

nestedCall()