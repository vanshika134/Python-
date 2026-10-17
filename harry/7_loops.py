i = 1
while i < 11:
    print(i)
    i+=1

print("--------End of loop--------")

for i in range(1,11,1):
    print(i)

print("--------End of loop--------")

list = [1, "Harry" , False, "This", "Rohan", "Vanshika"]
i = 0
while i < len(list):
    print(list[i],",",  i)
    i += 1

print("--------End of loop--------")

l = [1,2,63,244]
for i in l:
    print(i)
else:
    print("Done")

print("--------End of loop--------")


for i in range(100):
    if(i == 25):
        break             # exit the loop right now
    print(i)

print("--------End of loop--------")

for i in range(100):
    if(i % 2 == 0):
        continue          # skip this iteration
    print(i)

print("--------End of loop--------")

for i in range(643):
    pass                  # null statement (do nothing)

# print("--------End of loop--------")


# 1111
num = int(input("Enter you num: "))
for i in range(1,11,1):
    print(f"{i} * {num} = {i * num}")

print("--------End of loop--------")

# 2222(WAP that greet only those whose name starts from S)
l = {"Harry", "Vanshika", "Soham", "Sachin"}
for name in l:
    if(name.startswith("S")):
        print(f"Hello, {name}!")

print("--------End of loop--------")

# 3333
num = int(input("Enter your num: "))
i = 1
while i < 11:
    print(f"{i} * {num} = {i * num}")
    i+=1

print("--------End of loop--------")

# 4444(Prime number)
num = int(input("Enter num: "))
for i in range(2,num):
    if(num % i == 0):
        print(num, " is not a prime")
        break
else:
    print(num, "is prime")
    
print("--------End of loop--------")

# 5555(Sum of n natural numbers)
i = 0
sum = 0
num = int(input("Enter num: "))
while i <= num:
    sum += i
    i+= 1
print(sum)

print("--------End of loop--------")

# 6666
fact = 1
num = int(input("Enter num: "))
for i in range(1,num+1):
    fact = fact * i
print(fact, "is factorial.")

print("--------End of loop--------")

# 7777
num = int(input("Enter num: "))              #   *
for i in range(1,num+1):                     #  ***
    print(" "*(num-i), end = "")             # *****
    print("*"*(2*i-1), end = "")
    print()

print("--------End of loop--------")

# 8888
num = int(input("Enter num: "))               # *
for i in range(1, num + 1):                   # **
    print("*"*i, end = "")                    # ***
    print()                                     

print("--------End of loop--------")

# 9999
num = int(input("Enter num: "))             # ***
for i in range(1, num + 1):                 # * *   (n = 3)
    if(i==1 or i==num):                     # ***
        print("*"* num, end = "")
    else:
        print("*", end="")
        print(" "* (num - 2), end="")
        print("*", end = "")
    print()

print("--------End of loop--------")

# 10101010
num = int(input("Enter num: "))
for i in range(10,0,-1):
    print(f"{num} * {i} = {num * i}")
#        OOOORRRR
num = int(input("Enter num: "))
for i in range(1,11):
    print(f"{num} * {11-i} = {num * (11-i)}")

print("--------End of loop--------")
