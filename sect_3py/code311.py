#2からn-1まで割り切れるか確かめる O(N)

n = int(input())
bool = True
for i in range(2, n-1):
    if n % i == 0:
        bool = False
print(bool)