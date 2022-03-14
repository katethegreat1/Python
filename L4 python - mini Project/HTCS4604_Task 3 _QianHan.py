# This is my converting hex colour to RGB project.
# Made by Qian Han on 23/09/2021

# Welcome and explain what the program is for:

print("Welcome!\nThis program converts colours in hex format to RGB format.\n")

hex_number=""

# Loop until the user inputs 'q' to quit

while hex_number != "q":
    
    # Get input from the user
    
    hex_number=input("Enter a colour in hex format without the '#', or q to quit.")
    
    if hex_number != "q":
    
    # Use index to isolate hexadecimal digit pair, use int() for conversion
    
        try:
           r = int(hex_number[0:2],16)
           g = int(hex_number[2:4],16)
           b = int(hex_number[4:6],16)
           
    # Handle input from users that is not expected
    
        except:
            print("Please input a valid hex colour.")
            
        else:
            rgb = str(r)+","+ str(g)+","+ str(b)
            print("Hex Value: " + hex_number +"    Converts to RGB: (" + rgb + ")")
            
# Say goodbye and exit     
    else:
        print("Goodbye!")

