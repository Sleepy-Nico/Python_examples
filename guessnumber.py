##
#välja tal

import random
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



CorrectNumber = random.choice(list1)
numOfGuesses = 3

#be om siffra

while(numOfGuesses > 0):
    print("Guess a number")
    Guess = int(input())
    print("You guessed ")
    print(Guess)
    

    numOfGuesses -= 1
    #kolla om siffran är större, mindre eller lika

    if(Guess > CorrectNumber):
        print("You guessed to large, try again.")

    elif(Guess < CorrectNumber):
        print("You guessed to low, try again.")
    else:
        print("You guessed it!")
        numOfGuesses = 0



#gör 3 gånger

