#6. Constructors and Destructors
#Assignment:
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
 
class Logger:
    def __init__(self, program, error):
        self.program = program
        self.error = error
        print(f"The {self.program} has constructed with no {self.error}")

    def __del__(self):
        print(f"The {self.program} has destroyed with {self.error}")

project = Logger("Program","error")
print(f"{project.program} is running successfully!")

del project

