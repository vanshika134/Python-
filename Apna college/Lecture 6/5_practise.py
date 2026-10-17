# WAF to print the length of a ist.(list is the parameter)
cities = ["Delhi", "Gurgaon", "Mumbai", "chennai", "Bombay", "kolkata"]
heroes = ["thor", "ironman","captain america","Shaktiman"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)


# WAF to print the element of a list in a single line(list is the parameter)
cities = ["Delhi", "Gurgaon", "Mumbai", "chennai", "Bombay"]
heroes = ["thor", "ironman","captain america"]
def print_list(list):
    for item in list:
        print(item, end = " ")
print_list(cities)
print()
print_list(heroes)
print()


# WAF to find the factorial of n(n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(6)
cal_fact(15)
cal_fact(9)


# WAF to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR")
converter(3)
converter(4500)
converter(100)


# WAF for even and odd
def even_odd(p):
    if(p%2 == 0):
        print("Even")
    else:
        print("Odd")
even_odd(5)
even_odd(102)
