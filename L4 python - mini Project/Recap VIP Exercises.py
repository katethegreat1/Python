#Exercise 1

#Write the code that asks for an end value and displays each number from 1 to the end value in increments of one.

end_value=int(input("Enter a end value"))
value=0
while value < end_value:
    value+=1
    print(value)

#Exercise 2

#Write the code that asks for an end value and displays
#each number from 0 to the end value in increments of five.

end_value=int(input("Enter a end value"))
value=0
while value <= end_value:
    print(value)
    value+=5
    
# method 2

end_value=int(input("Enter a end value"))
for value in range (0, end_value+1, 5):
    print(value)
    


#Exercise 3

'''Create a program that:
Prompts the user for their full name
Uses a for loop to cycle through their name
If their name only contains 1 space or their name contains 0 spaces 
Print “haha you have no middle name”
else if their name contains > 2 spaces 
Print “wow that is a big name”
else
print “what an average name”'''

name=input("What's your full name?")
space=name.count(" ")
if space <=1:
    print("haha you have no middle name")
elif space >2:
    print("wow that is a big name")
else:
    print("what an average name")
    



