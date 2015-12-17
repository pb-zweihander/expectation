
from __future__ import division
from math import *

def diff(f, x, nbins=100):
	assert type(nbins)==int
	h = 1/(nbins*nbins)
	
	return (f(float(x) + h) - f(float(x)))/h

