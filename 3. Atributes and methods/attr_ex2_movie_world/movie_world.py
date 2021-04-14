from typing import List

from attr_ex2_movie_world.customer import Customer
from attr_ex2_movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name  = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        the_customer = [c for c in self.customers if c.id == customer_id][0]
        the_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        for c in self.customers:
            if the_dvd in c.rented_dvds and c == the_customer:
                return f"{the_customer.name} has already rented {the_dvd.name}"
            elif the_dvd in c.rented_dvds:
                return "DVD is already rented"
        if the_customer.age < the_dvd.age_restriction:
            return f"{the_customer.name} should be at least {the_dvd.age_restriction} to rent this movie"
        the_customer.rented_dvds.append(the_dvd)
        the_dvd.is_rented = True
        return f"{the_customer.name} has successfully rented {the_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        the_customer = [c for c in self.customers if c.id == customer_id][0]
        the_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if the_dvd in the_customer.rented_dvds:
            the_customer.rented_dvds.remove(the_dvd)
            the_dvd.is_rented = False
            return f"{the_customer.name} has successfully returned {the_dvd.name}"
        else:
            return f"{the_customer.name} does not have that DVD"

    def __repr__(self):
        result = '\n'.join([c.__repr__() for c in self.customers])
        result += '\n'
        result += '\n'.join([d.__repr__() for d  in self.dvds])
        return result




# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 18)
# c = Customer("Pesho", 16, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# result = movie_world.rent_dvd(4, 1)
#
# print(result)








