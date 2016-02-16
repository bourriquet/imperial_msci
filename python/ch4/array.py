from numpy import *

A = [[0,12,-1],[-1,-1,-1],[11,5,5]]
B = zeros([3,3])

for i in range(0,shape(A)[0],1):
    for j in range(0,shape(A)[1],1):
        x = A[i][j]
        B[i][j] = (x**3) + (x * exp(x)) + 1
        
# apply array expression
