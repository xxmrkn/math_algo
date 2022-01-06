#1からmin(A,B)まで計算するのは時間がかかるので
#大きい方の数を「大きい数を小さい数で割ったあまり」に置き換える作業を繰り返す
#どちらかが0になった時のもう片方の数が最大公約数である
#ユークリッドの互除法という、計算量はO(log(A+B))
A, B = map(int, input().split())

while (A >= 1 and B >=1):
    if A > B:
        A = A % B
    else:
        B = B % A
print(max(A,B))