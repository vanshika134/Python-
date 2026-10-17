# DICTIONARY

marks = {
    "Vanshika" : 100,
    "Shubham": 45,
    "Rohan" : 43
}
print(marks, type(marks))
# indexing not possible but print(marks["Vanshika"]) is possible
print(marks["Vanshika"])
# unordered, mutable, indexed, no duplicate keys
d = {}
print(type(d))

          # methods
grade = {
    "Vanshika" : 100,
    "Shubham": 45,
    "Rohan" : 43,
    0 : "Harry"
}
print(grade.items())
print(grade.keys())
print(grade.values())
grade.update({"Harry": 100, "Rohan" : 89})
print(grade)
print(grade.get("Vanshika")) # prints none if doesn't exist
print(grade["Vanshika"])  # prints error if doesn't exist


# SETS

s = {1,2,3,7,6,3,2,1,"Harry",4,3,3,3,3}
print(s)
e = set()     # not e = {} because it will create a dictionary
print(type(e))
            # Methods
s = {1,2,3,7,6,3,2,1,4,3,3,3,3}
s.add(56)
print(s)
print(len(s))    # return output : 7
s.remove(3)
print(s)
s1 = {1,4,2,4,6}
s2 = {3,7,0,5,2}
print(s1.union(s2))
print(s1.intersection(s2))


# 1111
words = {
    "Madad" : "Help",
    "Kursi" : "Chair",
    "Billi" : "Cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])

# 2222
s = set()
num = input("Enter number 1:")
s.add(int(num))
num = input("Enter number 2:")
s.add(int(num))
num = input("Enter number 3:")
s.add(int(num))
num = input("Enter number 4:")
s.add(int(num))
num = input("Enter number 5:")
s.add(int(num))
num = input("Enter number 6:")
s.add(int(num))
num = input("Enter number 7:")
s.add(int(num))
num = input("Enter number 8:")
s.add(int(num))
print(s)

# 3333
s = set()
s.add(18)
s.add("18")
print(s)

# 4444
s = set()
s.add(20)    # int and float are equal (1 == 1.0) True
s.add(20.0)
s.add("20")
print(s, len(s), type(s))

# 5555
s = {}
print(type(s))

# 6666
dict = {}
name = input("Enter friends name: ")
lang = input("Enter language name: ")
dict.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
dict.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
dict.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
dict.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
dict.update({name: lang})
print(dict)


# 7777
# When we will give same name/key 2 times so it will update
# value value(lang)

# 8888
# if value is same nothing will happen just assign to it

# 9999
# s = {8,7,12,"Harry", {1,2}}
# No, we cannot change
# TypeError: unhashable type: 'set'