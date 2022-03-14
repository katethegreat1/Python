# # This is my Hero's inventory project.
# Made by Qian Han on 21/10/2021


# Using list operations and methods
inventory = ["sword", "armour", "shield", "healing potion"]

menu_options = """These are your options:
                   1 - show inventory
                   2 - add item to inventory
                   3 - number of items in inventory
                   4 - remove item from inventory                   
                   5 - swap item in inventory for a different item at position"""

# Welcome message
print("Welcome! I am here to manage your inventory.")

# Loop until player enters q to quit
while True:
    
        choice = input("What would you like to do? Enter i to see the options, q to quit ")
        
        # Code for option 'i'
        if choice == "i":
            print(menu_options)
            
        # Code for option 'q'                             
        elif choice == "q":
            break
        
        # Code for option '1'    
        elif choice == "1":           
            print("This is your inventory " + str(inventory))
            
        # Code for option '2'
        elif choice == "2":
            add_item = input("Please enter the item you would like to add: ")
            inventory.append(add_item)
            
        # Code for option '3'
        elif choice == "3":
            item_number = len(inventory)
            print("You have " + str(item_number) + " items in your inventory.")  
            
        # Code for option '4'
        elif choice == "4":
            try:
                remove_item = input("Please enter the item you would like to remove: ")
                inventory.remove(remove_item)
                
            # Handle input from users that is not expected
            except:
                print ("That item is not in your inventory.")
                
        # Code for option '5'
        elif choice == "5":
            try:
                remove_item = input("Please enter the item you would like to remove: ")
                remove_index = inventory.index(remove_item)
                
            # Handle input from users that is not expected
            except:
                print ("That item is not in your inventory.")
            else:
                add_item = input("Please enter the item you would like to add: ")
                inventory[remove_index] = add_item
            
        else:
            print ("Please choose an item from the list - enter i to see the list.")

# Goodbye message printed when exit the while loop
print("Goodbye!")