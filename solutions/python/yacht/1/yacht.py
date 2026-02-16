# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 31
CHOICE = 9


def score(dice, category):
    four = [1,2,3,4,5]
    four2 = [2,3,4,5,6]
    sort1 = sorted(dice)
    if category in [50, 30, 31]:
        if len(set(dice)) == 1 or (sort1 == four and category == 30):
            return category
        if category == 31 and sort1 == four2:
            return 30
        return False
    if category in [1,2,3,4,5,6]:
        cat = [x for x in dice if x == category]
        return len(cat)*category
    #Handles Full house and choice
    if (category == 7 and dice.count(sort1[0]) in [2,3] and len(set(dice)) == 2) or category == 9:
        return sum(dice)
    #Handles 4k
    if category == 8 and (dice.count(sort1[0]) in [4,5] or dice.count(sort1[-1]) in [4,5]):
        fourK = [x for x in dice if dice.count(x) in [4,5]]
        return fourK[0] * 4
    return False
