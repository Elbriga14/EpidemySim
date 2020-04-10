import numpy as np
import random
from datatypes import *
from population import *

class pawn():
    pos = Loc(0, 0)
    parentSector = 0
    status = healthStatus.HEALTHY
    def __init__(self):
        self.pos = Loc(random.uniform(0, 100), random.uniform(0, 100))
        self.status = healthStatus.HEALTHY
    def changeLocation(self, averageAmount):
        self.pos.x = np.clip(self.pos.x + random.uniform(-averageAmount, averageAmount), 0, 100)
        self.pos.y = np.clip(self.pos.y + random.uniform(-averageAmount, averageAmount), 0, 100)
    def debugPos(self):
        print("pos", str(int(self.pos.x)), ";", str(int(self.pos.y)))
    def attributeSector(self, sector):
        if self.parentSector != sector:
            if self.parentSector != 0:
                self.parentSector.removeInhibitant(self)
            self.parentSector = sector
            self.parentSector.addInhibitant(self)
    def becomeInfected(self, population):
        if self.status != healthStatus.INFECTED :
            self.status = healthStatus.INFECTED
            population.healthyPawnSet.remove(self)
            population.infectedPawnSet.append(self)
    def debugStatus(self):
        print(str(self.status))
    def getPawnsInRadius(self, radius):
        pawnsToCheck = []
        for sector in self.parentSector.adjacentSectors:
            for inhiba in sector.inhibitants:
                pawnsToCheck.append(inhiba)
        for inhibb in self.parentSector.inhibitants:
            pawnsToCheck.append(inhibb)
        pawnsToCheck.remove(self)
        #print("pawns to check : " + str(len(pawnsToCheck)))
        pawnsInRadius = []
        for pawn in pawnsToCheck:
            vec = np.array([pawn.pos.x - self.pos.x, pawn.pos.y - self.pos.y])
            mag = np.sqrt(vec.dot(vec))
            if mag <= radius:
                pawnsInRadius.append(pawn)
        #print("pawns in radius: ", len(pawnsInRadius))
        return pawnsInRadius

    def isInfectedPawnInRadius(self, radius):
        for pawn in self.getPawnsInRadius(radius):
            if pawn.status == healthStatus.INFECTED or pawn.status == healthStatus.SICK:
                return True