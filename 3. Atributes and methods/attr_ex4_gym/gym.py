from typing import List

from attr_ex4_gym.customer import Customer
from attr_ex4_gym.equipment import Equipment
from attr_ex4_gym.exercise_plan import ExercisePlan
from attr_ex4_gym.subscription import Subscription
from attr_ex4_gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""
        the_subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        the_customer = [c for c in self.customers if c.id == the_subscription.customer_id][0]
        the_trainer = [t for t in self.trainers if t.id == the_subscription.trainer_id][0]
        the_plan = [p for p in self.plans if p.trainer_id == the_trainer.id][0]
        the_equipment = [e for e in self.equipment if e.id == the_plan.equipment_id][0]
        return f"{the_subscription}\n{the_customer}\n{the_trainer}\n{the_equipment}\n{the_plan}"


# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
