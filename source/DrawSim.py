import matplotlib.pyplot as plot
import matplotlib.axes as ax
import numpy as np
from random import *

def drawAllPawns(pawnset, index):
	path = "EpidemySim/source/imgs/output" + '{:04d}'.format(index) + ".png"
	plot.axis([0, 100, 0, 100])
	ax = plot.subplot()
	ax.set_aspect('equal')
	for pawn in pawnset:
		ax.scatter(pawn.pos.x, pawn.pos.y, 50, "black")
	plot.savefig(path)
	plot.cla()