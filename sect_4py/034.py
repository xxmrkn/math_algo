import math

N = int(input())
x = [0 for i in range(N)]
y = [0 for i in range(N)]
for i in range(N):
    x[i],y[i] = map(int, input().split())

ans = []

for i in range(N):
    for j in range(N):
        if j == i:
            continue
        else:
            dist = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            ans.append(dist)
print(min(ans))