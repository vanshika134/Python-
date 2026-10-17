student = {
    "name": "Vanshika",
    "age": 20,
    "subjects": {
        "C Language": 90,
        "Data Science": 95,
        "Machine Learning": 85
    },
    "is_adult": True   
}
# print(student.keys())
print(list(student.keys()))
# print(len(student.keys()))
# print(list(student.keys()))

print(student.values())
# print(list(student.values()))
# print(len(student.values()))
print()
print(student.items())
# print(list(student.items()))
print()
# print(student["name2"]) # This will give an error because there is no key named "name2"
print(student.get("name2")) # This will return None because there is no key named "name2"
print()
print(student.get("name2", "Key not found")) # This will return "Key not found" because there is no key named "name2"
print()

student.update({"city" : "delhi"})
print(student)