# Lists

firstList = ["a", "b", "c"]
print(firstList)

listTwo = ["A", 1, 3.5, [2,"d"], [], list(), True]
print(listTwo)
print(type(listTwo))

# Access a list numerically
print(firstList[2])
print(listTwo[5])
print(listTwo[-3])
print(len(listTwo))
print(listTwo[3][0]) # Accessing nested list element

# Modifying lists
listTwo[-1] = False
print(listTwo)

# Add to list
listTwo.insert(2, "3.4")
print(listTwo)
print("\nList Length:", len(listTwo))

del listTwo[3]
print(listTwo)
listTwo.pop()
print(listTwo)

# Appending
# Ideal for not caring about order
listTwo.append("A")
listTwo.append(True)
print(listTwo)

# Methods vs Properties
# what something is vs what something does

# print(max(listTwo))
# print(min(listTwo))

# does the value of "TRUE" exist in listTwo?
print(listTwo.index(True))
print(listTwo.count(3))

# extend a list onto another list
carListOne = ["Juke", "Odssey"]
carListTwo = ["Hyabusa", "Alfa Romeo", "MG Midget"]
print(carListOne)
print(carListTwo)
carListOne.extend(carListTwo)
print(carListOne)

carListTwo.clear()
print(carListTwo)

listFour = [99,98,24,4,36]
print(listFour)
listFour.sort()
print(listFour)
listFour.sort(reverse=True)
print(listFour)

carListTwo = listFour # reference of another
print(carListTwo)
print(listFour)

carListTwo[2] = "Tacoma"
print(carListTwo)
print(listFour)

carListThree = listFour.copy() # makes a copy
print(carListThree)
print(listFour)

carListThree[2] = "Silverado"
print(listFour)
print(carListThree)

# Lists and loops
# For loops for range of elements in a list

listZ = [0, 5, 6, 23, 3, 15]
listAdded = 0

for i in range(len(listZ)):
    listAdded += listZ[i]
    
print(listAdded)