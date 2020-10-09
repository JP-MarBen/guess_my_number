
"""
Spyder Editor

This is a temporary script file.
"""

import random

MIN=0
MAX=1000

class GuessMachine():
    '''
    I have a number in mind,
    you have to guess it !!
    
    +self.number_to_guess is generated during creation of the object
    + use'guess(num)' method to make a guess
    +I'll count  the number of attempt in self.number_of_attempt
    '''
    
    def __init__(self):
        
        self.number_to_guess=random.randint(MIN,MAX)
        self.number_of_attempt=0
    
    def guess (self,num):
        '''
        Attempt to find the right number
        it returns 'too high', 'too low', 'found'
        '''
        
        self.number_of_attempt +=1
        if num < self.number_to_guess:
            return 'too low'
        elif num> self.number_to_guess:
            return 'too high'
        else:
            return 'found'
        
if __name__=='__main__':
    
    guess_nachine=GuessMachine()
    print("Try to guess a number between %d and %d" % (MIN,MAX))
    
    while True:
        user_input=input("Your guess?")
        try:
            user_attempt=int(user_input)
            result=guess_nachine.guess(user_attempt)
            if result=='found':
                print("Bravo! you found the number I had in mind in %d attempts!" % guess_nachine.number_of_attempt)
                break

            else:
                print(result)
        except ValueError :
            print("You joker ... that was not an integer! ")
