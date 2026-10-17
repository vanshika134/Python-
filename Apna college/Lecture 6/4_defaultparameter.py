print("Vanshika","Python")  # sep = " "   default
print("CS")                 # end = "\n"  default


# Default Parameters...........
def calc_prod(a,b=3):  # def calc_prod(a=3,b) : Not possible
    print(a * b)
    return a * b
calc_prod(1)
