from testing_lab_ex2_cat.cat import Cat

from unittest import TestCase, main

class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Kitty")

    def test_cat_size_increases_after_eating(self):
        old_size = self.cat.size
        self.cat.eat()
        self.assertEqual(self.cat.size - old_size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_after_fed_raises_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual("Already fed.", exc.exception.args[0])

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(str(exc.exception), 'Cannot sleep while hungry')

    def test_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()






