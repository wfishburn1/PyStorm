# data type that represents one of two values: True or False(1 or 0)

is_John_True = True
is_John_False = False

print(is_John_True)
print(is_John_False)
print(bool(1))  # True
print(bool(0))  # False

correct = True
incorrect = False

# is 'correct' NOT TRUE, and is 'incorrect' NOT TRUE?
print(correct != True) # false
print(incorrect != True) # true
print(not correct) # false
print(not incorrect) # true

print(50 == 25)
print((50 == 25) == True)
print(15 < 20)
print(50 < 25)
print(10 <= 20)
print("=======================================")
age = 25
is_John = age >= 21
print(is_John)
# Above evaluates to True if age is 21 or higher

# Conditionals
x = 5
y = 10

if x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is greater than or equal to {y}")

# Logical Operators
sunny = True
warm = False

if sunny and warm:
    print("It's sunny outside")
elif sunny or warm:
    print("It's sunny or warm")
else:
    print("It's neither sunny nor warm...must be Boston")

# Booleans in functions
def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False

# Flow Control
def can_drive(age):
    return age >= 16

age = 9
if can_drive(age):
    print("Tyler can drive!")
else:
    print("Tyler cannot drive yet.")