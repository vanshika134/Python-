name1 = "Vanshika"
name2 = 'Vanshika'
name3 = '''Vanshika'''  # string is immutable

# Indexing
character1 = name1[1]
print(character1)

# Slicing
nameshort = name1[0:6]
print(nameshort)
print(name1[-4:-1])
print(name1[1:4])
print(name1[0:len(name1):2]) # skip value
print(name1[0:])
print(name1[:6])

# functions
name = "vanshika is my name"
# creates new strings not change the existing one
print(len(name))
print(name.endswith("name"))
print(name.startswith("Vanshika"))
print(name.capitalize()) #only first letter of whole string
print(name.lower())
print(name.upper())
print(name.title())  #First letter of each word
print(name.replace("my", "your"))

# escape sequence characters
print("Vanshika\tlearns python.\t.\nIn sunrise coaching.")
print("It's 'nice' ")
print("Vanshikaaa is \"vanshikaa\"") #double quote me double quotes
print("Hey \\ use of backslash yeah")

# 1111
a = input("Enter your name: ")
print("Good Afternoon!",a,"...","How are you?")
print(f"Good afternoon!! {a}... How are you?. ") 
# Strings ke andr bi variables asssign kr skte hai using f string

# 2222
letter = '''
        Dear <|Name|>
        You are selected!
        <|Date|>
        In Google.....
        '''
print(letter.replace("<|Name|>", "Vanshika").replace("<|Date|>", "18 January 2027"))
# chaining

# 3333
name = "Vanshika is  a good girl"
print(name.find("  "))

# 4444
name = "Vanshika is  a good girl"
print(name.replace("  ", " "))

# 5555
print("Dear Harry,\n\tThis python course is nice.\nThanks!")



