def myFunc():
    print("Hello World!")
myFunc()
print(__name__)

if __name__ == "__main__":
# if this code is directly executed by running the file its present in
    print("This is main.py")
    myFunc()
    print(__name__)