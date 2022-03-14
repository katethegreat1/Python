# This is my RPG game project.
# Made by Qian Han on 28/10/2021

import time
import random
from colorama import Fore

greetings = ["Heeey, baaaaabes!", "I like your face.", "Why, hello there!", "I'm Batman.", "I come in peace!"]
goodbyes = ["Goodbye!", "Don't go!", "Stay with me!", "Go away!", "I hate your face!", "I still like your face."]
hero_inventory = ["Healing potion", "Red gem", "Sword", "Armour"]

# Function to format text and output to the screen
def speak(quote):    
    print(Fore.CYAN, "\t \t \t \t ", quote, Fore.RESET, "\n")

# Function for game play
def guess_my_number():
    number = random.randint(1,100)
    
    global trial  # Declared as global

    speak("I've though of a number between 1 and 100, you have 10 trys to guess it")
    time.sleep(1)
    speak("If you guess correctly you will win my Magic Pen and it will be added to your inventory")
    # Get a guess from the player
    
    trial = 1
    
    while True:
        try:
            guess_number = int(input("Make your guess "))
                
        except:
            speak("Please choose a number from 1-100.")
            
        else: # After each guess, the computer will give the player a hint by saying “Lower!” or “Higher!”.
            if guess_number > number:
                speak("Lower!")
                trial += 1
                
            elif guess_number < number:
                speak("Higher")
                trial += 1
                
            else:
                # Break the loop if the player wins.
                break
            
def closing_credits():
    print ("""
    へ　　　　　／|
　　/＼7　　　 ∠＿/
　 /　│　　 ／　／
　│　Z ＿,＜　／　　 /`ヽ
　│　　　　　ヽ　　 /　　〉
　 Y　　　　　`　 /　　/
　ｲ●　､　●　　⊂⊃〈　　/
　()　 へ　　　　|　＼〈
　　>ｰ ､_　 ィ　 │ ／／
　 / へ　　 /　ﾉ＜| ＼＼
　 ヽ_ﾉ　　(_／　 │／／
　　7　　　　　　　|／
　　＞―r￣￣`ｰ―＿""")
    
    print("Kate Han is the best!")

# Set the scene
print("There is a pirate coming down the road")

# Menu loop
while True:
    # Get menu choice
    time.sleep(1)
    option = input("What would you like to do?\n1 to greet, 2 play a game of chance, 3 to walk on: ")

    # Menu option 1 code (greeting)
    if option == "1":
    
        greeting = input("Type in your greeting ")
        time.sleep(1)
        speak(random.choice(greetings))
        
    # Menu option 2 code (game)  
    elif option == "2":
        
        if hero_inventory == []:      # If you lost everything, you can not play again.
            speak("Sorry babe, you are not allowed to play again as you've already lost everything. Go home and cry.")
       
        else:
            time.sleep(1)
            speak("I do like a good game of chance...")
            time.sleep(1)
            speak("I have a Magic Pen that we can play for. Enter the item you will wager: ")
            time.sleep(1)
            wager = input("This is your inventory " + str(hero_inventory) +" ")
            
            if wager not in hero_inventory:
                speak("That is not in your inventory.")
                time.sleep(1)
                
            else:
                time.sleep(1)
                speak("That is acceptable, let's play")
                print("*"*90)
                time.sleep(1)
                guess_my_number()
                
                if trial <= 10:
                    hero_inventory.append("Magic Pen")
                    speak("Darn it!!!... you win in... " + str(trial) + " guesses!")
                    print("The magic Pen has been added to your inventory")
                    print("This is your inventory now ", hero_inventory, "\n")
                    speak("Arggh! I wish you had never come across my path!")
                    
                else:
                    hero_inventory.remove(str(wager))
                    speak("Ha! You had "+ str(trial) + " guesses! You lose!")
                    print("The " + wager + " has been removed to your inventory")
                    print("This is your inventory now ", hero_inventory, "\n")
                    speak("Yay! Thank you for you " + wager + "!")
    
    # Menu option 3 code (leaving)
    elif option == "3":
        goodbye = input("What would you like to say on leaving? ")
        time.sleep(1)
        print()  # make a space in between
        speak(random.choice(goodbyes))
        # End the game
        break
    
    else:
        time.sleep(1)
        print("Please choose a valid option.")
        
closing_credits()
