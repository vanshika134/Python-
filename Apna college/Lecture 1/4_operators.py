#Arithmetic Operators
a = 5
b = 3
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus (remainder)
print("a // b =", a // b) # Floor Division
print("a ** b =", a ** b) # Exponentiation (a raised to the power of b)


#Comparison/Relational Operators
x = 10
y = 20
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to
# print("x is greater than y:", x > y)  # Output: False
# print("x is less than y:", x < y)     # Output: True
# print("x is equal to y:", x == y)   # Output: False
# print("x is not equal to y:", x != y) # Output: True
# print("x is greater than or equal to y:", x >= y) # Output: False
# print("x is less than or equal to y:", x <= y) # Output: True
# print("x is greater than 5 and less than 15:", x > 5 and x < 15) # Output: True
# print("x is less than 5 or greater than 15:", x < 5 or x > 15) # Output: False


#Assignment Operators
c = 10
print("Initial value of c:", c)  # Output: 10
c += 5      # Equivalent to c = c + 5
print("After c += 5:", c)  # Output: 15
c -= 3      # Equivalent to c = c - 3
print("After c -= 3:", c)  # Output: 12
c *= 2      # Equivalent to c = c * 2
print("After c *= 2:", c)  # Output: 24
c /= 4      # Equivalent to c = c / 4
print("After c /= 4:", c)  # Output: 6.0
c %= 5      
print("After c %= 5:", c)  # Output: 1.0
c //= 2             
print("After c //= 2:", c)  # Output: 0.0
c **= 3 
print("After c **= 3:", c)  # Output: 0.0

c = 10  
c **= 3 
print("After c **= 3:", c)  # Output: 1000


#Logical Operators
p = True
q = False
print("p and q:", p and q)  # Logical AND
print("p or q:", p or q)    # Logical OR
print("not p:", not p)      # Logical NOT
print("not q:", not q)      # Logical NOT

print(not False)  # Output: True
print(not True)   # Output: False

r = 50
s = 30
print(not(r > s))  # Output: False

val1 = True
val2 = False
print("and operator:", val1 and val2)  # Output: False
print("or operator:", val1 or val2)    # Output: True
print("OR opertor:", (r==s) or (r>s))  # Output: True
print("AND opertor:", (r==s) and (r>s))  # Output: False