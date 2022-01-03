"""A = input()
l = len(A)-1
a = A[0]
ans = 0
ans1 = 1

for i in range(1 << l):
    for j in range(l):
        if (i & (1 << j)):
            a += "+"
        #if (i & (1 << j)):
        #    a += "-"
        a += A[j+1]
        a += ''
    print(a)
    ans += sum(map(int, a.split("+")))
    #print(a)
    #ans1 += sum(map(int, a.split("-")))

    if ans == 7:
        print(f'{ans}=7')
        #print(f'{ans1}=7')
        break"""
abcd = input() #4つの数字をstr型で入力
l = len(abcd)  # l=4

for bit in range(1 <<  l - 1):
    N = abcd[0]
    for i in range(l-1):
        N += ' '
        if (bit & (i << 1)):
            N += '-'
        else:
            N += '+'
        N += abcd[i +1]
        N += ' '
    #print(N)
    N_int = sum(map(int, N.split()))
    #print(N_int)
    if N_int == 7:
        #ans = list(map(str, N.split()))
        ans = N.replace(' ', '')
        print('{}=7'.format(ans))
        break