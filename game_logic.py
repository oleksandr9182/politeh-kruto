# game_logic.py
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INVADER_SPEED = 2

# Спрощений клас-заглушка для unit-тестів
class MockTurtle:
    def __init__(self, x, y, direction=1):
        self._x = x
        self._y = y
        self.direction = direction

    def xcor(self): return self._x
    def ycor(self): return self._y
    def setx(self, x): self._x = x
    def sety(self, y): self._y = y

# Функція для руху "алієна"
def muovi_aliena(aliena):
    x = aliena.xcor()
    x += aliena.direction * 5
    aliena.setx(x)

    if x > 290 or x < -290:
        aliena.direction *= -1
        y = aliena.ycor()
        y -= 40
        aliena.sety(y)

# Генерація power-up об'єкта
def genera_powerup():
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    return x, y
