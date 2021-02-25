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
