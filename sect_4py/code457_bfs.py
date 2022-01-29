#BFS
import queue

N, M = map(int, input().split())
A = [ None ]*M
B = [ None ]*M
for i in range(M):
    A[i],B[i] = map(int, input().split())

G = [ list() for i in range(N+1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

#BFSの初期化
dist = [-1]*(N+1)
Q = queue.Queue()
dist[1] = 0
Q.put(1)

while not Q.empty():#Queueが空じゃない間続ける
    pos = Q.get()#Queueの先頭の値を取得
    for nex in G[pos]:#先頭の値の隣接リストの値を取り出す
        if dist[nex] == -1:#もしその頂点のdistが-1なら
            dist[nex] = dist[pos] + 1#距離に1を足す
            Q.put(nex)

for i in range(1, N+1):
    print(dist[i])



