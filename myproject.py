Wendy = int(input("enter name"))
Lavenda = int(input("enter eng marks"))
Linda = int(input("enter kis marks"))
George = int(input("enter ssr marks"))
Pinky= int(input("enter sci marks"))

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