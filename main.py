#!/usr/bin/python

from differential import *
from expectation import *
from matplotlib import pyplot
import pylab
import numpy
'''
arr = getExpectation(xbar=0, s=1, n=100, a=0.01, b=5, nbins=500, pr=True)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)

for (za, exp, mn, mp) in arr:
	ax.plot([mn, mp], [exp, exp], color='orange', linewidth=2)

pyplot.savefig("result.png")
pyplot.show()
'''

def f(x):
	return 2*reverseExpectation(x, xbar=0, s=10, n=100, nbins=500)

def fprime(x):
	return diff(f, x, nbins=1000)

def fdoubleprime(x):
	return diff(fprime, x, nbins=100)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)

x = pylab.linspace(0.001, 7, 100)
ax.plot(x, map(f, x), color='black')
ax.plot(x, map(fprime, x), color='red')
ax.plot(x, map(fdoubleprime, x), color='orange')
pyplot.show()


