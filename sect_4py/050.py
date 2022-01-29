#TLE
"""a, b = map(int, input().split())

ans = 1

for i in range(1,b+1):
    ans = (ans*a)%1000000007
print(ans)"""

"""def modpow(a,b,m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans*p)%m
        p = (p*p)%m
    return ans

MOD = 1000000007

a, b = map(int, input().split())
print(modpow(a,b,MOD))"""

a, b = map(int, input().split())
print(pow(a, b, 1000000007)) # pow(a, b, m) は、a**b を m で割った余りを返す関数