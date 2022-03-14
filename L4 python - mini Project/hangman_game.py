import random
#below is a list of multiline strings which contains 7 elements which make up the different stages of your hangman game
hangman_parts = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


game_in_progress = True
current_attempts = 0


#below we have a while loop that will run the game till there are no more pieces of hangman to display or if user enters yes
while game_in_progress:
    
    print(hangman_parts[current_attempts])
    current_attempts += 1   
    user_guess = input("Is the game over? : ")
    
    if user_guess == "yes":
        print("oh ok then, bye")
        game_in_progress = False        
    elif current_attempts < len(hangman_parts):
        print("cool story bro")     
    else:
        print("mate the game is over, accept it")
        game_in_progress = False