from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):  # name, mammal_type, sound
        self.mammal = Mammal("Amy", "Lion", "Roar")

    def test_init(self):
        self.assertEqual("Amy", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_making_sound(self):
        self.assertEqual(f"Amy makes Roar", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info(self):
        self.assertEqual(f"Amy is of type Lion", self.mammal.info())



if __name__ == '__main__':
    main()
