#ミスって最小公倍数求めるやつ書いてしまった
def GCD(A,B):
    while A >= 1 and B >= 1:
        if A > B:
            A = A%B
        else:
            B = B%A
    if A >= 1:
        return A
    return B

N = int(input())
A = list(map(int, input().split()))

ans = GCD(A[0],A[1])

def LCM(ans):
    total = 1

    for j in A:
        total *= j
    return total/ans

for i in range(2,N):
    ans = GCD(ans,A[i])

ans2 = LCM(ans)

print(ans2)

##########################################
#N個の数値の最小公約数を表示する

# 最大公約数を返す関数
def GCD(A, B):
	while A >= 1 and B >= 1:
		if A < B:
			B = B % A  # A < B の場合、大きい方 B を書き換える
		else:
			A = A % B  # A >= B の場合、大きい方 A を書き換える
	if A >= 1:
		return A
	return B

# 最小公倍数を返す関数
def LCM(A, B):
	return int(A / GCD(A, B)) * B

# 入力
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
R = LCM(A[0], A[1])
for i in range(2, N):
	R = LCM(R, A[i])

# 出力
print(R)
