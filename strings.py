name = "Wendy Ondigo"
# strings are enclosed in quotations , this is to tell python to take that value literally,strings are also called literals.
name = "Wendy Ondigo + Adhiambo"
print(name)
phone_number = "0790486172"
print(phone_number)
print(type(phone_number))

marks = "30+20+40+30"
# typecasting
phone_number = int(phone_number)
print(phone_number)
print(type(phone_number))
phone_number = str(phone_number)
print(type(phone_number))

# STRING OPERATIONS

first_name = "Wendy"
second_name = "Ondigo"
# concatenating strings
# we use a plus operator to concat strings
full_name = first_name + " " + second_name
print(full_name)
first_name = "wendy"
print(first_name)
print(first_name.title())
print(first_name.upper())
print(first_name.lower())
print(first_name.split())
print(first_name.count("n"))

gender = "MFMFMFMFFFMMMFFFMMMFFMMFMFMFMFMFMFM"
print(gender.swapcase())
