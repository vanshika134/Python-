# Function definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    avg = (a+b+c)/3
    print(avg)
    print("Thank you!")
avg()           # Function call.....
avg()
avg()
avg()
a = avg()           # as many times as we want to....
print(a)


def goodDay():
    print("Good Day!!!!!")
goodDay()


# Functions with Arguments...........
def goodDay(name, ending):
    print("Good Day! " + name)
    print(ending)
goodDay("Vanshika", "Thank you")
goodDay("Mahak", "Thank you")
goodDay("Aayushi", "Thanks")


def goodDay(name, ending):
    print("Good Day! " + name)
    print(ending)
    return "Done"
a = goodDay("Vanshika", "Thank you")
print(a)   # without return it will return none,otherwise return value


# Default arguments
def goodDay(name, ending = "Thank you"):
    print(f"Good Day, {name}")
    print(ending)
goodDay("Vanshika", "Thanks")
goodDay("Harry")


# RECURSION (CALLS ITSELF)
'''
Factorial(0) = 1
Factorial(1) = 1
Factorial(2) = 1x2
Factorial(3) = 1x2x3
Factorial(4) = 1x2x3x4
Factorial(5) = 1x2x3x4x5
Factorial(n) = n x n-1 x ..... 3 x 2 x 1
Factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter your number: "))
print(f"The fact of a number is {factorial(n)}")


# 11111(WAP using F to find greatest of three numbers)
def greatest():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return b
# greatest()
print(greatest())


# 22222(WAF to convert celsius to fahrenheit)
def f_to_c():
    f = int(input("Enter temp in fahrenheit: "))
    return 5*(f-32)/9
print(f"Temperature is , {round(f_to_c(),2)} °C")    # Decimal places only for 2
print(f_to_c())
print(f_to_c())


# 33333(How do u prevent python print() function to print a new line at the end)
print("A", end = "")
print("B")
print("C")


# 44444(WARF to calcukate sum of first n natural numbers.)
'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4
sum(n) = 1+2+3+4.....n-1 + n
sum(n) = sum(n-1) + n
'''
def sum(n):
    if n == 1:
        return 1
    else:
        return  sum(n-1) + n
print(sum(4))

# def sum():
#     a = int(input("Enter number: "))
#     i = 0
#     sum = 0
#     while i <= a:
#         sum += i
#         i += 1
#     return sum
# print(sum())


# 55555(WAPF to print first n lines id following patterns:)
#  ***
#  **
#  *       for n = 3
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
pattern(3)

def pattern():
    n = int(input("Enter number: "))
    for i in range(n,0,-1):
        print("*"*i)
print(pattern())


# 66666 (WAPF which converts inches to cms)
def i_to_c(inch):
    return inch * 2.54
n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {i_to_c(n)}")


# 77777(WAPF to remove a given word from a list and strip at the same time)
def rem(l,word):
    for item in l:
        l.remove(word)
        return l
l = ["Harry" , "Rohan" , "Shubham", "an"]
print(rem(l,"an"))
    
def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Harry" , "Rohan" , "Shubham", "an"]
print(rem(l,"an"))


# 88888(WAPF to print multiplication table of a given number.)
def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
multiply(5)



