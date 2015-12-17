
from __future__ import division
from integration import *
import math

def getExpectation(xbar=0, s=1, n=100, a=1, b=4.5, nbins=100, pr=False):
	arr =[]
	fr = int(a * nbins)
	ds = int(b * nbins)
	for za in range(fr, ds, 1):
		exp = integTrap(z, 0, za/nbins, nbins)*2
		mp = xbar + ((za/nbins) * (s/math.sqrt(n)))
		mn = xbar - ((za/nbins) * (s/math.sqrt(n)))
		if pr:
			print("%s - %s : [%s, %s]" % (za/nbins, exp, mn, mp))
		arr.append((za/nbins, exp, mn, mp))
	print("Done!")
	return arr

def reverseExpectation(mp, xbar=0, s=1, n=100, nbins=100):
	za = (mp - xbar) * math.sqrt(n) / s
	exp = integTrap(z, 0, za, nbins)
	return exp

