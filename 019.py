N = int(input())
A = list(map(int, input().split()))

x=0
y=0
z=0

for i in A:
    if i == 1:
        x += 1
    elif i == 2:
        y += 1
    else:
        z += 1
print(x,y,z)

ans = (x*(x-1))/2 + (y*(y-1))/2 + (z*(z-1))/2
print(int(ans))