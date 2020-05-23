# program will use regex to interpret input
import re
import random

flag = 0 # this variable is used to define the exit condition of the loop

# welcome message
print('Welcome to DnDRoller. To roll dice, use the following syntax: ')
print('NdS where N is the number of dice to roll, and S is the size of ')
print('the dice. So, to roll 2 dice with 6 sides, type 2d6.')
print('\nTo add a modifer, type + or - followed by the value you')
print('want to add or subtract.')
print('\nTo close the program, type exit.')

# create regex to detect dice input of form <number><letter-d><number>
# the first number, representing the number of dice, is optional
# if this is not present, it will be interpreted as 1.
# will also detect optional modifier value, + or - an integer.
diceRegex = re.compile(r'(\d+)?d(\d+)(\+|\-)?(\d+)?')

# program will now enter a loop, so user can keep rolling until they decide
# to stop
while(flag == 0):
    modflag = 0 # flag tracks if current roll has a modifier
    print('Ready to roll:')
    request = input()   # takes user input
    mo = diceRegex.search(request) # searches input for a dice roll
                                   # saves match object in mo variable

    if mo == None: # if no valid dice roll found
        if request.lower() == 'exit': # check for exit command
            flag = 1 # create exit condition for loop
        else:
            # give error message and instructions
            print('Unrecognised syntax. Type your roll in the form NdS+M, or ')
            print('type exit to close the program.')
            
    else: # this code will only run if a valid roll is found
        number = mo[1] # extract number of dice from match object
        
        # typing the number of dice is optional. need to check if user left
        # mo[1] unspecified
        if number == None:
            number = 1 # number of dice assumed to be 1 if not specified
        else:
            number = int(number) # convert to integer

        size = int(mo[2]) # extract size of dice from match object and convert to int

        # message to confirm to user what is being rolled
        print('Rolling ' + str(number) + 'd' + str(size) + '...')
        
        # iterate over the size of number, to roll that many times
        total = 0 # running total starts at 0
        for i in range(number):
            roll = random.randint(1, size) # generates random roll
            if number != 1: # lists each roll if more than one die to roll
                print('Roll ' + str(i + 1) + ': ' + str(roll)) 
            total = total + roll # keeps running total of rolls

        # now check for any modifiers to the roll
        if mo[3] != None: # implies + or - detected
            if mo[4] != None: # implies modifier value detected
                # if both conditions true, a valid modifer has been found
                modflag = 1 # flags that this roll has a modifer
                operator = mo[3] # detects whetherto add (+) or subtract (-)
                modifier = int(mo[4]) # detects value of modifier 
                                
                # now add or subtract modifier depending on detected operator
                if operator == '+':
                    total = total + modifier
                else:
                    total = total - modifier

                # print modified total
                print('TOTAL (' + str(operator) + str(modifier) + '): ' + str(total))
                
        # if roll unmodified, print total
        if modflag == 0:
            print('TOTAL (+0): ' + str(total)) # prints total roll
