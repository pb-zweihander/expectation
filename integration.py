
from __future__ import division
from math import *

def z(x):
	return pow(e, (0-(x*x))/2)/sqrt(2*pi)

def sigma(f, a, b):
	s = 0.0
	
	x = a
	while(x <= b):
		s = s + f(x)
		x = x + 1

	return s

def integLeft(f, a, b, nbins=10):
	h = float(b-a)/nbins
	assert h > 0
	assert type(nbins) == int
	
	s = 0.0
	for n in range(nbins):
		s = s + h * f(a + n*h)
	
	return s


def integMid(f, a, b, nbins=10):
	h = float(b-a)/nbins
	assert h > 0
	assert type(nbins) == int
	
	s = 0.0
	x = a + h/2
	while (x < b):
		s = s + h * f(x)
		x = x + h
	
	return s

def integTrap(f, a, b, nbins=10):
	h = float(b-a)/nbins
	assert h > 0
	assert type(nbins) == int
	
	s = (h/2) * (f(a) + f(b))
	for n in range(1, nbins):
		s = s + h * f(a + n*h)
	
	return s

