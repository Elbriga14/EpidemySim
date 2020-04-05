import numpy
import random
from datatypes import *

class pawn:
    pos = Loc(0, 0)
    parentSector = 0
    status = healthStatus.HEALTHY
    def __init__(self):
        self.pos = Loc(random.uniform(0, 100), random.uniform(0, 100))
        self.status = healthStatus.HEALTHY
    def changeLocation(self):
        self.pos.x = numpy.clip(self.pos.x + random.uniform(-10, 10), 0, 100)
        self.pos.y = numpy.clip(self.pos.y + random.uniform(-10, 10), 0, 100)
    def debugPos(self):
        print(self.pos.x, self.pos.y)
    def attributeSector(self, sector):
        if self.parentSector != sector:
            if self.parentSector != 0:
                self.parentSector.removeInhibitant(self)
            self.parentSector = sector
            sector.addInhibitant(self)
    def becomeInfected(self):
        self.status = healthStatus.INFECTED
    def debugStatus(self):
        print(str(self.status))
    def getPawnsInRadius(self, radius):
        pawnsToCheck = []
        for sector in self.parentSector.adjacentSectors:
            for inhiba in sector.inhibitants:
                pawnsToCheck.append(inhiba)
        for inhibb in self.parentSector.inhibitants:
            pawnsToCheck.append(inhibb)
        print("pawns to check : " + str(len(pawnsToCheck)))