null_set = set()
print(null_set)

null_set.add(1)
null_set.add(2)
null_set.add(2)
print(null_set)

null_set.remove(1)
print(null_set)
# null_set.remove(7)   # It will show a keyError, That isnvalue doesnt exist

null_set.add("Vanshika")
null_set.add((1,2,3))
# null_set.add([1,2,3])  # TypeError: unhashable type : 'list'"Mutable"
# immutable -> ek hash value bn skti hai(original value ko change nhi kr skte)
print(null_set)

print(len(null_set))
# null_set.clear()

collection = {"hello" , "Vanshika", "world" , "coding", "python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection)



