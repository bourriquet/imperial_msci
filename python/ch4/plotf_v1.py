from math import tan, cos
from numpy import *
import matplotlib.pyplot as plt
import sys

min = eval(sys.argv[2])
max = eval(sys.argv[3])

xlist = linspace(min, max, 101)
y = []

for x in xlist:
    y.append(eval(sys.argv[1]))
    
plt.plot(xlist, y)
plt.savefig("tmp.eps")
plt.show()
