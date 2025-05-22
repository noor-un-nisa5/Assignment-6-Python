#14. Aggregation
#Assignment:
#Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def details(self):
        print("Department: " ,self.dept_name)
        self.employee.show()

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee Name: ", self.name)

emp = Employee("Noor Un Nisa")
dept = Department("Artificial Intelligence", emp)
dept.details()

