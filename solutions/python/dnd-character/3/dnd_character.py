from random import randint
class Character:
    """initializes dnd character traits by sorting 4 dice rolls and removing the lowest value"""
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return sum(sorted([randint(1,6) for roll in (range(4))])[1:])

def modifier(value):
    return (value - 10)//2
    
