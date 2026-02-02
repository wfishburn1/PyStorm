# variables

'''
how we store date into name locations
"=" OR reserved keywords
'''

name = "Will"
name_intStat = 3.2
print(type(name))
print(type(name_intStat))
print(name_intStat)

# assign a variable to itself
name_intStat = name_intStat + 75
print(name_intStat)

# ^ Increment / Decrement

name_intStat += 5
print(name_intStat)

name_agiStat = 25
name_agiStat -= 10
print(name_agiStat)
name_isJohnMain = False

# Casting
# Explicity allows the data type to be entered
# has to make sense

name = str("jorn")
print(name)
name_length = int(4)
print(name_length)

# print a string within a string
print("I often say \"I'm blessed, happy and loved\" .")
print('I often say "I am a child of God". ')

# other data types
car_list = ["camaro", "charger", "hemi", "mustang"]
print(type(car_list))
print(car_list)

car_tuple = ("camaro", "charger", "hemi", "mustang")
print(type(car_tuple))
print(car_tuple)

car_dictionary = {"mustang": 7, "camaro": 6, "charger": 7, "hemi": 4}
print(type(car_dictionary))
print(car_dictionary)

car_boolean = True
print(car_boolean)

car_range = range(7)

# list and dictionary mare mutable, tuple is not
# ordered, dictionaries target key:value
# duplictes allowed in lists and tuples, not dictionary 