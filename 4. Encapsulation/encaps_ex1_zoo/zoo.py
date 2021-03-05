from encaps_ex1_zoo.caretaker import Caretaker
from encaps_ex1_zoo.cheetah import Cheetah
from encaps_ex1_zoo.keeper import Keeper
from encaps_ex1_zoo.lion import Lion
from encaps_ex1_zoo.tiger import Tiger
from encaps_ex1_zoo.vet import Vet


class Zoo:
    def __init__(self, name:str, budget, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @property
    def worker_capacity(self):
        return self.__workers_capacity


    def add_animal(self, animal, price):
        if len(self.animals) + 1 <= self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            updated_budget = self.budget - price
            self.budget = updated_budget
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif len(self.animals) + 1 <= self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"


    def hire_worker(self, worker):
        if len(self.workers) + 1 <= self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        filtered_worker = [w for w in self.workers if w.name == worker_name]
        if filtered_worker:
            self.workers.remove(filtered_worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        for w in self.workers:
            sum_salaries += w.salary
        if self.budget >= sum_salaries:
            updated_budget = self.budget - sum_salaries
            self.budget = updated_budget
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"


    def tend_animals(self):
        sum_needs = 0
        for a in self.animals:
            sum_needs += a.get_needs()
        if self.budget >= sum_needs:
            updated_budget = self.budget - sum_needs
            self.budget = updated_budget
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        increased_budget = self.budget + amount
        self.budget = increased_budget

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([l.__repr__() for l in lions]) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join([t.__repr__() for t in tigers]) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([c.__repr__() for c in cheetahs])
        return result


    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([k.__repr__() for k in keepers]) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([c.__repr__() for c in caretakers]) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join([v.__repr__() for v in vets])
        return result




zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

