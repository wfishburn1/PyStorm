# Import Module
def hoot():
    print("Hoot! Hoot!")

class OwlIdentifier:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def greeting(self):
        return f"Hello I am {self.name},  {self.type} owl!"