from os import system
import random
import numpy
import asyncio
import time
#from datatypes import *
from pawn import *
from sector import *
from playground import *

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

for sector in playground.sectors:
	sector.debugSector()

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