N, S = map(int, input().split())
cnt = 0

for i in range(1,N+1):
    for j in range(1, N+1):
        if i+j <= S:
            cnt += 1
print(cnt)