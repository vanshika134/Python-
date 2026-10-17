# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

seq = range(11)
for i in seq:
    print(i)
#OR
for i in range(11):   # Last number is excluded
    print(i)

print("----End of loop----")

for i in range(2,10):      #range(start,stop)
    print(i)

print("----End of loop----")

for i in range(2,10,2):      #range(start,stop,step)
    print(i)

print("----End of loop----")

for i in range(2, 101, 2):               #Even numbers 1-00
    print(i)

print("----End of loop----")

for i in range(1, 100, 2):               #Odd numbers 1-00
    print(i)

print("----End of loop----")
