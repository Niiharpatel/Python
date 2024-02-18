# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    
    def get_brand(self):
        return self.__brand
    

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_car = Car("Hyundai","Venue")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_electric = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_electric.model)
# print(my_electric.full_name())

# print(my_electric.__brand)
print(my_electric.get_brand())