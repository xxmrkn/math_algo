N = int(input())
A = list(map(int, input().split()))
#5,8,2
M = int(input())
B = [0]*M

for i in range(M):
    B[i] = int(input())
    #2,3,4,3

S = [0 for i in range(N)]
for i in range(1,N):
    S[i] = S[i-1] + A[i-1]

ans = 0
for i in range(M-1):
    if B[i] < B[i+1]:
        ans += S[B[i+1]-1] - S[B[i]-1]
    else:
        ans += S[B[i]-1] - S[B[i+1]-1]
print(ans)