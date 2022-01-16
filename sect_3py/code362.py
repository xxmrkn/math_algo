N = int(input())
A = list(map(int, input().split()))

"""for i in range(N):
    min = A[i]
    for j in range(i+1,N):
        min2 = A[j]
        if min > min2:
            min = min2"""
for i in range(N-1):
    min_pos = i
    min_value = A[i]
    for j in range(i + 1, N):
        if min_value > A[j]:
            min_pos = j
            min_value = A[j]
    A[i], A[min_pos] = A[min_pos], A[i]
print(*A)