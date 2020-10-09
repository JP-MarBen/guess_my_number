
"""
Spyder Editor

This is a temporary script file.
"""

import random

MIN=0
MAX=1000

if __name__=='__main__':
    number_to_guess=random.randint(MIN, MAX)
    print("Try to guess a number between %d and %d" % (MIN,MAX))
    
    while True:
        user_input=input("Your guess?")
        try:
            user_attempt=int(user_input)
            if user_attempt==number_to_guess:
                print("Bravo!")
                break
            elif user_attempt < number_to_guess:
                print("too low!")
            else:
                print("too high!")
        except ValueError:
