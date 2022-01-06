def GCD(A,B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B
    if A >= 1:
        return A
    return B

N = int(input())
A = list(map(int, input().split()))

ans = GCD(A[0],A[1])
for i in range(2, N):
    ans = GCD(ans, A[i])

print(ans)