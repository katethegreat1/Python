# Word jumble with functions

import random

################################
# Functions

def display_instructions():
    """ This function displays the instructions """
    print("This program jumbles up a word and you have to guess what the word is.\nLet's play. q to quit.")
    
def string_to_list(word_string):
    """ This function takes a string and returns a list of letters """
    output_list = list(word_string)
    return output_list

def list_to_string(word_list):
    """ This function takes a list of letters and returns a string """
    output_string = "".join(word_list)
    return output_string

def format_message(message):
    """ This function takes a string and formats it into an output message"""
    pass

def goodbye_message():
    """ This function displays the goodbye credits"""
    print("Goodbye!")

################################
# Main body of code


# sequence of words to choose from
WORDS = ["jumble", "washing", "spatula", "answer", "zylophone"]
shuffled_word_string = ""

# Welcome message and instructions 
print("Hello, and welcome to word jumble \n")
display_instructions()


while True:
    # choose a word at random from the list
    word_string = random.choice(WORDS)

    # turn word into a list  of letters
    word_list = string_to_list(word_string)

    # shuffle the letters in list
    random.shuffle(word_list)

    # convert shuffled letters to one string
    shuffled_word_string = list_to_string(word_list)


# Print jumbled word to screen    print("Here is your word:")
    print(shuffled_word_string)
    print("\n")

    trial = 0
    while True:
        
        # Loop waiting for correct guess or q to quit

        guess = input("What is the word? (or q to quit) ")
        trial += 1
        
        if guess == word_string:
            print("\n******************************")
            print("Congratulations - that's correct!")
            print("You guessed " + str(trial) + " times.")
            print("******************************")
            break
               
        elif guess == "q":
            goodbye_message()
            exit()
            
        else:
            print("Please try again")


  
