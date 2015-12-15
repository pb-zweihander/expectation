#!/usr/bin/python

from expectation import *
from matplotlib import pyplot
import numpy

arr = getExpectation(75, 4, 64, 1, 4.5, 1000, 5)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)

for (za, exp, mn, mp) in arr:
	ax.plot([mn, mp], [exp, exp], color='orange', linewidth=3)

pyplot.savefig('result.png')
#pyplot.show()

