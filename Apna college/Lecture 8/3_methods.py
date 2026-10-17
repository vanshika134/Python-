class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):     # method
        print("Welcome Student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Alice", 99)
s1.welcome()
print("Marks:", s1.get_marks())
