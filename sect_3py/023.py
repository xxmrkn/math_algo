N = int(input())
B = list(map(int,input().split()))
R = list(map(int,input().split()))

BE = 0
RE = 0

for i in B:
    BE += 1/N * i
for i in R:
    RE += 1/N * i

print(BE + RE)
