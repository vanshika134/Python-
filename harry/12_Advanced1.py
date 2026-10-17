# Using Walrus Operator
if((n := len([1, 2, 3, 4, 5])) > 3):
    print(f"List has {n} elements")

# TYPES
n: int = 5
name: str = "Vanshika"
def sum(a: int, b: int) -> int:
    return a + b
print(sum(5, 6))

from typing import List, Dict, Tuple, Set, Union, Optional

# MATCH CASE
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(500))  # Output: Internal Server Error
print(http_status(300))  # Output: Unknown Status

dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
dict2 = {'d' : 4, 'e' : 5, 'f' : 6}
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# EXCEPTIONS
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
print("Thankyou!!")

# RAISING EXCEPTIONS
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if(b == 0):
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    print(f"The result of {a} divided by {b} is: {int(a)/b}")

# TRY WITH ELSE
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as e:
    print(e)
else:
    print("I am inside else.")

# TRY WITH FINALLY
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as e:
    print(e)
finally:
    print("I am inside finally.")
# WE can also writw it wothourt finally block
# but usually used in functions to close the file or database connection
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
    except ValueError as e:
        print(e)
    finally:
        print("I am inside finally.")
main()

# MAIN.PY
from module import myFunc
myFunc()

# GLOBALFUNCTIONS.py
# ENUMERATE.py

# l = [3,56,23,78,90]
# idx = 0
# for i in l:
#     print(f"Index is {idx} and value is {i}")
#     idx += 1
l = [3,56,23,78,90]
for idx, i in enumerate(l):
    print(f"Index is {idx} and value is {i}")

# LIST COMPREHENSION
l = [3,56,23,78,90]
squared = [x**2 for x in l]
print(squared)

# 11111
try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
print("Thankyou!!")

# 22222
l = [1,2,3,4,5,6,7,8]
for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)

# 33333
n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
print(table)

# 44444
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")

# 55555
n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
with open(r"D:\CODING\2 python\harry\tables.txt", "a") as f:
    f.write(str(table) + "\n")

