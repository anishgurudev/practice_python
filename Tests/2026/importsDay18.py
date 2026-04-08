# from math import pi , tau
# print(globals())
#
# import numpy as np
# print(globals())
#
# from math import *
# print(globals())

#Exercises
#1) Import the fractions module and create a Fraction
# from the float 2.25. You can find information on
# how to create fractions in the documentation.

import fractions
# fractions.Fraction(2.25)
print(fractions.Fraction(2.25))

#2) Import only the fsum function from the math module and
# use it to find the sum of the following series of floats.

from math import fsum
numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))

# 3)Import the random module using an alias, and find a random
# number between 1 and 100 using the randint function.
import random as rndm

print(rndm.randint(1,100) )

#4) Use the randint function from the exercise above to create
# a new version of the guessing game we made in day 8. This time
# the program should generate a random number, and you should
# tell the user whether their guess was too high, or too low, until they get the right number.

target_number = rndm.randint(1,5)

guess = int(input("Guess a number: "))

while guess!= target_number:
    if guess > target_number:
        print(f"Too High ")
    else:
        print("too low")
    print(f"Wrong Guess! {target_number} ")
    guess = int(input("Enter another number: "))

print(f"You guess correctly {target_number} ")
