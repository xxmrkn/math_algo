N, Q = map(int, input().split())
L = [0]*Q
R = [0]*Q
X = [0]*Q
B = [0]*(N+2)

for i in range(Q):
    L[i], R[i], X[i] = map(int, input().split())

B[0] = 0

#階差
for i in range(1,Q+1):
    B[L[i-1]] += X[i-1]
    B[R[i-1]+1] -= X[i-1]

ans =''

#判定
for i in range(1, N):
    if B[i+1] > 0:
        ans +='<'
    elif B[i+1] == 0:
        ans +='='
    else:
        ans +='>'

print(ans)