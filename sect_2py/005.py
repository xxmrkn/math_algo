N = int(input())
n = list(map(int, input().split()))

cnt = 0

for i in n:
    cnt += i
ans = cnt % 100
print(ans)