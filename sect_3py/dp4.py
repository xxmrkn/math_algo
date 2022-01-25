N = int(input())
A = list(map(int, input().split()))

dp1 = [0]*(N+1)
dp2 = [0]*(N+1)

for i in range(1,N+1):
        dp1[i] = dp2[i-1]+A[i-1]
        dp2[i] = max(dp1[i-1],dp2[i-1])
print(max(dp1[N],dp2[N]))