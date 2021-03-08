from inherit_lab_ex2_person.employee import Employee
from inherit_lab_ex2_person.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


