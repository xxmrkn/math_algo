N, S = map(int,input().split())
A = list(map(int, input().split()))

INF = 10**5
dp = [[None]*(S+1) for i in range(N+1)]
dp[0][0] = True
for i in range(1,S+1):
    dp[0][i] = False
print(dp)

for i in range(1,N+1):
    for j in range(0,S+1):
        if j < A[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            if (dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True):
                dp[i][j] = True
            else:
                dp[i][j] = False
if dp[N][S] == True:
    print("Yes")
else:
    print("No")