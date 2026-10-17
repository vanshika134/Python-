# Create student class that takes name & marks of 3 subjects
# as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        avg = (m1+m2+m3)/3
        self.avg = avg

s1 = Student("Vanshika", 99, 98, 97)
print(s1.name, s1.avg)

# oooooooooooooooooooorrrrrrrrrrrrrrrrrrrr

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your average marks are:", sum/3)
s1 = Student("Vanshika", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()


