def isprime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
        return True

N = int(input())
if isprime(N):
    print("prime")
else:
    print("not prime")