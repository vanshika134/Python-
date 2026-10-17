class Car:

    def __init__(self,type):    # constructor
        self.type = type

    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")
    
class ToyotaCar(Car):
    
    def __init__(self,name, type):
        super().__init__(type)  
        # super class ke andr constructir call hojyga jispe type method chla gya.
        self.name = name
        super().start()


car1 = ToyotaCar("Mercedes", "Electric")
print(car1.type)

