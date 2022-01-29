N = int(input())

a = [0 for i in range(N+1)]
a[1] = 1
a[2] = 1


for i in range(3,N+1):
    a[i] = (a[i-1]+a[i-2])%1000000007

print(a[N])