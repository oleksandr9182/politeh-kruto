# test_game.py
import unittest
from game_logic import muovi_aliena, genera_powerup, MockTurtle

class TestGameLogic(unittest.TestCase):
    def test_muovi_aliena_normal(self):
        aliena = MockTurtle(0, 200, 1)
        muovi_aliena(aliena)
        self.assertEqual(aliena.xcor(), 5)
        self.assertEqual(aliena.ycor(), 200)

    def test_muovi_aliena_boundary_right(self):
        aliena = MockTurtle(291, 200, 1)
        muovi_aliena(aliena)
        self.assertEqual(aliena.direction, -1)
        self.assertEqual(aliena.ycor(), 160)

    def test_muovi_aliena_boundary_left(self):
        aliena = MockTurtle(-291, 200, -1)
        muovi_aliena(aliena)
        self.assertEqual(aliena.direction, 1)
        self.assertEqual(aliena.ycor(), 160)

    def test_genera_powerup_range(self):
        for _ in range(100):
            x, y = genera_powerup()
            self.assertGreaterEqual(x, -290)
            self.assertLessEqual(x, 290)
            self.assertGreaterEqual(y, 100)
            self.assertLessEqual(y, 250)

if __name__ == '__main__':
    unittest.main()
