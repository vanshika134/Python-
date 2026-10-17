class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Vanshika")
print(s1.name)
del s1.name
print(s1.name)    # As the name is deleted using del word it shows,
# AttributeError: 'Student' object has no attribute 'name'

