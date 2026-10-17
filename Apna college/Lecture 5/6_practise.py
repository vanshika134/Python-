# Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
num = [1,4,9,16,25,36,49,64,81,100]
for val in num:
    print(val)


# Search for a number X in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]                 LINEAR SEARCH
num2 = (1,4,9,16,25,36,49,64,81,100,49)
X = 49
idx = 0
for val in num2:
    if(val == X):
        print("number found at idx: ", idx)
        break
    idx += 1


