#!/usr/bin/python

from expectation import *

dic = getExpectation(xbar=0, s=1, n=100, a=0.01, b=5, nbins=500, pr=True, pl=True, sh=True, plfn='result.png')

