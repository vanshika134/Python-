# USING CLASS METHOD (@classmethod)
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Vanshika bansal")
print(p1.name)
print(Person.name)



class Person:
    name = "anonymous"    # class ka name alag hai

    def changeName(self, name):
        self.name = name    # object ke andr ek nya name variable create hua hai

p1 = Person()
p1.changeName("Vanshika bansal")
print(p1.name)
print(Person.name)

# but now we have to change class attribute

class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("Vanshika bansal")
print(p1.name)
print(Person.name)

#           oooooooorrrrrrrr

class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Vanshika bansal"

p1 = Person()
p1.changeName("Vanshika bansal")
print(p1.name)
print(Person.name)


'''
1] Static methods
2] Class methods (cls)
3] Instance methods(self)
'''

