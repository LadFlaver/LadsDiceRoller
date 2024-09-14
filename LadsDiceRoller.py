import random
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
    global diceType
    print()
    diceType = input('What type of dice would you like to roll? (D100, D20, D12, D10, D8, D6, or D4): ')
    if diceType.upper() not in ['D100', 'D20', 'D12', 'D10', 'D8', 'D6', 'D4']:
        print()
        print('Error, Invalid Dice Type! Please input one of the following: D100, D20, D12, D10, D8, D6, or D4.')
        getDiceType()

#Gets the number of dice the user wants to roll and validates it.
def getDiceNumber():
    global diceNumber, rollAgainNumber
    print()
    try:
        diceNumber = int(input('How many?: '))
    except:
        print()
        print('Error, integer value expected!')
        getDiceNumber()
    rollAgainNumber = diceNumber
    
#Performs dice math and prints the results.
def diceRoller():
    global diceType, diceNumber
    print()
    print(f'Rolling {diceNumber} {diceType.upper()}...')
    diceType = diceType[1:]
    diceType = int(diceType)
    total = 0
    while diceNumber > 0:
        diceNumber = diceNumber - 1
        roll = random.randrange(1, diceType + 1)
        total = total + roll
        print(roll)
    print(f'The total is {total}!')

#Checks if the user wants to roll again with the same dice set previously used.
def rollAgainPrompt():
    global diceNumber, rollAgainNumber
    print()
    rollAgain = input('Do you want to roll again? (y/n): ')
    if rollAgain in 'y':
        global diceType
        diceType = f'D{diceType}'
        diceNumber = rollAgainNumber
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

main()
