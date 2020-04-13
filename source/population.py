from pawn import *

class population():
	pawnSet, healthyPawnSet, infectedPawnSet, sickPawnSet = [], [], [], []
	
	def __init__(self, simSpace, size, startInfected, avgMov):
		self.simSpace = simSpace
		self.size = size
		if startInfected > size:
			self.startInfected = size
		else: self.startInfected = startInfected
		for i in range (0, self.size):
			self.pawnSet.append(pawn(avgMov))
			self.simSpace.attributeSector(self.pawnSet[i])
		self.healthyPawnSet = self.pawnSet.copy()
		for i in range(0, self.startInfected):
			self.pawnSet[i].becomeInfected(self)

	def moveAllPawns(self):
		for pawn in self.pawnSet:
			pawn.changeLocation()
			self.simSpace.attributeSector(pawn)

	def updatePawnInfected(self, virus):
		pawnsToInfect = []
		for pawn in self.healthyPawnSet:
			# if pawn.isInfectedPawnInRadius(virus.InfectionRadius) and random.uniform(0, 1) <= virus.InfectionChance:
			# 	pawnsToInfect.append(pawn)
			infPawnsInRad = pawn.getInfectedPawnsInRadius(virus.InfectionRadius)
			if len(infPawnsInRad) > 0:
				for p in infPawnsInRad:
					if random.uniform(0, 1) <= virus.InfectionChance:
						pawnsToInfect.append(pawn)
						break
		for pawn in pawnsToInfect:
			pawn.becomeInfected(self)

	def tick(self, virus):
		self.updatePawnInfected(virus)
		self.moveAllPawns()

	def debugPopulation(self):
		print("population size: ", len(self.pawnSet))
		print("healthy population: ", len(self.healthyPawnSet))
		print("infected population: ", len(self.infectedPawnSet))
		print("sick population: ", len(self.sickPawnSet))