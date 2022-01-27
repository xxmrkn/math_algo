N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = [0]*M

for i in range(M):
    B[i] = int(input())

D = [0]*N
D[0] = 0

#Aの累積を求める
for i in range(1,N):
    D[i] = D[i-1] + A[i-1]
ans = 0

for i in range(M-1):
    if B[i] < B[i+1]:
        ans += D[B[i+1]-1] - D[B[i]-1]
    else:
        ans += D[B[i]-1] - D[B[i+1]-1]
print(ans)