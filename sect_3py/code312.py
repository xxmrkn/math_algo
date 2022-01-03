#[n]まで割ってそれ以降は計算しない O(√n)
import math
n = int(input())
bool = True
for i in range(2, math.floor(math.sqrt(n))+1):
    if n % i == 0:
        bool = False
print(f'{n}は素数 : {bool}')