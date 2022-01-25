N = int(input())

dp = [None]*(N+1)
dp[0]= 1

for i in range(1,N+1):
    if i == 1:
        dp[i] = 1
    elif i >=2:
        dp[i] = dp[i-2] + dp[i-1]
print(dp[N])