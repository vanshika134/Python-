# Create a new file "practice.txt" using python. Add the following data in it:
#   Hi everyone 
#   we are learning File I/O
#   using Java.
#   I like programming in Java.

with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java.\n")



# WAF that replace all occurences of "java" with "python" in above file.

with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "python")
print(new_data) 
with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\practice.txt", "w") as f:
    f.write(new_data)

# def replace_word_in_file(file_name, old_word, new_word):
#     with open(file_name, "r") as f:
#         data = f.read()
#     new_data = data.replace(old_word, new_word)
#     with open(file_name, "w") as f:
#         f.write(new_data)



# Search if the word "learning" exists in the file or not.

def check_word():
    word = "learning"
    with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print(f"{word} exists in the file.")
        else:
            print(f"{word} does not exist in the file.")

check_word()



# WAF to find in which line the word "learning" occur first.(Print-1 if the word is not found).

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("D:\\CODING\\2 python\\Apna college\\Lecture 7\\practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()