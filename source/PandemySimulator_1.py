from os import system
import random
import numpy
import asyncio
import time
#from datatypes import *
from pawn import *
from sector import *
from playground import *
from DrawSim import *

#the simulation space
simSpace = playground(8)

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

#for sector in playground.sectors:
#	sector.debugSector()

#define simulation duration
simTime = int(input("steps to simulate: "))
loopCount = 0
print(loopCount)

def mainloop():
	print("a day passes")
	global loopCount
	#_ = system('cls')
	for pawn in pawnSet:
		pawn.changeLocation()
		#pawn.debugPos()
		#pawn.debugStatus()
		if pawn.isInfectedPawnInRadius(10):
			pawn.becomeInfected()
	drawAllPawns(pawnSet, loopCount)
	time.sleep(0.1)
	loopCount = loopCount + 1
	if loopCount < simTime:
		mainloop()
	else:
		totalInfected = 0
		for pawn in pawnSet:
			if pawn.status == healthStatus.INFECTED or pawn.status == healthStatus.SICK:
				totalInfected += 1
		print("Start population infected:       ", str(baseInfected))
		print("Final population infected:       ", str(totalInfected))
		print("Start population infected ratio: ", str(round((100*(baseInfected/population)), 1)), "%")
		print("Final infected ratio:            ", str(round((100*(totalInfected/population)), 1)), "%")
		print("Number of days elapsed:          ", str(simTime), "days")
		print("Population density:              ", str(round((population/100), 1)), "p/u²")



mainloop()