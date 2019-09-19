# num = int(input("Enter a number-"))
# mod1 = num % 2
# mod2 = num % 4
# if mod1 is 0:
#     print(" even number.")
# if mod2 is 0:
#     print("multiple of 4")
# else:
#     print(" odd number.")

#
number = input("Enter a number: ")
number = int(number)
if number % 2 == 0:
    print(" number is even.")
elif number % 4 == 0:
    print("multiple of  4")
elif number % 4 != 0:
    print("not a multiple of 4")
else:
    print("number is odd")

num = int(input)