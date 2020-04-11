import matplotlib.pyplot as plot
import matplotlib.axes as ax
import numpy as np
from random import *
from datatypes import *

#colors
c_ltg = "#92cc8b"
c_ltltb = "#34a7dd"
c_ltb = "#25447a"
c_dkb = "#0c0f32"
c_ltr = "#c47761"

def drawAllPawns(index, population):
	path = "EpidemySim/source/imgs/sim/output" + '{:04d}'.format(index) + ".png"
	plot.figure(1)
	plot.axis([0, 100, 0, 100])
	ax = plot.subplot()
	ax.set_aspect('equal')
	#ax.set_facecolor("black")
	ax.patch.set_facecolor(c_dkb)
	plot.rcParams['figure.facecolor'] = 'black'
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
	ax.scatter(healthyPawnsX, healthyPanwsY, 50, c_ltb)
	ax.scatter(infectedPawnX, infectedPawnY, 50, c_ltr)
	plot.savefig(path, facecolor = c_ltb)
	plot.cla()

def drawSimStatistics(index, totalTime, totalPopulation, infectedValues, healthyValues):
	path = "EpidemySim/source/imgs/stats/output" + '{:04d}'.format(index) + ".png"
	plot.figure(2)
	graph = plot.subplot()
	graph.patch.set_facecolor(c_dkb)
	graph.axis([0, totalTime, 0, totalPopulation])
	graph.plot(infectedValues,color=c_ltltb, linestyle='-')
	graph.plot(healthyValues, color= c_ltg, linestyle='-')
	plot.ylabel("population")
	plot.xlabel("time")
	#plot.show()
	plot.savefig(path, facecolor=c_ltb)