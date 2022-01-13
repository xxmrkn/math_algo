import random

N = int(input())
M = 0

for i in range(1,N+1):
    px = random.random()
    py = random.random()
    #原点からの距離はsqrt(px * px + py * py)
    #これが1以下であればいいので、条件は「px * px + py * py　<= 1」
    if px * px + py * py <= 1.0:
        M += 1

print("%.12f" % (4*M/N))
