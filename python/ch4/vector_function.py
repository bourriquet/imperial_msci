from numpy import *

v = [2,3,-1]

def f(x):
    return (x**3) + (x*exp(x)) + 1

for i in v:
    print f(i)
    
# find out what vector computing rules are
