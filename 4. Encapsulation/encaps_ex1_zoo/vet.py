class Vet:
    counter = 0
    def __init__(self, name: str, age: int, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Vet.counter += 1

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"