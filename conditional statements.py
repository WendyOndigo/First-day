# in python. if is the only conditional statement

# # if-else statements
# balance = 100
# withdraw = 200
# name = "Wendy"
# if withdraw <= balance and name == "Wendy":
#     print("Withdraw success")
# else:
#     print("Insufficient funds")
#
# # if - elif - else statement
#
# score = "Excellent"
#
# if score == "Excellent":
#     print("Green label")
# elif score == "Good":
#     print("Red label")
# elif score == "Poor":
#     print("Red label")
# else:
#     print("unrecognised")

# Task= ask a user to enter the following marks,USE INPUT FUNCTION
# math
# eng
# kis
# ssr
# sci
# calculate the total of the marks
# calculate the average
# using the average,give grades to the student
# 80 - 100 = "A"
# 70 - <80 = "B"
# 60 - <70 = "C"
# 50 - <60 = "D"
# 40 - <50 = "E"

math = int(input("enter math mark"))
eng = int(input("enter eng marks"))
kis = int(input("enter kis marks"))
ssr = int(input("enter ssr marks"))
sci= int(input("enter sci marks"))

Totalmarks = (math + eng + kis + ssr + sci)
averagemarks = (Totalmarks/5)

if averagemarks >= 80 and averagemarks <=100:
    print("A")
elif averagemarks >= 70 and averagemarks <80:
    print("B")
elif averagemarks >= 60 and averagemarks <70:
    print("C")
elif averagemarks >= 50 and averagemarks <60:
    print("D")
elif averagemarks >= 0 and averagemarks <50:
    print("E")
else:
    print("unrealistic")


