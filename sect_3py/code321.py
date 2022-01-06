#正の整数A,Bの最大公約数を返す関数
#GCDはGreatest Common Divisorの訳
A, B = map(int, input().split())

for i in range(1,min(A,B)+1):
    if A % i == 0 and B % i == 0:
        ans = i
print(ans)