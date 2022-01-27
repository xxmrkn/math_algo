N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [0]*Q
R = [0]*Q

for i in range(Q):
    L[i], R[i] = map(int, input().split())

B = [0]*(N+1)
B[0] = 0

#累積
for j in range(N):
    B[j+1] = B[j] + A[j]
#print(B)
for i in range(Q):
    print(B[R[i]]-B[L[i]-1])