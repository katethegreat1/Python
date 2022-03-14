# Exercise 4

# Challenge 1
students = ["cSinNZCITE1991", "mHolNZCITE1994","gGreDIPLOM1985", "nSulBACHEL1991","bMatMASTER1901","hCarNZCITE2004"]

new_student = input("Enter you student info.")
students.insert(2, new_student)
#get the details for 1 student out of the list and place it in a variable

#print add that variable to the print statement below:
print("first students info:", students[0])

#use slicing to print out the birth year of that student

print("first students birth year:", students[0][10:])

#calculate their rough age by subtracting their birth year by 2021


#print that age
print("first students age:", str(2021-int(students[0][10:])))

# Challenge 2

print("First students Name:", students[0][:4], ", Age:", str(2021-int(students[0][10:]))+",", "Course:", str(students[0][4:10]))


# Challenge 3 & 4

try:
    student_number = 0
    while student_number<= 6:
        print("Current students Name:", students[student_number][:4], ", Age:", str(2021-int(students[student_number][10:]))+",", "Course:", str(students[student_number][4:10]))
        student_number += 1
        
except:
    print("please key in the correct student info.")
        

    


    