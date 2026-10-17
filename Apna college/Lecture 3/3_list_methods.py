list = [2, 1, 3]

print(list.append(4))      # Returns None because append() modifies the list in place and does not return a new list

list.append(4)             # Adds 4 to the end of the list
print(list)

list.sort()                # Sorts the list in ascending order
print(list)              

list.sort(reverse=True)    # Sorts the list in descending order
print(list)


list1 = ["banana", "apple", "grapes", "orange"]

list1.reverse()  # Reverses the order of the list
print(list1)

list1.sort()
print(list1)

list1.insert(0, "mango")    # Inserts "mango" at index 0
print(list1)

print(list1.pop(2))         # Removes and returns the item at index 2
print(list1)

list1.remove("apple")       # Removes the first occurrence of the value "apple" (if it exists)
print(list1)                # and returns the list after removal