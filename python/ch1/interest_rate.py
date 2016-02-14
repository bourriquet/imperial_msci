A = 1000
p = 0.05
n = 3

money = A * (1 + (p/100))**n

print "%g euros has grown to %.2f euros after %g years with a %g interest rate" %(A, money, n, p)
