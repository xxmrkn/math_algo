T = int(input())
N = int(input())
L = [0 for i in range(N)]
R = [0 for i in range(N)]

A = [0 for i in range(T + 2)]
B = [0 for i in range(T + 2)]

for i in range(N):
    L[i], R[i] = map(int, input().split())

#階差の計算
for i in range(N):
    B[L[i]]+= 1
    B[R[i]]-= 1

# 累積和 A[i] を計算する
A[0] = B[0]
for i in range(1, T):
	A[i] = A[i - 1] + B[i]

# 出力
for i in range(T):
	print(A[i])