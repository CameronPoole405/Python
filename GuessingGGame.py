'''
Program: GuessingGame.py
Author: Delta9C
Date: 10/15/2020
Summary:
    I hope this doesn't fail.
'''
import random

print("Welcome to the guessing game. Try to guess my secret number in under 5 tries")
myNumber = random.randint(1, 10)
count = 0

while count < 5:
    userGuess = int(input("Enter a guess: "))
    count += 1
    if userGuess > 10:
        print("Error: You've tried to guess a number larger than 10. Big oof.")
    elif userGuess < 0:
        print("Error: You've tried to guess a number lower than 0... Bigger oof")
    else:
        if userGuess > myNumber:
            difference = userGuess - myNumber
            print("Nice try, your guess was too high")
        elif userGuess < myNumber:
            difference = myNumber - userGuess
            print("Nice try, your guess was too low")
        elif userGuess == myNumber:
            print("Congradulations, you've won!")
        else:
            break
print("You've failed, Anakin")
