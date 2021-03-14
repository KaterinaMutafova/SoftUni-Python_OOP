from polym_ex5_animals.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow"