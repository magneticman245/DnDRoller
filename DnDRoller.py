# program will use regex to interpret input
import re
import random

flag = 0 # this variable is used to define the exit condition of the loop

# welcome message
print('Welcome to DnDRoller. To roll dice, use the following syntax: ')
print('NdS where N is the number of dice to roll, and S is the size of ')
print('the dice. So, to roll 2 dice with 6 sides, type 2d6.')
print('To close the program, type exit.')

# create regex to detect dice input of form <number><letter-d><number>
# the first number, representing the number of dice, is optional
# if this is not present, it will be interpreted as 1 
diceRegex = re.compile(r'(\d+)?d(\d+)')

# program will now enter a loop, so user can keep rolling until they decide
# to stop
while(flag == 0):
    print('Ready to roll:')
    request = input()   # takes user input
    mo = diceRegex.search(request) # searches input for a dice roll
                                   # saves match object in mo variable

    if mo == None: # if no valid dice roll found
        if request.lower() == 'exit': # check for exit command
            flag = 1 # create exit condition for loop
        else:
            # give error message and instructions
            print('Unrecognised syntax. Type your roll in the form NdS, or ')
            print('type exit to close the program.')
            
    else: # this code will only run if a valid roll is found
        number = mo[1] # extract number of dice from match object
        
        # typing the number of dice is optional. need to check if user left
        # mo[1] unspecified
        if number == None:
            number = 1 # number of dice assumed to be 1 if not specified
        else:
            number = int(number) # convert to integer

        size = mo[2] # extract size of dice from match object
        size = int(size) # convert to integer

        # message to confirm to user what is being rolled
        print('Rolling ' + str(number) + 'd' + str(size) + '...')
        
        # iterate over the size of number, to roll that many times
        total = 0 # running total starts at 0
        for i in range(number):
            roll = random.randint(1, size) # generates random roll
            if number != 1: # lists each roll if more than one die to roll
                print('Roll ' + str(i + 1) + ': ' + str(roll)) 
            total = total + roll # keeps running total of rolls

        print('TOTAL: ' + str(total)) # prints total roll

            
