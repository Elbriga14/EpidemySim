from sector import *

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
			adjSectors.clear()
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