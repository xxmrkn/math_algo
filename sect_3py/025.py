N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

for i in range(N):
    ans += (1.0/3.0)*A[i] + (2.0/3.0)*B[i]
print(ans)