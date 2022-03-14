#write a program that will:

#ask for the user to enter their hight in CMs and convert it to an int

#if they are < 140cm reject them from the ride
#if they are between 140 and 159 tell them "ok you can go on the ride"
#if they are between 160 and 179 tell them "you can go on the ride but watch out for dat tree"
#if they are 180 or over tell them "sorry bro you are a giraffe"

list_height = []
asking = True
while asking:
    try:
        height = int(input ("How tall are you in cm?"))
    except:
        print("numbers only plz!")
    else:
        if height < 140:
            print("Get out.")

        elif 140 <= height <= 159:
            print("ok you can go on the ride.")
            list_height.append(height)

        elif 160 <= height <= 179:
            print("you can go on the ride but watch out for dat tree.")
            list_height.append(height)

        else:
            print("sorry bro you are a giraffe.")

        end_program_decision = input("would you like the program to end? y/n: ")
        
        if end_program_decision == "y":
            asking = False

print("heights going on the ride:", list_height)
print("the program has finished goodbye!")

        

