
from __future__ import division
from integration import *
import math

def getExpectation(xbar, s, n, a=1, b=4.5, nbins=100, rndnum=4):
	arr = []
	fr = int(a * nbins)
	ds = int(b * nbins)
	for za in range(fr, ds, 1):
		exp = round(integTrap(0, za/nbins, z, 1000)*2, rndnum+2)
		mp = round(xbar + ((za/nbins) * (s/math.sqrt(n))), rndnum)
		mn = round(xbar - ((za/nbins) * (s/math.sqrt(n))), rndnum)
		arr.append((za/nbins, round(exp*100, rndnum), mn, mp))
	return arr

