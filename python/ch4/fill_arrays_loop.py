from numpy import *

x = zeros(101)
h = zeros(101)

for i in range(0,101,1):
    x[i] = -4 + (i*(8./100))
    h[i] = (1./(2*pi))*exp(0.5*(x[i]**2))
