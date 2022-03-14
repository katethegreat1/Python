# This is the Guess My Number project.
# Made by Qian Han on 16/09/2021

# Let the computer choose a number between 1 and 100.

import random
number = random.randint(1,100)

# Welcome the player and set up the rule.

print("Welcome to Guess My Number! \n")
print("I've got a number between 1 and 100. \n")

# Loop while the number has not been guessed correctly.

number_not_guessed = True
trial = 1


# Get a guess from the player

while number_not_guessed:
    guess_number = int(input("Guess my number - "))
    
    # After each guess, the computer will give the player a hint by saying “Lower!” or “Higher!” or "You win" if it's correct. 
    
    if guess_number > number:
        print("Lower!")
        trial += 1
        
    elif guess_number < number:
        print("Higher")
        trial += 1
        
    else:
        print("Congratulations, you win! \n")
        print("You made "+ str(trial) + " guesses.")
        
        # Break the loop if the player wins.
        
        number_not_guessed = False        
      
# End the game by saying "Goodbye!" to the player.

print("Goodbye!")