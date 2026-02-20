from random import randint
class Character:
    #initializes dnd character traits by sorting 4 dice rolls and removing the lowest value
    def __init__(self):
        self.strength = sum(sorted([randint(1,6) for roll in (range(4))])[1:])
        self.dexterity = sum(sorted([randint(1,6) for roll in (range(4))])[1:])
        self.constitution = sum(sorted([randint(1,6) for roll in (range(4))])[1:])
        self.intelligence = sum(sorted([randint(1,6) for roll in (range(4))])[1:])
        self.wisdom = sum(sorted([randint(1,6) for roll in (range(4))])[1:])
        self.charisma = sum(sorted([randint(1,6) for roll in (range(4))])[1:])
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return sum(sorted([randint(1,6) for roll in (range(4))])[1:])

def modifier(value):
    return (value - 10)//2
    
