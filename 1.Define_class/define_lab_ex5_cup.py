# Create a class called Cup. Upon initialization it should receive size
# and quantity (a number representing how much liquid is in it). The class
# should also have a method called fill(milliliters) which will increase the
# amount of liquid in the cup with the given milliliters (if there is space in
# the cup, otherwise ignore). The cup should also have a status() method which
# will return the amount of free space left in the cup. Submit only the class in
#     the judge system. Don't forget to test your code.


class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, millilitres: int):
        if self.size - self.quantity >= millilitres:
            self.quantity += millilitres
        return self.quantity


    def status(self):
        space = self.size - self.quantity
        return space



cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
