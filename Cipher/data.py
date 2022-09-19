print(hex(123))
print(hex(123).replace('0x',''))

print(bin(456))
print(bin(456).replace('0b',''))

print(int("59"))

print(1.2,int(1.2))

str = 'Hello'
print(str)
print(str[0])
print(str[0:4])
print(str[0:])
print(str*2)
print(str + ' ' + 'World!')

a='hello'
print(a.split)

print(int('10010',2)) # 18   (10010 - base 2)
print(int('10010'))

p = True
q = False
print(p+p+q)  # 2
print(p or q)

# List
myList = [2423424, 'hi', 34343,'kate',2323]
print(myList[1:6:2]) # show every second

print(len(myList))
#print(myList[1][0],myList[2][3])

myList.remove('hi')
myList.remove(myList[1])

string = 'ID name grade'
lis=string.split()
print(lis)

# Tuple
myTuple = (345,'hi',123,'kate')
print(myTuple)

#Dictionary
myDict = {'ID':123, 'name':'kate'}
print(myDict)

myDict['name'] = 'babe'  # replaced
print(myDict)


#Bitwise cal on inergers

# &  |   ^  Complement ~   Left shift  <<    Right shift >>
x = 13
y = 27

print(x | y)
print(x ^ y)
print(x << y)

import socket
hostname = socket.gethostname()
if hostname == 'PC1':
    print('This is Kates.')
    Flag = True
else:
    Flag = False

# in   &   not in

#Functions
def FuncName(inputs):
    "dicstring"
    Actions
    return outputs

header = ['4500','0073']
def Cal_Sum(header):
    p0 = int (header[0],16)
    p1 = int (header[1],16)
    decimal_sum = p0 + p1
    S = hex (decimal_sum)
    print(S)
    
# While
#while condition:
#    Action

pw = input ('pw please ')
while pw != "123":
    print('wrong,again ')
    break

    
# For loop
for num in [1,2,3]:
    print(num)
print("end")
