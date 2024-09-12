import random
roll = 0
total = 0
diceNumber = 0
diceType = ''
rollMore = 'yes'
#Prints the final result to the command line.
def printTotal():
    global total
    print(f'The total is {total}!')
    total = 0
#Prompts the user for what dice they want to use and how many to roll.
def getDice():
    global diceNumber, diceType
    print()
    print('What type of dice would you like to roll? (D100, D20, D12, D10, D8, D6, or D4)')
    diceType = input()
    print('How many?')
    diceNumber = input()
    diceNumber = int(diceNumber)
#Does the math for dice rolls. Checks if dice types are valid real-world dice types.
def diceRoller():
    global diceType
    if diceType == 'D100' or diceType == 'D20' or diceType == 'D12' or diceType == 'D10' or diceType == 'D8' or diceType == 'D6' or diceType == 'D4':
        print()
        print(f'Rolling {diceNumber} {diceType}...')
        diceType = diceType[1:]
        diceType = int(diceType)
        while diceNumber > 0:
            global roll, total
            roll = random.randrange(1, diceType + 1)
            total = roll + total
            dicePrinter()
        printTotal()
    else:
        print('Error, Invalid Dice Type! Please Input One Of The Following: D100, D20, D12, D10, D8, D6, or D4.')
#Prints the result of each dice roll and controls the number of rolls.
def dicePrinter():
    global diceNumber
    diceNumber = diceNumber - 1
    print(roll)
#Runs at the end of dice rolls. Controls the rollMore variable. Checks for valid inputs.
def quitPrompt():
    print()
    print('Would you like to roll more dice? (yes/no)')
    global rollMore
    rollMore = input()
    if rollMore != 'yes' and rollMore != 'no':
        print('Error, "yes" or "no" expected.')
        quitPrompt()
print()
print("Welcome to Lad's Dice Roller!")
#Runs until the rollMore variable is set to 'no'.
while rollMore == 'yes':
    getDice()
    diceRoller()
    quitPrompt()
