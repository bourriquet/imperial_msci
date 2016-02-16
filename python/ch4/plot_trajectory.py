from numpy import *
import matplotlib.pyplot as plt
import sys

# define constants
g = 9.81

# try getting command-line arguments
try:
    y0 = float(sys.argv[1])
    theta = float(sys.argv[2])
    v0 = float(sys.argv[3])
except IndexError:
    print "You didn't supply a command-line argument."

# compute trajectory
def f(x):
    return (x*tan(theta)) - ((g*(x**2))/(2*(v0**2)*((cos(theta))**2))) + y0

# find roots of trajectory, but are only interested in positive root (other root has to be negative as we start at x = 0)
a = - (g/(2*(v0**2)*((cos(theta))**2)))
b = tan(theta)
c = y0

if (-b + sqrt((b**2) - (4*a*c)))/(2*a) > 0:
    xg = (-b + sqrt((b**2) - (4*a*c)))/(2*a)
elif (-b - sqrt((b**2) - (4*a*c)))/(2*a) > 0:
    xg = (-b - sqrt((b**2) - (4*a*c)))/(2*a)

# plot the trajectory
x = linspace(0,xg,101)
y = f(x)

plt.plot(x,y)
plt.show()
