from enum import Enum

class healthStatus(Enum):
    HEALTHY = 1
    INFECTED = 2
    SICK = 3
    CURED = 4
    DEAD = 5
    def __str__(self):
        switcher = ["healthy", "infected", "sick", "cured", "dead"]
        return switcher[self.value-1]


class Loc():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y