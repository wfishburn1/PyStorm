# Dictionaries

dictionaryOne = {"one:":1, "two:":2, "three:":3}
print(dictionaryOne)
print(dictionaryOne["two:"])

spirit_animal = {"Hamster": "Dallas", "Owl":"Dave", "Dog": "John"}
empty_dictionary = {}

print(empty_dictionary)
print(spirit_animal['Owl'])

print(spirit_animal.get("Dog"))
print(spirit_animal.keys())
print(spirit_animal.values())

# Adding to a dictionary
spirit_animal["Lion"] = "Bob"
print(spirit_animal)
spirit_animal.update({"Wolf": "Karen"})
print(spirit_animal)
spirit_animal["Wolf"] = "Rocky"
print(spirit_animal)

# Delete from a dictionary
del spirit_animal['Wolf']
print(spirit_animal)
spirit_animal.pop("Hamster")
print(spirit_animal)

# Nested dictionaries
spirit_animal['Lion'] = {"a":1, "b":2}
print(spirit_animal)

# Is/Is Not Loop to check dictionaries
japanese_numbers = {
    "one": "ichi",
    "two": "ni",
    "three": "san",
    "four": "shi",
    "five": "go"
}

translations = ['three', 'four', 'five']
for translation in translations:
    if translation in japanese_numbers:
        print(translation, "-->", japanese_numbers[translation])
    else:
        print(translation, "is not in japanese_numbers")

# keys() and values()
spirit_animal = {"Hamster": "Dallas", "Owl":"Dave", "Dog": "John"}

for key in spirit_animal.keys():
    print(key, "--->", spirit_animal[key])

for value in spirit_animal.values():
    print(value)