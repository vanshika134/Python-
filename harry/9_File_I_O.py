f = open(r"D:\CODING\2 python\harry\file\file.txt","r")
data = f.read()
print(data)
f.close()
print()



# FILE ME WRITE

st = "Hey Vanshika you are amazing"
f = open(r"D:\CODING\2 python\harry\file\myfile.txt", "w")
f.write(st)
f.close()



# FILE MORE FUNCTIONS

f = open(r"D:\CODING\2 python\harry\file\file.txt")

# lines = f.readlines()         Read all lines together
# print(lines, type(lines))

# line1 = f.readline()          Read line 1
# print(line1, type(line1))

# line2 = f.readline()          Read line 2
# print(line2, type(line1))

# line3 = f.readline()          Read line 3
# print(line3, type(line1))

# line4 = f.readline()          Doesn't exist
# print(line4 == "")            True

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()



# APPEND THE FILES(Add lines in text file)

st = "\nHey Vanshika you are amazing"
f = open(r"D:\CODING\2 python\harry\file\myfile.txt", "a")
f.write(st)
f.close()



# WITH 

f = open(r"D:\CODING\2 python\harry\file\file.txt")
print(f.read())
f.close()
# The same can be written using with statement like this:
with open(r"D:\CODING\2 python\harry\file\file.txt") as f:
    print(f.read())    # you don't have to explixitely close the file



# 1111111111
f = open(r"D:\CODING\2 python\harry\file\poems1.txt")
content = f.read()
if("Twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")
f.close()


# 2222222222
import random
def game():
    print("You are playing the game...")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open(r"D:\CODING\2 python\harry\file\highscore2.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open(r"D:\CODING\2 python\harry\file\highscore2.txt", "w") as f:
            f.write(str(score))
    return score
game()


# 3333333333
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"D:\\CODING\\2 python\\harry\\file\\tables3/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(2,21):
    generateTable(i)

    
# 4444444444
word = "Donkey"
with open(r"D:\CODING\2 python\harry\file\file4.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "#####")
with open(r"D:\CODING\2 python\harry\file\file4.txt", "w") as f:
    content = f.write(contentNew)


# 5555555555 
words = ["Donkey", "human", "languages"]
with open(r"D:\CODING\2 python\harry\file\file5.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open(r"D:\CODING\2 python\harry\file\file5.txt", "w") as f:
    content = f.write(content)


# 6666666666
with open(r"D:\CODING\2 python\harry\file\log6.txt") as f:
    content = f.read()
if("Python" in content):
    print("Yes Python is present")
else:
    print("Not Present")


# 7777777777 
with open(r"D:\CODING\2 python\harry\file\log6.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("Python" in line):
        print(f"Yes Python is present, Line no: {lineno}")
        break
    lineno += 1
else:
    print("Not Present")


# 8888888888
with open(r"D:\CODING\2 python\harry\file\this8.txt") as f:
    content = f.read()
with open(r"D:\CODING\2 python\harry\file\this8_copy.txt", "w") as f:
    f.write(content)


# 9999999999
with open(r"D:\CODING\2 python\harry\file\this8.txt") as f:
    content1 = f.read()
with open(r"D:\CODING\2 python\harry\file\log6.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No these files are not identical")


# 10101010101010101010
with open(r"D:\CODING\2 python\harry\file\this8_copy.txt", "w") as f:
    f.write("")


# 11111111111111111111
with open(r"D:\CODING\2 python\harry\file\old11.txt") as f:
    content = f.read()
with open(r"D:\CODING\2 python\harry\file\renamed_by_python.txt", "w") as f:
    f.write(content)

