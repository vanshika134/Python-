tuple = (2, 1, 3, 1)  # in this last me comma is optional but it is a good practice to use it to avoid confusion with parentheses used for grouping in expressions
print(type(tuple))    # Output: <class 'tuple'>
print(tuple[0])       # Output: 2
print(tuple[1])       # Output: 1
print(tuple[2])       # Output: 3
print(tuple[3])       # Output: 1
# tuple[0] = 5        # This will raise a TypeError because tuples are immutable

tup = ()
print(type(tup))      # Output: <class 'tuple'>
print(tup)            # Output: ()

tup2 = (1,)
print(type(tup2))     # Output: <class 'tuple'>
print(tup2)           # Output: (1,)

tup3 = ("hello",)
print(type(tup3))     # Output: <class 'tuple'>
print(tup3)           # Output: ('hello',)  
