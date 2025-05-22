#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Noor Un Nisa", "$1000", "25.4.2006")

print("Employee name:", emp.name)
print("Employee salary:", emp._salary)
print("Employee social security number:", emp._Employee__ssn)
