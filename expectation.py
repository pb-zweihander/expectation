
from __future__ import division
from integration import *
import math
from matplotlib import pyplot
import numpy

def getExpectation(xbar, s, n, a=1, b=4.5, nbins=100, rndnum=4, pr=False, pl=True, sh=True, plfn=None):
	arr = []
	fig = None
	ax = None
	if pl:
		fig = pyplot.figure()
		ax = fig.add_subplot(1, 1, 1)
		if sh:
			pyplot.show()
	fr = int(a * nbins)
	ds = int(b * nbins)
	for za in range(fr, ds, 1):
		exp = round(integTrap(z, 0, za/nbins, nbins)*2, rndnum+2)
		mp = round(xbar + ((za/nbins) * (s/math.sqrt(n))), rndnum)
		mn = round(xbar - ((za/nbins) * (s/math.sqrt(n))), rndnum)
		if pl:
			ax.plot([mn, mp], [exp, exp], color='orange', linewidth=2)
		if pr:
			print("%s - %s : [%s, %s]" % (round(za/nbins, rndnum), exp, mn, mp))
		arr.append((za/nbins, round(exp*100, rndnum), mn, mp))
	if pl and plfn:
		pyplot.savefig(filename)
	if pl:
		return {'array':arr, 'figure':fig, 'axis':ax}
	else:
		return arr

