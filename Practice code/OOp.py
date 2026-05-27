class Car:
    total_cars = 0
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.year = year
        Car.total_cars += 1

    def get_brand(self):
        return "Brand is private"

    def full_name(self):
        return f"{self.year} {self.__brand} {self.__model}"
    
    @staticmethod
    def general_description():
        return "cars are a common mode of transportation"
    
    @property
    def model(self):
        return self.__model

print(Car.general_description())

my_car = Car("Honda", "Civic", 2019)
print(my_car.get_brand())
print(my_car.full_name())


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
    def model_with_battery(self):
        return f"{self.full_name()} with a {self.battery_size}-kWh battery" 
    
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.full_name())

safari_car = Car("Land Rover", "Defender", 2021)
print(safari_car.full_name())

battery_car = ElectricCar("Nissan", "Leaf", 2021, 40)

print(isinstance(battery_car, Car))  # True
print(isinstance(battery_car, ElectricCar))   # True
print(battery_car.model_with_battery())

my_electric_car = ElectricCar("Tesla", "X", 2020, 75)
print(my_electric_car.full_name())

print(f"Total cars created: {Car.total_cars}")



class Engine(Car):
    def engine_type(self):
        return "This is a generic engine type"
    
class Tire(Car):
    def tire_type(self):
        return "This is a generic tire type"
    
class Accessory(Engine, Tire, Car):
    pass

new_accessory = Accessory("Generic", "Accessory", 2022)
print(new_accessory.engine_type())  
print(new_accessory.tire_type())    