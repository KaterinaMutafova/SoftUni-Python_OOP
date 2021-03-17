# Open/Closed principle -> може да  се добавят нови  функционалности без да  се променят вече създадените

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species):
        self.species = species
        self.animals = []

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'bou'

class Chicken(Animal):
    def make_sound(self):
        return 'chick-chirick'



# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)