"""import math

N = int(input())

ans = ""

for i in range(2, math.floor(math.sqrt(N-1))):
    while N % i == 0:
        ans += str(i)
        ans += "x"
        N = int(N/i)

if N != 1:
    ans[-1] = str(N)
print(ans)"""

N = int(input())
ans = []

limit = int(N**0.5)
for i in range(2,limit+1):
    while N % i == 0:
        N /= i
        ans.append(i)
if N >= 2:
    ans.append(int(N))
print(*ans)
