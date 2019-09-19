# A function is a named ,reusable,block of code used to perform a related action.

# a = 0
# b = []
# c = {}
# d = ()

# def is the keyword python uses to create a new function
# "add two numbers" is the name of the funtion.
# a and b are called parameters of a function.
# c is the return value

def add_two_numbers(a,b):
    c = a+b
    return c
# Creatin/defining a fuction
def first_name_and_second_name(FN,SN):
    name = (FN + SN)
    return name
res = first_name_and_second_name( "Wendy","Ondigo")
print(res)

student1 = [12,23,34,45,65]
student2 = [22,23,34,45,65]
student3 = [32,23,34,45,65]
student4 = [42,23,34,45,65]

def studenttotal(list):
    result = list[0] + list[1] + list[2] + list[3] + list[4]
    return  result

def studentavrage(avrae):
    av = avrae/5
    return  av

a = studenttotal(student1);
b = studenttotal(student2);
c = studenttotal(student3);
d = studenttotal(student4);

st1 = studentavrage(a)
st2 = studentavrage(b)
st3 = studentavrage(c)
st4 = studentavrage(d)

# print("student one  total " + str(a))
# print("student two  total " + str(b))
# print("student three total " + c)
# print("student four  total " + d)
#
# print("student one avrage" + st1)
# print("student two avrage" + st2)
# print("student three avrage" + st3)
# print("student four avrage" + st4)
# totall = student1[0] + student1[1] + student1[2] + student1[3] + student1[4]
# totall = student2[0] + student2[1] + student2[2] + student2[3] + student2[4]
# totall = student3[0] + student3[1] + student3[2] + student3[3] + student3[4]
# totall = student4[0] + student4[1] + student4[2] + student4[3] + student4[4]
#
# average1 = totall/4
# average1 = totall/4
# average1 = totall/4
# average1 = totall/4

# a = int(input("first no."))
# b = int(input("second no."))
# def sum_digits(a,b):
#     num = a + b
#     return num
#
# result = sum_digits(a,b)
# print(result)

# a = int(input("num"))

# def sum_digits(num):
#     hint:use a for loop
#     return sum _of_digits

# num = 12345
#
# def dum_digits(num):
#     s= str(num)
#     b = a.split()
#     c= 0
#     for asa in b:
#         print(asa)
#
# dum_digits(num)

def sum_digits(num):
    sum_of_digits = 0
    num = str(num)
    for i in num:
        sum_of_digits = sum_of_digits + int(i)
    return sum_of_digits

a = sum_digits(22)
print(a)

