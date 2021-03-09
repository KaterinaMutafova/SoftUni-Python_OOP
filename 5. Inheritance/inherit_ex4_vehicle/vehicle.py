

class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = float(fuel)
        self.horse_power = int(horse_power)
        self.fuel_consumption = float(self.__class__.DEFAULT_FUEL_CONSUMPTION)

    def drive(self, kilometers):
        if self.fuel >= kilometers * self.__class__.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * self.__class__.DEFAULT_FUEL_CONSUMPTION





