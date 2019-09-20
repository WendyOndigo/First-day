from classes_and_objects import Student
# roy is an object of class student.
# roy is an member of class student.
# roy is an instance of class student.
roy = Student(12,13,23,45,57)
wendy = Student(34,34,67,98,60)
said = Student(23,56,89,90,67)

roy.english

said = Student()
wendy = Student()
roy = Student()

print(roy.english)
print(said.english)

roy.find_total()
roy.find_average()
roy.find_grade()

print(roy.grade)
print(wendy.grade)
print(said.grade)


