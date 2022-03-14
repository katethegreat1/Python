# Shut the box game, made by Chris Hanley.

# Required for rolling dice
import random
# To use time.sleep function
import time
# For colouring output text
from colorama import Fore, Back, Style

full_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
current_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Function to repopulate the board between games.
def refresh_board():
    global current_board
    if len(current_board) == 0:
        current_board.append('1')
        current_board.append('2')
        current_board.append('3')
        current_board.append('4')
        current_board.append('5')
        current_board.append('6')
        current_board.append('7')
        current_board.append('8')
        current_board.append('9')
    return current_board


# Function that throws the dice, stores the values of the dice
def dice_throw():
    # Variables that are storing the value of the dice, dice values are converted to strings to match what user input
    # will be.
    dice_throw.dice_1 = str(random.randrange(1, 7))
    dice_throw.dice_2 = str(random.randrange(1, 7))
    dice_throw.total = int(dice_throw.dice_1) + int(dice_throw.dice_2)
    dice_throw.total_str = str(dice_throw.total)
    print('\nRolling now...')
    time.sleep(0.3)
    print('You rolled...')
    # Fancy dice.
    print(" -----------" + '   ' + "-----------")
    print("|           |" + ' ' + "|           |")
    print("|           |" + ' ' + "|           |")
    print("|    ", dice_throw.dice_1, "    |" + ' ' + "|    ", dice_throw.dice_2, "    |")
    print("|           |" + " " + "|           |")
    print("|           |" + ' ' + "|           |")
    print(" -----------" + ' ' + "  -----------")
    return [dice_throw.dice_1, dice_throw.dice_2, dice_throw.total_str]

# Function to output current board to use
def output_board():
    output_string = "\t"
    print('\nYour board is currently: ')
    for number in full_board:
        if number in current_board:
            output_string = output_string + str(number) + "   "
        else:
            output_string = output_string + "    "
    print(Fore.BLUE + Style.BRIGHT + output_string)
    print(Style.RESET_ALL)
    return output_string

def invalid_input():
    print(Fore.RED + Style.BRIGHT + "\nItems not on board or invalid input.")
    print(Style.RESET_ALL)
    time.sleep(0.5)
    return


# Function for closing credits
def closing_credits():
    print('''
        _______            
      /\\       \\           
     /()\\   ()  \\          
    /    \\_______\\         
    \\    /()     /         
     \\()/   ()  /          
      \\/_____()/

        _______            
      /\\       \\           
     /()\\   ()  \\          
    /    \\_______\\         
    \\    /()     /         
     \\()/   ()  /          
      \\/_____()/
  
    ''')

    print("Created by Chris Hanley 2021, with modifications for use in class")


# Main game code
def update_board():
    if start_game == "y":
        playing_game = True
    turns = 0
    # Check sentry variable playing_game, while True game runs. Also checks the length of current board does not
    # equal 0 (another rule for game to play)
    while playing_game is True and len(current_board) != 0:
        turns = turns + 1
        # Show player their current board
        # Make player interact with game by pressing Enter
        # Calls the dice_throw function and stores its data in the current_go variable (to test valid moves by user)
        current_go = dice_throw()
        output_board()
        # Ask player for their move, option to quit and roll again.
        player_move = input('Enter the number(s) you wish to remove from your board, Press enter to roll again or q '
                            'to quit: ')
        # Checks player move, using length and checking that their move is valid by using the current_go variable.
        if len(player_move) == 0:
            print('Skipping move..')
            time.sleep(0.3)
        elif len(player_move) == 1:
            if player_move in current_go and player_move in current_board:
                current_board.remove(player_move)
                if player_move not in current_go:
                    invalid_input()
            elif player_move == 'q':
                playing_game = False
                print('Thanks for playing, returning you to main menu.')
                time.sleep(0.4)
            else:
                invalid_input()
        elif len(player_move) == 2:
            if player_move[0] in current_go and player_move[0] in current_board and player_move[1] in current_go and player_move[1] in current_board:
                current_board.remove(player_move[0])
                current_board.remove(player_move[1])
                if player_move[0] not in current_go and player_move[1] not in current_go:
                    invalid_input()
            else:
                invalid_input()
        else:
            invalid_input()
    # Program checking if the current board length is 0, If True updates game_running sentry variable and prints to
    # user amount of turns they took to finish the game
    if len(current_board) == 0:
        # playing_game = False
        print('\nYou took {} turns to complete the game.'.format(turns))
        refresh_board()


# Main body of code
print("Welcome to shut the box!")

game_running = True
# Checks the sentry variable game_running, and loops while game_running is True
while game_running:
    time.sleep(0.1)
    # Collect user choice from main menu
    choice = input("""\nPlease make a selection:
                   Play the game (p)
                   View the rules (r)
                   Finish playing (q)
                   Selection: """)
    # Check what the user has inputted, for each possible input it does something, if input isn't valid tells them to
    # enter valid input.
    if choice == "r":
        time.sleep(0.1)
        print(
            '\nTwo dice will be rolled, you can add the values of the two dice to remove a tile, or use each dice '
            'individually to remove one or two tiles.\nIf you roll the dice and cannot make use of either of the '
            'values, you can ask for the dice to be rolled again.')
    elif choice == "q":
        game_running = False
    elif choice == "p":
        start_game = "y"
        update_board()
    else:
        print("\nPlease make a valid selection from the menu. Press q to finish playing.")

# Goodbye message printed when exit the while loop
closing_credits()
