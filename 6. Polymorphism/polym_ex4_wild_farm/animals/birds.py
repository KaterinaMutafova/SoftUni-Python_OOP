from abc import ABC, abstractmethod

from polym_ex4_wild_farm.animals.animal import Animal, Bird
from polym_ex4_wild_farm.food import Meat, Vegetable, Fruit


class Owl(Bird):
    INCREASE_GRAMS = 0.25
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)


    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(self.INCREASE_GRAMS, food)


class Hen(Bird):
    INCREASE_GRAMS = 0.35
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(self.INCREASE_GRAMS, food)



# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)




