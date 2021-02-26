from math import log, pow, sqrt

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def set_x(self, new_x: int):
        self.x = new_x


    def set_y(self, new_y: int):
        self.y = new_y

    def distance(self, x2, y2):
        x3 = abs(self.x - x2)
        y3 = abs(self.y - y2)
        z = sqrt(pow(x3, 2) + pow(y3, 2))
        return z


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))






