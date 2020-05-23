# DnDRoller

A simple program for rolling dice, for tabletop RPGs.

Written in Python 3.8.2

Author: Dan Mott



HOW DOES IT WORK?

This program takes input of the form NdS, where N is the number of dice to roll, and S is the size of the dice. It interprets the user input using a regular expression, and generates a random number from 1 to the value of S. This is done N times, and the total of all 'rolls' is displayed.

The user can then type a new roll, repeating until the program is closed.

For example, inputting 2d6 would generate a random number from 1 to 6 twice, sum the results and output the total. The output may look something like:

    Rolling 2d6...
    
    Roll 1: 4
    
    Roll 2: 1
    
    TOTAL: 5

As Regex are used to detect the NdS syntax, the program is capable of detecting a roll even if the user types other things around it.

For example, the following two inputs are interpreted exactly the same way:

    2d6
    
    Please roll 2d6, thank you.

If no valid roll is detected, the program will print an error message reminding the user of how to format their input.



NEW FEATURE (LATEST COMMIT)

Add modifiers to rolls. To do this, append your input with a plus (+) or minus (-) followed by the value to add or subtract. The program will detect this and add or subtract from the total roll.

This is useful for making ability checks or rolling damage, as you can add appropriate modifiers when you roll, and see straight away what your result is. For example, see the input:

    2d6+2

This could produce the following output:

    Rolling 2d6...

    Roll 1: 4

    Roll 2: 1

    TOTAL (+2): 7

To close the program, simply type 'exit'.



LIMITATIONS

At the present time, the program will only detect the first valid dice roll in the input field. Consider the input:

    2d6 3d8
    
In this case, the first roll of 2d6 would be detected and the second roll 3d8 would be ignored.

PLANNED FEATURES

Future features include rolling multiple types of dice at once. For example, the user could type the following input:

    2d6+2d8
    
which would output something like this:

    Roll 1(d6): 4
    
    Roll 2(d6): 2
    
    Roll 3(d8): 1
    
    Roll 4(d8): 7
    
    TOTAL: 14


The Regex used to interpret the input cannot cope with whitespace in the input field. This in particular is noticeable when modifying the roll, as one may be tempted to type 2d6 +2, rather than 2d6+2. At the moment, the first of those options will not be detected by the Regex. 

In the future, the plan is to make the Regex more forgiving with regards to whitespace, and extraneous explanation, in the input, so any of the following would be accepted identically:

    2d6+2
    2d6 +2
    2d6 + 2
    2 d6+ 2
    2 d6 and +2