#!/usr/bin/python

from __future__ import division
from integration import *
import math

xbar = 75
s = 4
n = 64

for za in range(100, 451, 1):
	exp = round(integTrap(0, za/100, z, 1000)*2, 6)
	mp = round(xbar + ((za/100) * (s/math.sqrt(n))), 4)
	mn = round(xbar - ((za/100) * (s/math.sqrt(n))), 4)
	print("%s, %s%% : [%s, %s]" % (za/100, exp*100, mn, mp))
