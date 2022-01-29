N, M = map(int, input().split())
A = [0 for i in range(M)]
B = [0 for i in range(M)]
for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [ list() for i in range(N+1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

ans = 0

for i in range(1, N+1):
    cnt = 0
    for j in G[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)