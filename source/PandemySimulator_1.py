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
sickValues = []

#the simulation space
simSpace = playground(8)

#initialize population
pop = population(simSpace, int(input("population size: ")), int(input("infected: ")), float(input("average movement: ")))
#pop.debugPopulation()

#Create a new virus
virus = virus(float(input("virus infection radius: ")), float(input("virus infection chance: ")), float(input("virus infection to disease speed (0 to 1): ")))

#for sector in playground.sectors:
#	sector.debugSector()

#define simulation duration
simTime = int(input("steps to simulate: "))
loopCount = 0
print(loopCount)

def printProgressBar():
	_ = system('cls')
	pbarF = ""
	pbarE = ""
	for i in range (0, int((((loopCount/simTime)*50)))):
	 	pbarF += "|"
	for i in range (int((((loopCount/simTime)*50))), 50):
		pbarE += "."
	print(pbarF + pbarE)
	print("simulating... ", round((loopCount/simTime)*100, 1), "%")

def drawGraphs():
	drawSimStatistics(loopCount, simTime, pop.size, infectedValues, healthyValues, sickValues)
	drawAllPawns(loopCount, pop)

def mainloop():
	global loopCount

	printProgressBar()
	drawGraphs()
	pop.tick(virus)

	#keep track of values
	daysElapsed.append(loopCount)
	infectedValues.append(len(pop.infectedPawnSet))
	healthyValues.append(len(pop.healthyPawnSet))
	sickValues.append(len(pop.sickPawnSet))
	loopCount = loopCount + 1
	if loopCount < simTime:
		mainloop()
	else:
		printProgressBar()
		totalInfected = len(pop.infectedPawnSet)
		totalSick = len(pop.sickPawnSet)
		print("[P] Start population infected:       ", str(pop.startInfected))
		print("[P] Final population infected:       ", str(totalInfected))
		print("[P] Final population sick:           ", str(totalSick))
		print("[P] Start population infected ratio: ", str(round((100*(pop.startInfected/pop.size)), 1)), "%")
		print("[P] Final infected ratio:            ", str(round((100*(totalInfected/pop.size)), 1)), "%")
		print("[P] Final sick ratio:                ", str(round((100*(totalSick/pop.size)), 1)), "%")
		print("[P] Population density:              ", str(round((pop.size/100), 1)), "p/u²")
		print("[t] Number of days elapsed:          ", str(simTime), "days")
		print(virus)

mainloop()