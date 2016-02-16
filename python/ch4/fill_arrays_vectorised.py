from numpy import *

def f(x):
    return (1./(2*pi))*exp(0.5*(x**2))

x = linspace(-4,4,101)
h = f(x)
