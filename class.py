import random

class Jorn:
    '''
    represent a BASIC mmorpg class
    '''

    def __init__(self, name, char_class):
        '''
        Docstring for __init__
        
        name = name of char
        char_class = 'mage', 'warrior'
        '''

        self.name = name
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.health = 100
        self.mana = 150 if char_class == 'Mage' else 50
        self.strength = 15 if char_class == 'Warrior' else 5
        self.intelligence = 15 if char_class == 'Mage' else 5


    def level_up(self):
        '''
        Increase char lvl and attr once enough exp is reached
        '''
        if self.experience >= self.level * 100: # exp points per lvl
            self.level +=1
            self.experience = 0
            self.health += 20
            self.mana += 20 if self.char_class == 'Mage' else 10
            self.strength += 10 if self.char_class == 'Warrior' else 5
            self.intelligence = 10 if self.char_class == 'Mage' else 5
            print(f"{self.name} leveled up to level {self.level}!")

    def attack(self, target):
        '''
        Perform an attack by targeting
        '''

        if self.char_class == 'Warrior':
            damage = self.strength + random.randint(1, 5)
            target.health -= damage
            print(f"{self.name} attacks attacks {target.name} with Greatsword for {damage} damage!")
        elif self.char_class == 'Mage':
            if self.mana >= 10:
                damage = self.intelligence + random.randint(5, 10)
                target.health -= damage
                self.mana -= 5
                print(f"{self.name} casts Fireball at {target.name} for {damage} damage!")
            else: 
                print(f"{self.name} does not have enough mana to cast! RUN!!!")

    def gain_exp(self, amount):
        '''
        inc char's exp points
        '''
        self.experience += amount
        print(f"{self.name} gains {amount} experience points.")
        self.level_up() # check for lvl up after gain #

if __name__== "__main__":
    hero = Jorn("JornHelmBreaker", "Warrior")
    enemy = Jorn("Odinson", "Mage")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.gain_exp(50)
    hero.gain_exp(60)
