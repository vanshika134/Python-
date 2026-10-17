class Car:
    def __inint__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True  # These unnecessary lines are just to show that we can access attributes of the class using self reference
        self.acc = True     # These are hidden called abstraction, we don't need to know about these attributes, we just need to know that we can start the car using start method
        print("Car started")

car1 = Car()
car1.start()

# ek class bna di usme attributes and functions bi hai 
# vo encapsulation hota hai...