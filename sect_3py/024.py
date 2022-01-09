N = int(input())
E = 0
for i in range(N):
    P,Q = map(int,input().split())
    E += 1/P * Q

print(E)