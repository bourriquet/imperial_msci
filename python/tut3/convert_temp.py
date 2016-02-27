def C2F(x):
    return (x*9./5) + 32

def F2C(x):
    return (x - 32)*(5./9)

def C2K(x):
    return x + 273.15

def K2C(x):
    return x - 273.15

def F2K(x):
    return C2K(F2C(x))

def K2F(x):
    return C2F(K2C(x))
