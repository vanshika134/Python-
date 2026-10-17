# From a file containing numbers separated by comma, print the count of even numbers.

with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\numbers.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]


# oooooooooooorrrrrrrrrrrrr

count = 0
with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(f"Count of even numbers: {count}")