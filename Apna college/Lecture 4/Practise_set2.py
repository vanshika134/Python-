# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}

x = int(input("enter phy: "))
marks.update({"phy" : x})
x = int(input("enter maths: "))
marks.update({"maths" : x})
x = int(input("enter chem: "))
marks.update({"chem" : x})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of build-in data types)
# values = {9, "9.0"}                # 9 amd 9.0 are same in python
# values = {9.0, "9"}             # OR
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
