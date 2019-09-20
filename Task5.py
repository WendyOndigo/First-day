tpl = (1,2,3,4,5,6,7,8,9,10)
lst1,lst2 = [],[]

for i in range(0,5):
    lst1.append(tpl[i])

for i in range(5,10):
    lst2.append(tpl[i])

print(lst1)
print(lst2)
print("firsthalf ",lst1,"\t secondhalf ",lst2)

# tupl = (1,2,3,4,5,6)
#
# divider = int(len(tupl)/2)
#
# tpll = (tup1[:divider])
# tpl2 = (tup1[divider:])
#
# print(tpl1)
# print(tpl2)