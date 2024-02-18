# Problem: Add a class variable to Car that keeps track of the number of cars created.


class Car:

    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1 

    
    def get_brand(self):
        return self.__brand
    

    def full_name(self):
        return f"{self.brand} {self.model}"
    

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_car = Car("Hyundai","Venue")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_electric = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_electric.model)
# print(my_electric.full_name())

# print(my_electric.__brand)
# print(my_electric.get_brand())
print(my_electric.fuel_type())

safari = Car("Tata", "Safari")

print(safari.fuel_type())

print(Car.total_car)