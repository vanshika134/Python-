# Virtual Environment (---env---)
# pip freeze (IT tells you which packages are 
#            installed in your virtual environment)
# pip freeze > requirements.txt (IT creates a file
#                               with all the packages 
#                               installed in your 
#                               virtual environment)

# Lambda Function
square = lambda x: x**2
print(square(5))

# join method
a = ["Vanshika","BTech","CS"]
print("-:".join(a))

# Formatting
a = "{0} is a good {1}".format("Vanshika","Student")
print(a)
a = "{1} is a good {0}".format("Vanshika","Student")
print(a)

# MAP FILTER REDUCE
l = [1,2,3,5,4]
squared = list(map(lambda x: x**2, l))
print(squared) 

l = [1,2,3,5,4]
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even, l)
print(list(onlyEven))

l = [1,2,3,5,4]
def sum(a,b):
    return a+b
mul = lambda a,b: a*b
from functools import reduce
print(reduce(sum, l))
print(reduce(mul, l))

# 11111
# 22222
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))
s = "The name of the student is {0} and her marks are {1} and her phone number is {2}".format(name,marks,phone)
print(s)

# 33333
table = [str(7*i) for i in range(1,11)]
s = "\n".join(table)
print(s)

# 44444
def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [1,2,34423,45,566,32,5,3,78,32]
f = list(filter(divisible5, a))
print(f)

# 55555
from functools import reduce
l = [111, 2, 65, 5553, 635, 65,64,74, 45, 55]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))

# 66666


# 77777
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()