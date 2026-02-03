# Conditionals & Loops

# Linear - left to right, top to bottom
# Stop on True 

if True:
    print("True")

if False:
    print("False")

if not False:
    print("Not False")

if 1 < 1:
    print("1 < 1")
elif 1 <= 1:
    print("1 is less than or equal to 1")
else:
    print("Otherwise false")

# Combine comparisons
# Combination of operators MUST EQUAL TO TRUE
# AND OR

if 5 > 4 and 3 < 4:
    print("5 is greater than 4 AND 3 is less than 4")

# parenthesis
if (5 > 10 or 5 < 10) and 1 == 1:
    print("5 is less than 10 and 1 is equal to 1")

# Ternary Operator
# Combine syntax into a one line conditional
# if 1 >=1:
#    print("1 is >= 1")
# else:
#    print("1 is <= 1")
print("1 is >= 1") if 1 >= 1 else print("1 is < 1")

""" # Nested IF
temp = float(input("What is the temperature outside? "))
humidity = float(input("What is the humidity outside? "))

if temp > 70:
    if humidity > 70:
        weather = "Hot and Humid"
        print(weather)
    else:
        weather = "Hot"
        print(weather)
else:
    if humidity > 50:
        weather = "Humid"
        print(weather)
    else: 
        weather = "Cool and Dry"
        print(weather)
 """

# Loops
# while, for, and "Nested"

# while
# UNTIL condition is FALSE
""" x = 5
while x < 10:
    print(x)
    x += 1

while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input == 'q':
        break
    print(f"You have entered {user_input}.")
 """
# For
# excecution by number of times

cars = ("69 Charger", "67 Shelby", "72 Camaro SS")
for car in cars:
    print(cars)

for i in (0, 1, 2, 3, 4):
    print(i + 2)

# range
for i in range(5): # 0,1,2,3,4
    print(i + 4)

# Nested Loops
for i in range(5):
    for j in range(5):
        print(f"({i}, {j})")

# Break
# user wants to exit loop once condition is met
for i in range(10):
    if i == 3:
        break
    print(i)

# finding the first even number greater than x
for i in range(3, 27):
    if i % 2 == 0:
        print(f"The first even number greater than 3 is {i}")
        break

# Keep the loop alive despite condition met.. skip the condition
for i in range(5):
    if i == 3:
        continue
    print(i)

# Print even number from 1 to 10 using continue
for i in range(1, 11):
    if i % 2 == 1: # SKIP ODD NUMBERS
        continue
    print(i)

# pass