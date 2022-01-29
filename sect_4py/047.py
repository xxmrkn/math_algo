import sys

N, M = map(int, input().split())
A = [0 for i in range(M)]
B = [0 for i in range(M)]

for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [list() for i in range(N+1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

def dfs(pos, G, color):
    for i in G[pos]:
        if color[i] == 0:
            color[i] = 3-color[pos]
            dfs(i, G, color)
