#!/usr/bin/python

from expectation import *
from matplotlib import pyplot
import numpy

arr = getExpectation(xbar=0, s=1, n=100, a=0.01, b=5, nbins=500, pr=True)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)

for (za, exp, mn, mp) in arr:
	ax.plot([mn, mp], [exp, exp], color='orange', linewidth=2)

pyplot.savefig("result.png")
pyplot.show()

