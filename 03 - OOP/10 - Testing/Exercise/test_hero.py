from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("a", 3, 2.5, 4.5)

    def test_battle_fighting_yourself(self) -> None:
        with self.assertRaises(Exception) as error:
            self.hero.battle(Hero("a", 1, 1, 1))

        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_when_no_hero_health(self) -> None:
        self.hero.health = -2
        with self.assertRaises(ValueError) as error:
            self.hero.battle(Hero("b", 1, 1, 1))

        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest",
            str(error.exception)
        )

        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(Hero("b", 1, 1, 1))

        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest",
            str(error.exception)
        )

    def test_battle_when_no_enemy_health(self) -> None:
        enemy = Hero("b", 0, 0, 0)

        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)

        self.assertEqual(
            f"You cannot fight {enemy.username}. He needs to rest",
            str(error.exception)
        )

        enemy = Hero("b", 0, -100, 0)

        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)

        self.assertEqual(
            f"You cannot fight {enemy.username}. He needs to rest",
            str(error.exception)
        )

    def test_battle_win_health_is_taken_correctly(self) -> None:
        enemy_damage = 1
        hero_damage = self.hero.damage * self.hero.level

        enemy = Hero("b", 1, 1, 1)
        self.hero.battle(enemy)

        self.assertEqual(4, self.hero.level)
        self.assertEqual(7.5 - enemy_damage, self.hero.health)
        self.assertEqual(9.5, self.hero.damage)

        self.assertEqual(1, enemy.level)
        self.assertEqual(1 - hero_damage, enemy.health)
        self.assertEqual(1, enemy.damage)
        
    def test_battle_losing_health_is_taken_correctly(self) -> None:
        enemy_damage = 10000
        hero_damage = self.hero.damage * self.hero.level

        enemy = Hero("b", 100, 100, 100)
        self.hero.battle(enemy)

        self.assertEqual(3, self.hero.level)
        self.assertEqual(2.5 - enemy_damage, self.hero.health)
        self.assertEqual(4.5, self.hero.damage)

        self.assertEqual(101, enemy.level)
        self.assertEqual(100 - hero_damage + 5, enemy.health)
        self.assertEqual(100 + 5, enemy.damage)

    def test_battle_draw(self) -> None:
        self.assertEqual(
            "Draw",
            self.hero.battle(Hero("b", 3, 2.5, 4.5))
        )

    def test_battle_win(self) -> None:
        self.assertEqual(
            "You win",
            self.hero.battle(Hero("b", 1, 1, 1))
        )

    def test_battle_lose(self) -> None:
        self.assertEqual(
            "You lose",
            self.hero.battle(Hero("b", 100, 100, 100))
        )

    def test_string_method(self) -> None:
        expected = (
            f"Hero {self.hero.username}: {self.hero.level} lvl\n"
            f"Health: {self.hero.health}\n"
            f"Damage: {self.hero.damage}\n"
        )

        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
