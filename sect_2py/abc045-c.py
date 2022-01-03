S = input()
l = len(S) - 1

ans = 0

for i in range(1 << l):
    s = S[0]
    for j in range(l):
        if (i & (1 << j)):
            s += "+"
        s += S[j + 1]
    ans += sum(map(int, s.split('+')))
print(ans)
