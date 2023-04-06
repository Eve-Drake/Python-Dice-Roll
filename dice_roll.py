import random

def diceRoll(numberOfDice):
    i = 0
    rolls = []
    while i < numberOfDice:
        die = random.randint(1, 6)
        rolls.append(die)
        i += 1
    print(rolls)


def getNumberDice():
    try:
        number = int(input('How many Dice do you wish to Roll?'))
        diceRoll(number)
    except ValueError:
        print('Please enter a whole number')
        getNumberDice()

