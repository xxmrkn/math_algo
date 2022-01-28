l = 1.0
r = 2.0
for i in range(20):
    m = (l+r)/2
    if m**2 <2:
        l = m
    else:
        r = m
    print("Step #%d: m = %.12f" % (i,m))