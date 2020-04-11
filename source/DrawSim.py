import matplotlib.pyplot as plot
import matplotlib.axes as ax
import numpy as np
from random import *
from datatypes import *

def drawAllPawns(index, population):
	path = "EpidemySim/source/imgs/sim/output" + '{:04d}'.format(index) + ".png"
	plot.figure(1)
	plot.axis([0, 100, 0, 100])
	ax = plot.subplot()
	ax.set_aspect('equal')
	healthyPawnsX = []
	healthyPanwsY = []
	infectedPawnX = []
	infectedPawnY = []
	for pawn in population.healthyPawnSet:
		healthyPawnsX.append(pawn.pos.x)
		healthyPanwsY.append(pawn.pos.y)
	for pawn in population.infectedPawnSet:
		infectedPawnX.append(pawn.pos.x)
		infectedPawnY.append(pawn.pos.y)
	ax.scatter(healthyPawnsX, healthyPanwsY, 50, "black")
	ax.scatter(infectedPawnX, infectedPawnY, 50, "red")
	plot.savefig(path)
	plot.cla()

def drawSimStatistics(index, totalTime, totalPopulation, infectedValues, healthyValues):
	path = "EpidemySim/source/imgs/stats/output" + '{:04d}'.format(index) + ".png"
	plot.figure(2)
	graph = plot.subplot()
	#graph.set_aspect('equal')
	graph.axis([0, totalTime, 0, totalPopulation])
	graph.plot(infectedValues, 'b-')
	graph.plot(healthyValues, 'g-')
	plot.ylabel("population")
	plot.xlabel("time")
	#plot.show()
	plot.savefig(path)