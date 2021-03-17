# Liskov Substitution Principle ->  Всяка една  функция, която  може да се приложи на инстанциите на
# наследниците трябва да може да  се приложи и инстанциите на родителския клас

from abc import ABC,abstractmethod

class Robot(ABC):
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    @abstractmethod
    def get_senzors_count(self):
        pass


class Android(Robot):
    def get_senzors_count(self):
        return 4


class Chappie(Robot):
    def get_senzors_count(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.get_senzors_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)