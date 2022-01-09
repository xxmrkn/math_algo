N = int(input())
A = list(map(int, input().split()))

a=0
b=0
c=0
d=0

for i in A:
    if i == 100:
        a += 1
    elif i == 200:
        b += 1
    elif i == 300:
        c += 1
    else:
        d += 1

print(a*d + b*c)
