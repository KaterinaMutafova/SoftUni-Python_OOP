from unittest import TestCase, main
from testing_ex3_hero.project.hero import Hero


class TestHero(TestCase): #username: str, level: int, health: float, damage: float
    def setUp(self):
        self.main_hero = Hero("Naruto", 3, 90, 10)

    def test_instance_is_set(self):
        self.assertEqual("Naruto", self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_battle_to_fight_with_yourself(self):
        enemy = Hero("Naruto", 3, 90, 10)
        with self.assertRaises(Exception) as exc:
            self.main_hero.battle(enemy)
        self.assertEqual(enemy.username, self.main_hero.username)
        self.assertEqual("You cannot fight yourself", str(exc.exception))

    def test_battle_when_your_health_is_below_zero(self):
        enemy = Hero("Sasuke", 3, 90, 30)
        self.main_hero.battle(enemy)
        self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(Exception) as exc:
            self.main_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exc.exception))

    def test_battle_when_enemy_health_is_below_zero(self):
        enemy = Hero("Sasuke", 3, 30, 10)
        self.main_hero.battle(enemy)
        self.assertEqual(0, enemy.health)
        with self.assertRaises(Exception) as exc:
            self.main_hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(exc.exception))

    def test_battle_if_self_damage_and_enemy_damage_are_set_correctly(self):
        enemy = Hero("Sasuke", 4, 90, 10)
        self.assertEqual(30, self.main_hero.damage * self.main_hero.level)
        self.assertEqual(40, enemy.damage * enemy.level)

    def test_battle_if_health_decreases_when_in_battle(self):
        enemy = Hero("Sasuke", 4, 90, 10)
        self.main_hero.battle(enemy)
        self.assertEqual(50, self.main_hero.health)
        self.assertEqual(65, enemy.health)

    def test_battle_if_there_is_draw(self):
        self.main_hero = Hero("Naruto", 3, 90, 30)
        enemy = Hero("Sasuke", 3, 90, 30)
        self.assertEqual("Draw", self.main_hero.battle(enemy))

    def test_battle_if_you_win(self):
        self.main_hero = Hero("Naruto", 3, 100, 30)
        enemy = Hero("Sasuke", 3, 90, 30)
        self.assertEqual("You win", self.main_hero.battle(enemy))

    def test_battle_if_you_lose(self):
        self.main_hero = Hero("Naruto", 3, 80, 30)
        enemy = Hero("Sasuke", 3, 100, 30)
        self.assertEqual("You lose", self.main_hero.battle(enemy))

    def test_str_representation(self):
        self.assertEqual(f"Hero {self.main_hero.username}: {self.main_hero.level} lvl\n"
                         f"Health: {self.main_hero.health}\n"
                         f"Damage: {self.main_hero.damage}\n", self.main_hero.__str__())

    def test_battle_you_lose_enemy_points_increase(self):
        self.main_hero = Hero("Naruto", 3, 100, 30)
        enemy = Hero("Sasuke", 3, 110, 30)
        self.main_hero.battle(enemy)
        self.assertEqual(4, enemy.level)
        self.assertEqual(25, enemy.health)
        self.assertEqual(35, enemy.damage)


    def test_battle_you_win_your_points_increase(self):
        self.main_hero = Hero("Naruto", 3, 100, 30)
        enemy = Hero("Sasuke", 3, 90, 30)
        self.assertEqual("You win", self.main_hero.battle(enemy))
        self.assertEqual(4, self.main_hero.level)
        self.assertEqual(15, self.main_hero.health)
        self.assertEqual(35, self.main_hero.damage)







if __name__ == '__main__':
    main()


