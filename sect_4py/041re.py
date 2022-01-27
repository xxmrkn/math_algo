T = int(input())
N = int(input())

L = [0 for i in range(N)]
R = [0 for i in range(N)]

for i in range(N):
    L[i], R[i] = map(int, input().split())

A = [0 for i in range(T+2)]
B = [0 for i in range(T+2)]

for i in range(N):
    B[L[i]] += 1
    B[R[i]] += -1

A[0] = B[0]
for i in range(1,T):
    A[i] = A[i-1] + B[i]

for i in range(T):
    print(A[i])