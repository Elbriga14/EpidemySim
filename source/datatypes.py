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
    def __str__(self):
        return str(self.x) + " ; " + str(self.y)
    def __abs__(self):
        #vector magnitude
        return ((self.x ** 2 + self.y ** 2) ** 0.5)
    def __add__(self, o):
        return Loc((self.x+o.x),(self.y+o.y))
    def __sub__(self, o):
        return Loc((self.x - o.x), (self.y - o.y))
    def __mul__(self, o):
        if isinstance(o, float) or isinstance(o, int):
            return Loc((self.x * o), (self.y * o))
        elif isinstance(o, Loc):
            return Loc((self.x * o.x), (self.y * o.y))
        else:
            print("can only multiply Loc type with Loc, int or float type")
    def __div__(self, o):
        if isinstance(o, float) or isinstance(o, int):
            return Loc((self.x / o), (self.y / o))
        elif isinstance(o, Loc):
            return Loc((self.x / o.x), (self.y / o.y))
        else:
            print("can only divide Loc type with Loc, int or float type")
    def norm(self):
        mag = abs(self)
        return Loc(self.x/mag, self.y/mag)