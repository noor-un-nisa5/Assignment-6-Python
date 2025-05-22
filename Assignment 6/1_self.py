#1. Using self
#Assignment:
#Create a class Student with attributes name and marks.
# Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"The student name is {self.name}. He/She got {self.marks} marks.")


student = Student("Noor", 550)

student.display()

