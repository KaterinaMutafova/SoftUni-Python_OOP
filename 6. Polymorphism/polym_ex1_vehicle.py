from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def CONSUMPTION_PER_KM_AIR_C(self):
        pass

    def drive(self, distance):
        needed_fuel = distance * (self.CONSUMPTION_PER_KM_AIR_C + self.fuel_consumption)
        if self.fuel_quantity < needed_fuel:
            return
        self.fuel_quantity -= needed_fuel

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION_PER_KM_AIR_C = 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_PER_KM_AIR_C = 1.6

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95



car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


