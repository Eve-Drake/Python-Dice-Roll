import random

def diceRoll(numberOfDice):
    i = 0
    howManySides = int(input('How many sides?'))
    rolls = []
    while i < numberOfDice:
        die = random.randint(1, howManySides)
        rolls.append(die)
        i += 1
    return rolls


def getNumberDice():
    try:
        number = int(input('How many Dice do you wish to Roll?'))
        diceRoll(number)
    except ValueError:
        print('Please enter a whole number')
        getNumberDice()

