from numpy import *
import matplotlib.pyplot as plt
import sys

try:
    function = str(sys.argv[1])
    min = eval(sys.argv[2])
    max = eval(sys.argv[3])
except IndexError, TypeError:
    print "Command-line arguments of the wrong type or not provided"
    sys.exit(1)

try:
    r = eval(sys.argv[4])
except:
    r = 501

xlist = linspace(min, max, r)
y = []

for x in xlist:
    y.append(eval(function))
    
plt.plot(xlist, y)
plt.savefig("tmp.eps")
plt.show()
