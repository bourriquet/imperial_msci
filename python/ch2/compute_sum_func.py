def s(M):
    s = 0
    for i in range(1,(M+1),1):
        s += 1./i
    return s

print s(100)
