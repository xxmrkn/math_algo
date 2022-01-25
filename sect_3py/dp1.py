N = int(input())
h = list(map(int, input().split()))

dp = [None]*N
dp[0] = 0

for i in range(1,N):
    if i == 1:
        dp[i] = abs(h[i - 1] - h[i])
    if i >= 2:
        s1 = dp[i-1]+ abs(h[i-1]-h[i])
        s2 = dp[i-2]+ abs(h[i-2]-h[i])
        dp[i] = min(s1,s2)
print(dp[N-1])
