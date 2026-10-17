class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345" , "abcde")
print(acc1.acc_no)
# print(acc1.acc_pass)    # but we need it private info..
# Iske liye hum acc_pass ke agey __ (do underscore) lga dege
# now it shows this :(Now we cannot access it outside class)
# AttributeError: 'Account' object has no attribute 'acc_pass'
print(acc1.reset_pass())    
# ye class ke andr ka code hai, jo sirf hme pta hai...


class Person:
    __name = "anonymous"
p1 = Person()
print(p1.__name)  
#AttributeError: 'Person' object has no attribute '__name'


class Person:
    def __hello():
        print("Hello person!")
p1 = Person()
print(p1.hello())    # Error


class Person:
    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()
p1 = Person()
print(p1.welcome())    