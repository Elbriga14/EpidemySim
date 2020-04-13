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

daysElapsed = []
infectedValues = []
healthyValues = []

#the simulation space
simSpace = playground(8)

#initialize population
pop = population(simSpace, int(input("population size: ")), int(input("infected: ")), int(input("average movement: ")))
#pop.debugPopulation()

#Create a new virus
virus = virus(float(input("virus infection radius: ")), float(input("virus infection chance: ")))

#for sector in playground.sectors:
#	sector.debugSector()

#define simulation duration
simTime = int(input("steps to simulate: "))
loopCount = 0
print(loopCount)

def mainloop():
	global loopCount

	#PROGRESS BAR
	_ = system('cls')
	pbarF = ""
	pbarE = ""
	for i in range (0, int((((loopCount/simTime)*50)))):
	 	pbarF += "|"
	for i in range (int((((loopCount/simTime)*50))), 50):
		pbarE += "."
	print(pbarF + pbarE)
	print("simulating... ", round((loopCount/simTime)*100, 1), "%")

	drawSimStatistics(loopCount, simTime, pop.size, infectedValues, healthyValues)
	drawAllPawns(loopCount, pop)

	# pawnsToInfect = []
	# for pawn in pop.pawnSet:
	# 	if pawn.isInfectedPawnInRadius(virus.InfectionRadius):
	# 		pawnsToInfect.append(pawn)
	# for pawn in pawnsToInfect:
	# 	pawn.becomeInfected(pop)
	pop.updatePawnInfected(virus)
	pop.moveAllPawns()
	daysElapsed.append(loopCount)
	infectedValues.append(len(pop.infectedPawnSet))
	healthyValues.append(len(pop.healthyPawnSet))
	loopCount = loopCount + 1
	if loopCount < simTime:
		mainloop()
	else:
		#_ = system('cls')
		totalInfected = len(pop.infectedPawnSet)
		print("Start population infected:       ", str(pop.startInfected))
		print("Final population infected:       ", str(totalInfected))
		print("Start population infected ratio: ", str(round((100*(pop.startInfected/pop.size)), 1)), "%")
		print("Final infected ratio:            ", str(round((100*(totalInfected/pop.size)), 1)), "%")
		print("Number of days elapsed:          ", str(simTime), "days")
		print("Population density:              ", str(round((pop.size/100), 1)), "p/u²")

mainloop()