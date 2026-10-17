a = int(input("Enter your age: "))

# if elif else ladder    (Elif clause (n no. of elif))

# If statement no. : 1
if(a%2 == 0):
    print("a is even")
# End of statement no.: 1

# If statement no. : 2
if(a>=18):
    print("You are adult")
elif(a<0):
    print("Are you losted")
elif(a==0):
    print("Ohhh!! really...")
else:
    print("You are minor")
# End of statement no.: 2

print("----End of program----")
# Operators

# else and elif can be executed without if.....


# 1111
a1 = int(input("Enter no 1 : "))
a2 = int(input("Enter no 2 : "))
a3 = int(input("Enter no 3 : "))
a4 = int(input("Enter no 4 : "))
if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greatest",a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greatest",a4)

# 2222
marks1 = int(input("Enter marks1 "))
marks2 = int(input("Enter marks2 "))
marks3 = int(input("Enter marks3 "))
per = ((marks1 + marks2 + marks3)/300)*100
if(per >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass..",per, "%")
else:
    print("You fail..",per, "%")

# 3333
p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
message = input("Enter your comment")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
    
# 4444
username = input("Enter username: ")
if(len(username) >= 10):
    print("Valid username , ", username)
else:
    print("Invalid , ", username)

# 5555
l = ["Vanshika" , "Rohan" , "Ridhi" , "Tisha"]
name = input("Enter your name ")
if(name.lower() in l):
    print("Your name is in l")
else:
    print("Not present")

# 6666
grade = int(input("Enter your marks: "))
if(grade >= 90 and grade <=100):
    grade = "Excellent"
elif(grade >= 80 and grade <90):
    grade = "A"
elif(grade >= 70 and grade <80):
    grade = "B"
elif(grade >= 60 and grade <70):
    grade = "C"
elif(grade >= 50 and grade <40):
    grade = "D"
else:
    grade = "F"
print("Your grade is , ", grade)

# 7777(WAP whether post is talking about vanshika or not)
post = input("Enter your post : ")
if("Vanshika".lower() in post.lower()):
    print("It contains your name , ", post)
else:
    print("Not your name....", post)

