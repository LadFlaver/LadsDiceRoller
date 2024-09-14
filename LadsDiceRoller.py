import random

class diceVars:
    diceType = ''
    diceNumber = 0
    rollAgainNumber = 0

def main ():
    getDiceType()
    getDiceNumber()
    diceRoller()
    rollAgainPrompt()
    quitPrompt()

#Gets the type of dice the user wants to roll and validates it.
def getDiceType():
    print()
    diceVars.diceType = input('What type of dice would you like to roll? (D100, D20, D12, D10, D8, D6, or D4): ')
    if diceVars.diceType.upper() not in ['D100', 'D20', 'D12', 'D10', 'D8', 'D6', 'D4']:
        print()
        print('Error, Invalid Dice Type! Please input one of the following: D100, D20, D12, D10, D8, D6, or D4.')
        getDiceType()

#Gets the number of dice the user wants to roll and validates it.
def getDiceNumber():
    print()
    try:
        diceVars.diceNumber = int(input('How many?: '))
    except:
        print()
        print('Error, integer value expected!')
        getDiceNumber()
    diceVars.rollAgainNumber = diceVars.diceNumber

#Performs dice math and prints the results.
def diceRoller():
    print()
    print(f'Rolling {diceVars.diceNumber} {diceVars.diceType.upper()}...')
    diceVars.diceType = diceVars.diceType[1:]
    diceVars.diceType = int(diceVars.diceType)
    total = 0
    while diceVars.diceNumber > 0:
        diceVars.diceNumber = diceVars.diceNumber - 1
        roll = random.randrange(1, diceVars.diceType + 1)
        total = total + roll
        print(roll)
    print(f'The total is {total}!')

#Checks if the user wants to roll again with the same dice set previously used.
def rollAgainPrompt():
    print()
    rollAgain = input('Do you want to roll again? (y/n): ')
    if rollAgain in 'y':
        diceVars.diceType = f'D{diceVars.diceType}'
        diceVars.diceNumber = diceVars.rollAgainNumber
        diceRoller()
        rollAgainPrompt()
    elif rollAgain not in ['y', 'n']:
        print("Error, 'y' or 'n' expected.")
        rollAgainPrompt()

#Checks if the user wants to quit the program.
def quitPrompt():
    print()
    quitConfirmation = input('Would you like to quit the application? (y/n): ')
    if quitConfirmation in 'n':
        main()
    elif quitConfirmation not in ['y', 'n']:
        print("Error, 'y' or 'n' expected.")
        quitPrompt()
    else:
        quit()

print("Welcome to Lad's Dice Roller!")
main()
