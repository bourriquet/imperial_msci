from numpy import linspace
from math import pi, exp, sqrt

xlist = linspace(-4,4,101)
hlist = [(1./(2*pi))*exp(0.5*(i**2)) for i in xlist]
