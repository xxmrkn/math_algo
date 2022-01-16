"""import random

N = 100000
M = 0

for i in range(N):
    px = 6.0 * random.random()
    py = 9.0 * random.random()
    dist_33 = ((px-3.0)*(px-3.0)+(py-3.0)*(py-3.0)) ** 0.5
    dist_37 = ((px-3.0)*(px-3.0)+(py-7.0)*(py-7.0)) ** 0.5

    if(dist_33 <= 3.0 or dist_37 <= 2.0):
        M+=1
print(M)"""

S = 54
p = 71908/100000
print(54*p)