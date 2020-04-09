import matplotlib.pyplot as plot
import matplotlib.axes as ax
import numpy as np
from random import *
from datatypes import *

def drawAllPawns(pawnset, index):
	path = "EpidemySim/source/imgs/output" + '{:04d}'.format(index) + ".png"
	plot.axis([0, 100, 0, 100])
	ax = plot.subplot()
	ax.set_aspect('equal')
	for pawn in pawnset:
		color = "black"
		if pawn.status == healthStatus.HEALTHY:
			color = "black"
		else:
			color = "red"
		ax.scatter(pawn.pos.x, pawn.pos.y, 50, color)
	plot.savefig(path)
	plot.cla()