from math import tan, cos
from numpy import *
import matplotlib.pyplot as plt
import sys

g = 9.81

try:
    y0 = float(sys.argv[1])
    theta = float(sys.argv[2])
    v0 = float(sys.argv[3])

except IndexError:
    print "You didn't supply a command-line argument."

def f(x):
    return (x*tan(theta)) - ((g*(x**2))/(2*(v0**2)*((cos(theta))**2))) + y0

a = - (g/(2*(v0**2)*((cos(theta))**2)))
b = tan(theta)
c = y0

if (-b + sqrt((b**2) - (4*a*c)))/(2*a) > 0:
    xg = (-b + sqrt((b**2) - (4*a*c)))/(2*a)
elif (-b - sqrt((b**2) - (4*a*c)))/(2*a) > 0:
    xg = (-b - sqrt((b**2) - (4*a*c)))/(2*a)

print xg

x = linspace(0,xg,101)
y = f(x)

plt.plot(x,y)
plt.show()
