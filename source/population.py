
from pawn import *

class population():
	pawnSet, healthyPawnSet, infectedPawnSet, sickPawnSet = [], [], [], []
	
	def __init__(self, simSpace, size, startInfected, avgMov):
		self.simSpace = simSpace
		self.size = size
		self.averageMovement = avgMov
		if startInfected > size:
			self.startInfected = size
		else: self.startInfected = startInfected
		for i in range (0, self.size):
			self.pawnSet.append(pawn())
			self.simSpace.attributeSector(self.pawnSet[i])
		self.healthyPawnSet = self.pawnSet.copy()
		for i in range(0, self.startInfected):
			self.pawnSet[i].becomeInfected(self)

	def moveAllPawns(self):
		for pawn in self.pawnSet:
			pawn.changeLocation(self.averageMovement)
			self.simSpace.attributeSector(pawn)

	def debugPopulation(self):
		print("population size: ", len(self.pawnSet))
		print("healthy population: ", len(self.healthyPawnSet))
		print("infected population: ", len(self.infectedPawnSet))
		print("sick population: ", len(self.sickPawnSet))