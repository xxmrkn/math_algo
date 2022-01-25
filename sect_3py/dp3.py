N, W = map(int, input().split())
w = [None]*(N)
v = [None]*(N)
for i in range(N):
    w[i],v[i] = map(int, input().split())

INF = 10**18
dp = [[None] * (W+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(1,W+1):
    dp[0][i] = -INF

for i in range(1,N+1):
    for j in range(0,W+1):     
        if j < w[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
ans = max(dp[N])
print(ans)
