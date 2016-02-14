from math import exp, pi, sqrt

m = 0.
s = 2.
x = 1.

gauss = (1/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)

print gauss
