from functions import add_two_numbers
# Assignment operators
#=
# this line means "100 is assigned to a"
a = 100
total = 1+1+1+1+2+2+3

#Arithmetic operators
# + addition
# - subtraction
# * multiplication
# / division
# ** exponential
# % modulo operator - gives the remainder of values
c = 10 % 2
print(c)

# Comparison operators
# The result of comparison operators is always 0
z = 10
y = 11
# w = z > y
# print(w)
w = z <= y
# less than or equal to

# equality operator
d = 1
e = 2
print(d==e)
# is d equal to e

# inequality operator
print(d != e)

# comparison operators are used with conditional statements ie if statements

# LOGICAL OPERATORS
# and
# all conditions must be true for and operator
# True and True and False = False
#or
# at least one condition must be true
# True and True - true
# False and False - false
# True and false - false
# True or false - false
# false or false - false

# NOT-Negates operations
print(not(True and False))
print(not(True and False or False))
print(not(1<3 and 2>4 or 2>4))

first_number = eval(input("Enter first number"))
second_number = eval(input("Enter second number"))
# calling our function
result = add_two_numbers((first_number,second_number))
print(result)