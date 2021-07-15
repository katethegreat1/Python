#  Kris_class

#  1. crypto/exercises/07_containers.py /

a_tuple = ('some tuple', 123, 56.0, True, False, 123.0, 'hello')

# Tuples support two additional methods. count() and index().
# count() tells you how many times an item appears in a tuple.
print(a_tuple.count(56.0))
print(a_tuple.count(123))
print(a_tuple.count('a value that does not exist'))

# index() tells you where in the tuple an item appears. The index starts at 0.
print(a_tuple.index('hello'))
print(a_tuple.index('some tuple'))

# What happens if you try to find out the index for an item that does not exist in the tuple?

# What happens if we try to change a value at a specific index? e.g. a_tuple[0] = 123

# Lists are similar to tuples but they can be changed (they are "mutable"), and have additional methods.

# 2. crypto/exercises/06_operators.py

# Here are some of the operators built in to Python

# Operands are things that operators work with.
# e.g. 3 and 5 are operands in 3 + 5, while + is the operator.

print('=== Math Operators')
# Addition: +
print(3 + 5)

# Subtraction: -
print(5 - 3)

# Multiplication: *
print(3 * 5)

# Division: /
print(15 / 2)

# Floor Division, divides and rounds down. - Try this out to learn how it works: //
print(15 // 2)

# Modulus/Remainder, can be useful when combined with floor division,
# is used often in cryptography.
# You can think of the operand on the right as being like a clock.
# e.g. 16:00 is 4PM on a clock with 12-hours, so 16 % 12 is 4: %

print(16 % 12)

# Kate's code for %: (OMG I'm sooooo smart hahahaha)

a=16
b=12
if a>b:
    c= (a/b - int(a/b)) * b
    print(c)
    print(str(int(c)) + ' is the result if c is an int')
    print(str(int(c+1)) + ' is the result if c is not an int')

    # if c is not a int, a % b == int (c+1)
    # if c in a int, a % b ==c

elif a<b:
    print(str(a)+' is the result')



# Exponent/Power: **
print(3**5)  # This is the same as 3*3*3*3*3


# Comparison operators
print('=== Comparison Operators')

# Less Than: <
print('Is 3 < 5? ', 3 < 5)

# Greater Than: >
print('Is 3 > 5? ', 3 > 5)

# Less Than or Equal: <=
print('Is 2 less than or equal to 2?')
print(2 <= 2)

# Greater Than or Equal: >=
print('Is 10 greater than or equal to 12? ', 10 >= 12)

# Is Equal. Careful you don't confuse this with '=' which just has one equals sign.: ==
print('Is 42 equal to 42?', 42 == 42)

# Is Not Equal: !=
print('Is 25 not equal to 51?', 25 != 51)



# Operator Overloading: Operators can be "overloaded" and have different behaviour depending on what they're operating on.
print(10 + 5)  # This adds two integers.
print('hello' + ' world')  # This concatenates two strings.

print()

# Logical Operators:
# Python also has logical operators:
print('=== Logical Operators:\n')
# The logical AND is sometimes written as && in other programming languages, but in Python it's just written as: and
print('AND')
age = 30
has_license = True
if age >= 16 and has_license == True:
  print('Can drive')
else:
  print("Can't drive")  # You can also use " " for strings if you want to use the ' character.and

# The logical OR operator is sometimes written as || in other languages, but in Python it's just: or
print('OR: ')
admin = False
backdoor = True
if admin or backdoor:
  print('Access Granted')
else:
  print('Access Denied')


# The logical NOT operator is sometimes written as ! in other programming languages, but in Python it's just: not
print('NOT: ')
hotdog = False
if not hotdog:  # You don't need to write if hotdog == True
  print('not hotdog')
else:
  print('hotdog')

