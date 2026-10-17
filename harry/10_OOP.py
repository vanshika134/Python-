from random import random

# Here name is object attribute and salary and language 
# are class attributes as they directly belong to the class.

class Employee:
    # name = "Vanshika" 
    language = "Python"   # This is a class attribute
    salary = 150000
Vanshika = Employee()
print(Vanshika.language, Vanshika.salary)
Rohan = Employee()
Rohan.salary = 100000
Rohan.name = "Rohan Roro Robinson" # This is an instance attribute
print(Rohan.name, Rohan.language, Rohan.salary)

print()

# instance attribute > class attribute (precedence)
class Employee:
    language = "Python"
    salary = 120000
harry = Employee()
harry.language = "Javascript"
print(harry.language, harry.salary) # Output: Javascript 120000

print()

# Self Methods & Static methods
class Employee:
    language = "Python"
    salary = 120000
    def show(self):    # If i dont pass self it will give an error....
        print("Language:", self.language)
        print("Salary:", self.salary)
    @staticmethod    # to not to pass self(object property) we use static method
    def greet():
        print("Hello, welcome to the company!")
harry = Employee()
harry.language = "Javascript"    #This is an instance attribute
harry.show() # Output: Language: Javascript Salary: 120000
harry.greet() # Output: Hello, welcome to the company!

print()

# __init__ constructor method (automatically called methods)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("This is the constructor method.")
Vanshika = Employee("Vanshika", 150000) # Output: This is the constructor method.
print(Vanshika.name, Vanshika.salary) # Output: Vanshika 150000


# 1111111111
class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = programmer("Vanshika", 1200000, 2432312)
print(p.name, p.salary, p.pin, p.company)
p = programmer("Harry", 12000, 24312)
print(p.name, p.salary, p.pin, p.company)

# 2222222222
class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
a = Calculator(4)
a.square()
a.cube()
a.squareroot()

# 3333333333(NO)
class Demo:
    a = 4
o = Demo()
print(o.a)    # prints class attribute because instance attribute is not present
o.a = 0       # Instance attribute is set
print(o.a)    # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute

# 4444444444
class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
    @staticmethod
    def hello():
        print("Hello World!!!")
a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()

# 5555555555
# import random
from random import randint
class Train:
    def __init__(self, trainno):
        self.trainno = trainno
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainno} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no: {self.trainno} is running on time.")
    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(100, 1000)}")
t = Train(12345)
t.book("Delhi", "Mumbai")
t.book("Mumbai", "Delhi")
t.getStatus()
t.getFare("Delhi", "Mumbai")

# 6666666666
# No Error............in 5 if we replace self to slf...
