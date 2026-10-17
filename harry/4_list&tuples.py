# List [mutable]
friends = ["Apple", "Orange", 4, 4.5, True, False, None]
print(friends[0])
friends[0] = "Grapes"     # unlike strings lists are mutable
print(friends[0])         # Indexing
print(friends[0:5])       # Slicing
            # methods
friends.append("Vanshika")
print(friends)
l1 = [1,432,12,567,43,34,345,23,1,3,5,287,5674,3,45]
l1.sort()
print(l1)
# print(l1.pop(3))        Index ki value return krega
l1.pop(3)                 # Removes element at idx...
print(l1)
l1.insert(2,3343423)
print(l1)


# Tuple (immutable)
a = (1,2,3,4,4)
print(type(a))
a = ()
print(type(a))
a = (6,)
print(type(a))
a = (1,542,45.3,"Vanshika" , True, None,"Bansal")
# a[0]="Harry"  #TypeError: 'tuple' object does not support item assignment
print(a)
print(type(a))
            # methods
t = (1,542,45.3,542,"Vanshika","Vanshika",True, None,"Bansal")
print(t.count(542))
print(t.index("Vanshika"))
print(t*2) # repeatition


# 1111(WAP to store seven fruits entered by thr user)
l1 = []
n = input("Enter your values ")
l1.append(n)
n = input("Enter your values ")
l1.append(n)
n = input("Enter your values ")
l1.append(n)
n = input("Enter your values ")
l1.append(n)
n = input("Enter your values ")
l1.append(n)
n = input("Enter your values ")
l1.append(n)
n = input("Enter your values ")
l1.append(n)
print(l1)


# 2222(Marks of 6 students and sort them)
l2 = []
n = int(input("Enter your marks "))
l2.append(n)
n = int(input("Enter your marks "))
l2.append(n)
n = int(input("Enter your marks "))
l2.append(n)
n = int(input("Enter your marks "))
l2.append(n)
n = int(input("Enter your marks "))
l2.append(n)
n = int(input("Enter your marks "))
l2.append(n)
n = int(input("Enter your marks "))
l2.append(n)
print(l2)
print(sorted(l2))


# 3333
# a = (34,234,"Harry")
# a[3] = "Larry"    #TypeError: 'tuple' object does not support item assignment


# 4444
l = [34,23,645,123]
print(sum(l))


# 5555
a = (7,0,8,0,0,9)
print(a.count(0))
