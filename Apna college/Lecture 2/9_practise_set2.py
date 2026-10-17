# WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

# WAP to find the greatest of 3 numbers entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a > b and a > c):
    print("The greatest number is:", a  )
elif(b > a and b > c):
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)

# Wap to check if a number is a multiple of 7 or not.
num = int(input("Enter a number: "))
if(num % 7 == 0):
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")
    