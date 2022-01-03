#N以下の約数を小さい順に列挙
import math

N = int(input())

l = []

for i in range(1, math.floor(math.sqrt(N))):
    if N % i == 0:
        l.append(int(i))
        if N/i != i:
            l.append(int(N/i))
l.sort()
for i in l:
    print(i)

"""# このプログラムは、コード 3.1.3 とは異なり、約数を小さい順に出力するプログラムとなっています。

# 入力
N = int(input())

# すべての約数を求め、配列 divisors に入れる
LIMIT = int(N ** 0.5)
divisors = []
for i in range(1, LIMIT + 1):
	if N % i == 0:
		divisors.append(i)
		if i != N // i:
			divisors.append(N // i)

# 小さい順に並べ替え → 出力
# sort は小さい順に並べ替える関数です（3.6.1 項で扱います）
divisors.sort()
for i in divisors:
	print(i)"""