age = int(input("Enter your age: "))
if(age >= 18):
    if(age >= 60):
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")


marks = int(input("Enter your marks: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("Grade of the student -> " , grade)