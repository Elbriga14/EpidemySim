import matplotlib.pyplot as plot
import matplotlib.axes as ax
import numpy as np
from random import *

path = "EpidemySim/source/imgs/img.png"
plot.axis([0, 100, 0, 100])
ax = plot.subplot()
ax.set_aspect('equal')

i = 0
while i < 100:
	i += 1
	ax.scatter(randint(0, 100), randint(0, 100), 50, "black")
plot.savefig(path)
plot.show(ax)
#plot.savefig(path)