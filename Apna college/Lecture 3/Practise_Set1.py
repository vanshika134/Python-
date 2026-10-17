# WAP to ask the user to enter names of their 3 favourite movies and store them in a list.

movies = []
movies.append(input("Enter your fav. movie 1: "))
movies.append(input("Enter your fav. movie 2: "))
movies.append(input("Enter your fav. movie 3: "))
print("Your favourite movies are:", movies)

#     --------OR--------

# movies = []
# movie1 = input("Enter your fav. movie 1: ")
# movies.append(movie1)
# movie2 = input("Enter your fav. movie 2: ")
# movies.append(movie2)
# movie3 = input("Enter your fav. movie 3: ")
# movies.append(movie3)
# print("Your favourite movies are:", movies)



# WAP to check if a list contains a palindrome of elements.(Hint: use copy() method )
# [1,2,3,2,1]         [1,"abc","abc",1]

list1 = [1,2,1]
copy_l1 = list1.copy()  # Create a copy of list1]
copy_l1.reverse()        # Reverse the copy of list1
if copy_l1 == list1:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

#     --------OR--------

list2 = eval(input("Enter your list: "))
if list2 == list2[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
