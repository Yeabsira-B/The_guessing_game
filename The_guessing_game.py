

import random
num = random.randint(num(1,100))
# the code above generates random numbers between 1 and 100
# the next code will be assigning a variable for the guess,
user_guess = int(input("Welcome to the guessing game! Please guess a number between 1 and 100: "))
#the above line will display an input box for the user to enter their guess
while user_guess != num:
#while loop to keep the game running until the user guesses the correct number
    if user_guess < num:
        print("Your guess is low, try again!")
        user_guess = int(input("Enter your next guess: "))
    else:
        print("Your guess is high, try again!")
        user_guess = int(input("Enter your next guess: "))



