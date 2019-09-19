userDetails = {"name":"Muyani Letina","age":20,"location":"Nairobi","team":"Dothraki Screamers"}

print (userDetails)
 # a dictionary is a store for key value pairs

 # retrieve name of the user
print (userDetails["name"])

# add an item to the dictionary
userDetails["levelOfEducation"] = "Bachelor"
print (userDetails)

# tyocasting dictionary values to be a list
userDetailsList = list(userDetails.values())
print (userDetailsList)

#ASSIGNMENT type cast dictionary keys to be a list

# length of a dictionary
print (len(userDetails))

# loop over all dictionary values
for i in userDetails.values():
    print (i)

# loop over both values and keys
for key,value in userDetails.items():
    print (key,value)
