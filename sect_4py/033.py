import math

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

bax = a[0]-b[0]
bay = a[1]-b[1]
bcx = c[0]-b[0]
bcy = c[1]-b[1]

cax = a[0]-c[0]
cay = a[1]-c[1]
cbx = b[0]-c[0]
cby = b[1]-c[1]

if (bax*bcx+bay*bcy) <0:
    p = 1
elif (cax*cbx+cay*cby) <0:
    p = 3
else:
    p = 2

if p == 1:
    ans = math.sqrt(bax**2+bay**2)
elif p == 3:
    ans = math.sqrt(cax**2+cay**2)
else:
    ans = abs(bax*bcy-bay*bcx)/math.sqrt(bcx**2+bcy**2)
print(ans)