
from __future__ import division
from integration import *
import math
from matplotlib import pyplot
import numpy

def getExpectation(xbar, s, n, a=1, b=4.5, nbins=100, pr=False, pl=True, sh=True, plfn=None):
	arr = []
	fig = None
	ax = None
	if pl:
		fig = pyplot.figure()
		ax = fig.add_subplot(1, 1, 1)
	fr = int(a * nbins)
	ds = int(b * nbins)
	for za in range(fr, ds, 1):
		exp = integTrap(z, 0, za/nbins, nbins)*2
		mp = xbar + ((za/nbins) * (s/math.sqrt(n)))
		mn = xbar - ((za/nbins) * (s/math.sqrt(n)))
		if pl:
			ax.plot([mn, mp], [exp, exp], color='orange', linewidth=2)
		if pr:
			print("%s - %s : [%s, %s]" % (za/nbins, exp, mn, mp))
		arr.append((za/nbins, exp, mn, mp))
	if pl and plfn:
		pyplot.savefig(plfn)
	if pl and sh:
		pyplot.show()
	print("Done!")
	if pl:
		return {'array':arr, 'figure':fig, 'axis':ax}
	else:
		return arr

