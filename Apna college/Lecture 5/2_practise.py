# Print numbers from 1 - 100
i1 = 1
while i1 <= 100:
    print(i1)
    i1 += 1

print("----Loop Ended----")

# Print numbers from 100 - 1
i2 = 100
while i2 >= 1:
    print(i2)
    i2 -= 1

print("----Loop Ended----")

# Print the multiplication table of a number n
i3 = 1
n = int(input("give me your num: "))
while i3 <= 10:
    print(n*i3)
    i3 += 1

print("----Loop Ended----")

# Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
i4 = 1
while i4 <= 10:
    print(i4*i4)
    i4 += 1

# OOOORRRR

nums = [1,4,9,16,25,36,49,64,81,100]        
idx = 0                                # TRAVERSE
while idx < len(nums):
    print(nums[idx])       # nums[0], nums[1], nums[2]....
    idx += 1

print("----Loop Ended----")

# SEarch for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)
i5 = (1,4,9,16,25,36,49,64,81,100)
X = int(input("Give the number u want to search: "))
i = 0    #initialization
while i < len(i5):
    if(i5[i] == X):
        print("Found at index ", i)
    else:
        print("finding...")
    i+=1

    