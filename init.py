# classes & oop

# help define and build -- objects "instatiate"
# Animals

class Animal:
    # init method -- constructor to initialize object
    '''
    Assign characteristics for each instaniated object
    Age
    Name
    if None, it is optional upon instantiation
    '''

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def __init__(self, type, breed):
        self.type = type
        self.breed = breed
        self.age = None
        self.name = None

    def describe(self):
        description = f"This animal is a {self.type} {self.breed}."
        if self.name is not None:
            description += f" Its name is {self.name}."
        if self.age is not None:
            description += f" Is is {self.age} years old."
        return description


# create instances of the Animal class
    
animal_dog = Animal("Tri-Color", "Shepherd")
animal_owl = Animal("Horned", "Owl")

print(animal_dog.describe())
print(animal_owl.describe())

animal_dog.set_name("Moose")
animal_dog.set_age(3)

animal_owl.set_name("Cookie")
animal_owl.set_age(7)

print(animal_dog.describe())
print(animal_owl.describe())

# Create a Car class

class Car:

    def set_color(self, color):
        self.color = color
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = None
    

    def describe(self):
        color = f"{self.color}" if self.color else ""
        description = f"This Car is a {color} {self.make} {self.model}."
        return description

toyota_car = Car("Toyota", "Camry")
print(toyota_car.describe())


toyota_car.set_color("White")
print(toyota_car.describe())