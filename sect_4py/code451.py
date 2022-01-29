#隣接リスト表現

N, M = map(int, input().split())
A = [0 for i in range(M)]
B = [0 for i in range(M)]

for i in range(M):
    A[i], B[i] = map(int, input().split())
    #頂点A[i]とB[i]は隣接している

G = [ list() for i in range(N+1)]
print(G)#Gは空のリスト、各頂点番号と隣接している頂点番号のリスト

for i in range(M):#頂点A[i]とB[i]が隣接しているなら、B[i]とA[i]も隣接している
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

print(G)

for i in range(1,N+1):
    output = str(i) + ': {'
    for j in range(len(G[i])):
        if j >= 1:
            output += ','
        output += str(G[i][j])
    output += '}'
    print(output)