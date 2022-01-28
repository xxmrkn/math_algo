N = int(input())
F = [0 for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,(N//i)+1):
        F[j*i] += 1

ans = 0
for i in range(1,N+1):
    ans += i*F[i]

print(ans)
