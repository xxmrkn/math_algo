A, B = map(int, input().split())

def GCD(A,B):
    if B == 0:
        return A
    return GCD(B, A%B)
print(GCD(A,B))