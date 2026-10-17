with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\demo6.txt", "r") as f:
    data = f.read()
    print(data)

# no need to close the file when we use with statement, it automatically closes the file after the block of code is executed.

with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\demo6.txt", "w") as f:
    f.write("new data")

