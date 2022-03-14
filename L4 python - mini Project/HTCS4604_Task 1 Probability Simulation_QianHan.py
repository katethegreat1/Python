# This is the Probability Simulation project.
# Made by Qian Han on 09/09/2021

import random

# Define variables to store numbers for each sum dice (1-9, others) was made.

total_1s = 0
total_2s = 0
total_3s = 0
total_4s = 0
total_5s = 0
total_6s = 0
total_7s = 0
total_8s = 0
total_9s = 0
total_others = 0

# Loop for 1000 times using a "for" loop:

for i in range (1,1001):
    
# Simulate the throwing of two dice using random.randint() and add the numbers up:

    sum_dice = random.randint(1,6) + random.randint(1,6)
    
# Keep count of the number of times each sum number (1-9, others) was made:

    if sum_dice == 1:
        total_1s += 1
    elif sum_dice == 2:
        total_2s += 1
    elif sum_dice == 3:
        total_3s += 1
    elif sum_dice == 4:
        total_4s += 1
    elif sum_dice == 5:
        total_5s += 1
    elif sum_dice == 6:
        total_6s += 1
    elif sum_dice == 7:
        total_7s += 1
    elif sum_dice == 8:
        total_8s += 1
    elif sum_dice == 9:
        total_9s += 1
    else:
        total_others += 1

# calculate the probability (p) of each sum dice (1 to 9), using the round() function to round to 2dp.
# Print the results to the screen.

print("1 was thrown "+ str(total_1s) + " times.\t       p(1) = " + str(round((total_1s/1000),2)))
print("2 was thrown "+ str(total_2s) + " times.\t       p(2) = " + str(round((total_2s/1000),2)))
print("3 was thrown "+ str(total_3s) + " times.\t       p(3) = " + str(round((total_3s/1000),2)))
print("4 was thrown "+ str(total_4s) + " times.\t       p(4) = " + str(round((total_4s/1000),2)))
print("5 was thrown "+ str(total_5s) + " times.\t       p(5) = " + str(round((total_5s/1000),2)))
print("6 was thrown "+ str(total_6s) + " times.\t       p(6) = " + str(round((total_6s/1000),2)))
print("7 was thrown "+ str(total_7s) + " times.\t       p(7) = " + str(round((total_7s/1000),2)))
print("8 was thrown "+ str(total_8s) + " times.\t       p(8) = " + str(round((total_8s/1000),2)))
print("9 was thrown "+ str(total_9s) + " times.\t       p(9) = " + str(round((total_9s/1000),2)))

# Print the results for all other sum numbers thrown to the screen and the total number of trials:

print("Other numbers were thrown "+ str(total_others) +" times.")
print("Total number of throws was " + str(i) + " times.")
