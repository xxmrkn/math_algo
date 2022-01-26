N, Q = map(int,input().split())
L = [0]*Q
R = [0]*Q
X = [0]*Q
B = [0]*(N+2)

for i in range(Q):
    L[i],R[i],X[i] = map(int, input().split())

for i in range(Q):
    B[L[i]] += X[i]
    B[R[i]+1] -= X[i]

answer = ""
for i in range(2, N + 1):
	if B[i] > 0:
		answer += "<"
	if B[i] == 0:
		answer += "="
	if B[i] < 0:
		answer += ">"
print(answer)