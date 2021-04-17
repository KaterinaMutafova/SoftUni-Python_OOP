from testing_lab_ex1_worker.test_lab_ex1_solution import Worker

from unittest import TestCase, main

class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Katerina", 1500, 100)
    def test_worker_is_initialized(self):
        self.assertEqual(self.worker.name, "Katerina")
        self.assertEqual(self.worker.salary, 1500)
        self.assertEqual(self.worker.energy, 100)

    def test_if_energy_is_incremented_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_worker_is_raising_exception_if_working_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_is_increasing_his_salary_after_working(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_worker_is_decreasing_his_energy_after_working(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(old_energy - self.worker.energy, 1)

    def test_string_repr_after_get_info(self):
        self.worker.work()
        self.worker.get_info()
        self.assertEqual('Katerina has saved 1500 money.', self.worker.get_info())




if __name__ == '__main__':
    main()

