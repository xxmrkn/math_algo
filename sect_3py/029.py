N = int(input())

dp = [None]* (N+1)
dp[0]=1

for i in range(1,N+1):
    if i == 1:
        dp[i] = 1
    if i >= 2:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N])