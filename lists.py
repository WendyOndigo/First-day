# name = "Wendy Ondigo"
# age = "19"
# location = "Nairobi"
# school = "KU"
# job = "TIT"
person1 = ["Wendy Ondigo",19,"Nairobi","KU","TIT",True]
# we use square braackets to tell that this is a list
print(type(person1))
print(person1)
# a list can store anything,including floats and boolean

front_row_students =["Said","Howard","Kelvin","patricia"]
#print(front_row_students)
# we use indexing to access various positions in a string
# first = front_row_students[0]
# first = front_row_students[1]
# first = front_row_students[2]
# when you dont know no. of records
# last student -1,second last -2
first = front_row_students[-1]
print(first)
# to select fiirst x students,we use range
first = front_row_students[0:2]
print(first)
# in indexing,the integer on the left of the colon is normally the starting point,this is called list slicing
# the last element is normally the last list element but is exclusive
first = front_row_students [1:3]
print(first)

# LIST OPERATIONS
# CONCATENATING
form1east = ["Howard"]
form1west = ["Melvin"]
form1 = form1east + form1west
print(form1)
print(len(form1))

# determining membership in a list
is_Melvin = "Melvin" in form1
print(is_Melvin)

# ASSIGNMENT
# list methods
form1.count("Melvin")