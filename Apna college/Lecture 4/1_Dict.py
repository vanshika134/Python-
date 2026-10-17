info = {
    # "key" : "value",
    "name" : "Vanshika",
    "learning" : "Python",
    "Subjects" : ["C Language", "Data Science", "Machine Learning"],
    "age" : 20,
    "is_adult" : True,
    "marks" : (90, 95, 85),
    12 : 45,
} 
print(info)
print(type(info))
print(info["name"])
print(info["learning"])
print(info["Subjects"])
print(info["age"])
print()
# print(info["Surname"]) # This will give an error because there is no key named "Surname"
info["name"] = "Vanshika Bansal" # This will update/overwrite the value of the key "name"
print(info)        # OVERWRITE
print()
info["Surname"] = "Bansal" # This will add a new key-value pair to the dictionary
print(info)

