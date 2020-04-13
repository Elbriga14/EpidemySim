import matplotlib.pyplot as plot
import matplotlib.axes as ax
import numpy as np
from random import *
from datatypes import *

#colors
c_ltb = "#25447a" #Healthy
c_dkb = "#0c0f32" #Background
c_ltr = "#c47761" #Infected
c_dkr = "#60101a" #Sick

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
	healthyPawnsY = []
	infectedPawnX = []
	infectedPawnY = []
	sickPawnX = []
	sickPawnY = []
	for pawn in population.healthyPawnSet:
		healthyPawnsX.append(pawn.pos.x)
		healthyPawnsY.append(pawn.pos.y)
	for pawn in population.infectedPawnSet:
		infectedPawnX.append(pawn.pos.x)
		infectedPawnY.append(pawn.pos.y)
	for pawn in population.sickPawnSet:
		sickPawnX.append(pawn.pos.x)
		sickPawnY.append(pawn.pos.y)
	ax.scatter(healthyPawnsX, healthyPawnsY, 50, c_ltb, label= "healthy")
	ax.scatter(infectedPawnX, infectedPawnY, 50, c_ltr, label ="infected")
	ax.scatter(sickPawnX, sickPawnY, 50, c_dkr, label = "sick")
	ax.legend(fancybox=True, framealpha=0.5, loc="upper right")
	plot.savefig(path, facecolor = c_ltb)
	plot.cla()

def drawSimStatistics(index, totalTime, totalPopulation, infectedValues, healthyValues, sickValues):
	path = "EpidemySim/source/imgs/stats/output" + '{:04d}'.format(index) + ".png"
	plot.figure(2)
	graph = plot.subplot()
	graph.patch.set_facecolor(c_dkb)
	graph.axis([0, totalTime, 0, totalPopulation])
	graph.plot(infectedValues,color=c_ltr, linestyle='-', label="infected")
	graph.plot(healthyValues, color= c_ltb, linestyle='-', label="healthy")
	graph.plot(sickValues, color = c_dkr, linestyle='-', label = "sick")
	graph.legend(fancybox=True, framealpha=0.5, loc="upper right")
	plot.ylabel("population")
	plot.xlabel("time")
	#plot.show()
	plot.savefig(path, facecolor=c_ltb)
	plot.cla()