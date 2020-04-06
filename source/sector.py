

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
		self.inhibitants = []
		#print ("sector: ")
		#print (self.position)
		#print(self.min, self.max)
	def addInhibitant(self, pawn):
		self.inhibitants.append(pawn)
	def removeInhibitant(self, pawn):
		self.inhibitants.remove(pawn)
	def setAdjacentSectors(self, sectors):
		self.adjacentSectors = sectors
	def debugSector(self):
		print ("--- sector no " + str(self.index))
		print ("- number of adjacent sectors: " + str(len(self.adjacentSectors)))
		print ("- number of inhibitants: " + str(len(self.inhibitants)))