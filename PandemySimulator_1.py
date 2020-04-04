from enum import Enum
from os import system
import random
import numpy
import asyncio
import time

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

        
            
class sector:
    position = [0,0]
    index = 0
    min = [0, 0]
    max = [0, 0]
    inhibitants = []
    adjacentSectors = []
    def __init__(self, x, y, min, max, index):
        self.position = [x, y]
        self.min = min
        self.max = max
        self.index = index
        #print ("sector: ")
        #print (self.position)
        #print(self.min, self.max)
    def addInhibitant(self, pawn):
        self.inhibitants.append(pawn)
    def removeInhibitant(self, pawn):
        self.inhibitants.remove(pawn)
    def setAdjacentSectors(self, sectors):
        for sector in sectors:
            self.adjacentSectors.append(sector)


class playground:
    subdivisions = 0
    sectors = []
    def __init__(self, size):
        self.subdivisions = size
        index = 0
        for i in range (0, size):
            for j in range (0, size):
                min = [j*(100/size), i*(100/size)]
                max = [(j+1)*(100/size), (i+1)*(100/size)]
                self.sectors.append(sector(i, j, min, max, index))
                index = index + 1
        #we need to tell each sector its adjacent sectors:
        for i in range (0, len(self.sectors)):
            adjSectors = []
            if i%(self.subdivisions) != 0:
                adjSectors.append(self.sectors[i-1])
            if (i+1)%(self.subdivisions) != 0:
                adjSectors.append(self.sectors[i+1])
            if i >= self.subdivisions:
                adjSectors.append(self.sectors[i-self.subdivisions])
                if (i%(self.subdivisions) != 0):
                    adjSectors.append(self.sectors[i-self.subdivisions-1])
                if ((i+1)%self.subdivisions != 0):
                    adjSectors.append(self.sectors[i-self.subdivisions+1])
            if i < pow(self.subdivisions, 2)-self.subdivisions:
                adjSectors.append(self.sectors[i+self.subdivisions])
                if (i+1)%self.subdivisions != 0:
                    adjSectors.append(self.sectors[i+self.subdivisions+1])
                if i%self.subdivisions != 0:
                    adjSectors.append(self.sectors[i+self.subdivisions-1])
            self.sectors[i].setAdjacentSectors(adjSectors)
                


    def attributeSector(self, pawn):
        i = 100/self.subdivisions
        pawncolumn = 0
        while i <= pawn.pos.x:
            pawncolumn += 1
            i = i + (100/self.subdivisions)
        i = 100/self.subdivisions
        pawnrow = 0
        while i <= pawn.pos.y:
            pawnrow += 1
            i = i + (100/self.subdivisions)
        pawnSectorIndex = (pawnrow*(self.subdivisions)) + pawncolumn
        pawn.attributeSector(self.sectors[pawnSectorIndex])




#the simulation space
simSpace = playground(4)
#the set of people
pawnSet = []

#define population size
population = int(input("population size: "))


#initialize population
for i in range(0, population):
    pawnSet.append(pawn())
    #pawnSet[i].debugPos()
    simSpace.attributeSector(pawnSet[i])
#initialize infected population
baseInfected = int(input("infected people amount: "))
if baseInfected > population:
    baseInfected = population
for i in range (0, baseInfected):
    pawnSet[i].becomeInfected()


#define simulation duration
simTime = int(input("steps to simulate: "))
loopCount = 0
print(loopCount)

def mainloop():
    _ = system('cls')
    for pawn in pawnSet:
        pawn.changeLocation()
        pawn.debugPos()
        pawn.debugStatus()
        pawn.getPawnsInRadius(10)
    time.sleep(0.5)
    global loopCount
    loopCount = loopCount + 1
    if loopCount < simTime:
        mainloop()


mainloop()