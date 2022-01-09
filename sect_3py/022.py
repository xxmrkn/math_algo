#####TLE#####
"""N = int(input())
A = list(map(int,input().split()))

ans = 0

for i in range(0,N):
    for j in range(i+1,N):
        if A[i] + A[j] == 100000:
            ans +=1
print(ans)"""

N = int(input())
A = list(map(int,input().split()))


#全探索だとTLEなので，A中の数値の箇所のみに個数のフラグを立てた配列cntを作る
cnt = [0 for i in range(10)]
for i in range(N):
    cnt[A[i]] += 1

ans = 0
for i in range(1,5):
    ans += cnt[i] * cnt[10 - i]
#公式
ans += cnt[5] * (cnt[5] - 1)//2

print(ans)