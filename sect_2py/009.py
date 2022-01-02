#bit全探索
N, S = map(int, input().split())
A = list(map(int, input().split()))

ans = 'No'

for i in range(0, 1 << N):
    partsum = 0
    for j in range(0, N):
        if (i & (1 << j)) != 0:
            partsum += A[j]
    if partsum == S:
        ans = 'Yes'
        break
print(ans)