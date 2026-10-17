# WARF to calculate the sum of first n natural numbers.

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)


# WARF to print all elements in a list.
# (Use list & index as parameters.)

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["mango","litchi","apple"]
print_list(fruits)