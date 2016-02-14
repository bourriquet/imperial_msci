import sys

try:
    F = float(sys.argv[1])

except IndexError:
    print "You failed to provide a command-line arg."
    sys.exit(1)
    
C = (F - 32)*(5./9)

print C
