# scopesdemo.py

def functionOne():
    variable = 123
    return variable

functionPrint = functionOne()
print(functionPrint)

# Extend variables scope to include the function body
# global

def functionTwo():
    global dontChangeMe
    dontChangeMe = 7
    print(dontChangeMe)

dontChangeMe = 5
functionTwo()
print(dontChangeMe)