# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

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
print(my_electric.model)
print(my_electric.full_name())