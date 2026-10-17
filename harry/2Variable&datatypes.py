a,b = 1,3         # int variable
print(a+b)

c = 5.22          # float
print(c)

name = "Harry"    # string variable
print(name)

d = False         # boolean variable
print(d)

e = None
print(e)          # None variable

# Variable can contain only alphabets,digits and underscores
# Can not start with a digit
# no white spces or special characters

# OPERATORS IN PYTHON 
print("1] Arithmetic operators : +, -, *, / etc")
a,b = 7,4
print(a+b)
print("2] Assignment operators : =, +=, -=, etc")
d = 6                     
d += 6   #increment value of d and assign it to d                  
print(d)                     
d -= 7   #decrement value of d and assign it to d                 
print(d)                     
print("3] Comparison operators : ==, >, >=, <, <=, !=, etc")
e = 5>4                     
print(e)                 #True or False               
print("4] Logical operators : and, or, not")
f = True or False                     
print(f)                     
g = True and False                     
print(g)                 #True or False   


# Type function() and type casting
h = "31.2"
print(type(h))
i = float(h)
print(type(i))


# input function
p = input("enter number1: ")        #1
q = input("enter number2: ")        #6
print("sum is ", p+q) #Concatenated (16)

p = int(input("enter number1: "))   #1
q = int(input("enter number2: "))   #6
print("sum is ", p+q)               #(7)


# 1111(Add two numbers)
a,b = 1,2
print(a+b)

# 2222(find remainder when no. divided by z)
c,d = 34,5
print("Remainder when c is divided by d is: ", c % d)

# 3333(type of variable)
e = eval(input("Enter value to know its type: "))
print(type(e))

# 4444(whether a is greater than b or not)
f = int(input("Enter 1 "))
g = int(input("Enter 2 "))
print("f is greater than g is: ", f>g)

# 5555(find avg)
h = int(input("Enter 1 "))
i = int(input("Enter 2 "))
print("avg is ", (h+i)/2)

# 6666(square of a number)
j = int(input("Enter number "))
print("The square of number is: ", j**2) #(j*j)



