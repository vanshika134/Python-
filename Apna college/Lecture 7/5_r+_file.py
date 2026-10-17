f = open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\demo5.txt", "r+")
f.write("ABC")  # ABC is overwrite on Thi
print(f.read()) # This will read the remaining part of the file after ABC
f.close()

# pointer in start in read+ (no truncate) mode, so it will overwrite the data from start and then read the remaining part of the file after ABC.
# write+ - overwrite, truncate(Clear) the file and write new data, if file doesn't exist then create new file.
# a+ - pointer at end of file, so it will append the data at end of file, if file doesn't exist then create new file.(no truncate)

