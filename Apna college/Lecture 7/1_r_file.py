# D:\CODING\2 python\Apna college\Lecture 7\demo1.txt

f = open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\demo1.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()                # usually so that no other can access our data

print()

f = open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\demo1.txt", "r")
data = f.read(5)         # Read only 5 characters
print(data)
f.close()

print()

f = open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\demo1.txt", "r")
line1 = f.readline()     # just reads line 1 only
line2 = f.readline()     # just reads line 2 only
print(line1)
print(line2)
line3 = f.readline()     # This will give an empty space
print(line3)
f.close()

# AGR HMNE EK BR DATA KO READ KRLIA TO BD ME EMPTY LINES AYGI


