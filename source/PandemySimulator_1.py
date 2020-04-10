from os import system
import random
import numpy
import asyncio
import time
#from datatypes import *
from population import *
from pawn import *
from sector import *
from playground import *
from DrawSim import *
from virus import *


#the simulation space
simSpace = playground(8)

#the set of people
pawnSet = []

pop = population(simSpace, 100, 10, 2)
pop.debugPopulation()


#Create a new virus
virus = virus(float(input("virus infection radius: ")))

#define population size
# population = int(input("population size: "))
# avgDailyPawnMovement = float(input("Average daily pawn movement: "))

#initialize population
# for i in range(0, population):
# 	pawnSet.append(pawn())
# 	#pawnSet[i].debugPos()
# 	simSpace.attributeSector(pawnSet[i])
# #initialize infected population
# baseInfected = int(input("infected people amount: "))
# if baseInfected > population:
# 	baseInfected = population
# for i in range (0, baseInfected):
# 	pawnSet[i].becomeInfected(pop)

#for sector in playground.sectors:
#	sector.debugSector()

#define simulation duration
simTime = int(input("steps to simulate: "))
loopCount = 0
print(loopCount)

def mainloop():
	global loopCount
	print("day : ", loopCount)
	drawAllPawns(pop.pawnSet, loopCount)
	#_ = system('cls')
	pawnsToInfect = []
	for pawn in pop.pawnSet:
		if pawn.isInfectedPawnInRadius(virus.InfectionRadius):
			pawnsToInfect.append(pawn)
	for pawn in pawnsToInfect:
		pawn.becomeInfected(pop)
	pop.moveAllPawns()
	# for pawn in pawnSet:
	# 	pawn.changeLocation(avgDailyPawnMovement)
	# 	simSpace.attributeSector(pawn)
	#time.sleep(0.1)
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