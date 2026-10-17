class Student:    # CLASS
# -------- PARAMETERIZED CONSTRUCTOR --------
# (JISKE ANDR SELF KE ALAWA AUR BHI ARGUMENTS HAIN, USSE PARAMETERIZED CONSTRUCTOR KEHTE HAIN)
    college_name = "MIET"    # Class attribute
    def __init__(self, fullname , marks):  # CONSTRUCTOR(SELF ARGUMENT IS MANDATORY)
        self.name = fullname        # or name instead of fullname
        self.marks = marks          # self object ka reference hai, jiske through hum object ke attributes ko access karte hain
        # print(self)
        print("Adding new student in Database...")


s1 = Student("Vanshika", 95)    # OBJECT CREATION
# print(s1)
print(s1.name, s1.marks)
print(s1.college_name)    # Accessing class attribute using object reference

s2 = Student("Rohit", 85)    # Additional info. stored in s2 object
print(s2.name, s2.marks)
print(s2.college_name)    # Accessing class attribute using object reference

# -------- DEFAULT CONSTRUCTOR --------
class Student:    
    def __init__(self):  
        pass
