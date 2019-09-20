# A class is a group of related functions and variables.

# oop-object oriented programming.

# in python a function that is inside a class is called a method.

# An object is an instance of a class./a member of that class.

# student = [] student is a member of class list.

# A constructor-A constructor is a special type of method (function) which is used to initialize the instance members of the class.
#                -special type of method that runs every time you instantiate a class.
class Student:
    math = 0
    english = 0
    kis = 0
    ssr = 0
    sci = 0
    total_marks = 0
    average_marks = 0.0
    grade = ""

    # a constructor
    def __init__(self,math,english,kis,ssr,sci):
        self.math = math
        self.english = english
        self.kis = kis
        self.ssr = ssr
        self.sci = sci
        self.find_total()
        self.find_average()
        self.find_grade()

    def find_total(self):
        self.total_marks = self.math+self.english+self.kis+self.ssr+self.sci

    def find_average(self):
        self.average_marks = self.total_marks/5
    def find_grade(self):
        ave = self.average
        if ave >=80 and ave<=100:
            self.grade = "A"
        elif ave >=70:
            self.grade = "B"
        elif ave >= 60:
            self.grade = "C"
        elif ave >= 50:
            self.grade = "D"
        else:
            self.grade = "E"