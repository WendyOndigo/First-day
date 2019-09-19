# var1 = int(input("a"))
# var2 = int(input("b"))
def biggest1 (num1,num2,num3):
    if num1>num2 and num1>num3:
        return(num1)
    elif num2>num1 and num2>num3:
        return(num2)
    elif num3>num1 and num3>num2:
        return(num3)


# def three_variables(var3):
#

num1 = int(input("an integer a "))
num2 = int(input("an integer b "))
num3 = int(input("an integer c "))

print(biggest1(num1,num2,num3))