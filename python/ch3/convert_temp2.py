from convert_temp import *
import sys

try:
    T = float(sys.argv[1])
    U = sys.argv[2]

except IndexError:
    print "You failed to provide a command-line arg."
    sys.exit(1)
    
if (U == "K"):
    print K2C(T), "C"
    print K2F(T), "F"
elif (U == "C"):
    print C2F(T), "F"
    print C2K(T), "K"
elif (U == "F"):
    print F2C(T), "C"
    print F2K(T), "K"
