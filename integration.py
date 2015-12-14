
from __future__ import division
import math

e = 2.718281828

def z(x):
	return math.pow(e, (0-(x*x))/2)/math.sqrt(2*math.pi)

def integLeft(a, b, f, nbins=10):
	h = float(b-a)/nbins
	assert h > 0
	assert type(nbins) == int
	
	s = 0.0
	for n in range(nbins):
		s = s + h * f(a + n*h)
	
	return s


def integMid(a, b, f, nbins=10):
	h = float(b-a)/nbins
	assert h > 0
	assert type(nbins) == int
	
	s = 0.0
	x = a + h/2
	while (x < b):
		s = s + h * f(x)
		x = x + h
	
	return s

def integTrap(a, b, f, nbins=10):
	h = float(b-a)/nbins
	assert h > 0
	assert type(nbins) == int
	
	s = (h/2) * (f(a) + f(b))
	for n in range(1, nbins):
		s = s + h * f(a + n*h)
	
	return s
