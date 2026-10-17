f = open("sample.txt", "w")
f.close()
# As sample.txt file doesn't exist , it will create new in same directory.
f = open("sample1.txt", "a")
f.close()