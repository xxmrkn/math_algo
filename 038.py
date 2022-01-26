N, Q = map(int,input().split())
A = list(map(int, input().split()))
L = [0]*Q
R = [0]*Q
B = [0]*(N+1)

B[0] = 0

for i in range(Q):
    L[i],R[i] = map(int, input().split())

for i in range(N):
    B[i+1] = B[i] + A[i]

for j in range(Q):
    print(B[R[j]]-B[L[j]-1])