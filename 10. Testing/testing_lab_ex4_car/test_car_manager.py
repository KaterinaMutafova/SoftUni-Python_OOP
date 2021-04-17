from testing_lab_ex4_car.car_manager import Car

from unittest import TestCase, main

class TestCar(TestCase):
    def setUp(self) -> None: # make, model, fuel_consumption, fuel_capacity
        self.car = Car("Nisan", "PathFinder", 10, 50)


    def test_car_is_set(self):
        self.assertEqual("Nisan", self.car.make)
        self.assertEqual("PathFinder", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_car_empty_string(self):
        with self.assertRaises(Exception) as exc:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(exc.exception))

    def test_set_make_car_to_new_value(self):
        self.car.make = "Kia"
        self.assertEqual("Kia", self.car.make)

    def test_set_model_car_to_empty_string(self):
        with self.assertRaises(Exception) as exc:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(exc.exception))

    def test_set_model_car_to_new_value(self):
        self.car.model = "Sportage"
        self.assertEqual("Sportage", self.car.model)

    def test_set_fuel_consumption_to_negative_or_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_consumption = -10
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(exc.exception))

    def test_set_fuel_consumption_to_new_value(self):
        self.car.fuel_consumption = 15
        self.assertEqual(15, self.car.fuel_consumption)

    def test_set_fuel_capacity_to_negative_or_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_capacity = -50
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(exc.exception))

    def test_set_fuel_capacity_to_new_value(self):
        self.car.fuel_capacity = 55
        self.assertEqual(55, self.car.fuel_capacity)

    def test_set_fuel_amount_to_negative_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(exc.exception))

    def test_set_fuel_amount_to_new_value(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_set_new_fuel_amount_to_negative_or_zero_raises_exc(self):
        with self.assertRaises(Exception) as exc:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(exc.exception))

    def test_refuel_set_new_fuel_to_positive_amount(self):
        self.car.refuel(10)
        self.car.refuel(20)
        self.assertEqual(30, self.car.fuel_amount)


    def test_refuel_with_more_fuel_than_capacity(self):
        self.car.refuel(51)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_car_with_enaugh_fuel(self):
        self.car.refuel(11)
        self.car.drive(100)
        self.assertEqual(1, self.car.fuel_amount)

    def test_drive_car_without_enough_fuel(self):
        self.car.refuel(9)
        with self.assertRaises(Exception) as exc:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(exc.exception))




if __name__ == '__main__':
    main()