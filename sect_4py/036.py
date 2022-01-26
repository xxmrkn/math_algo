import math
A, B, H, M = map(float, input().split())


PI = 3.14159265358979
hx= A*math.cos((30.0*H + 0.5*M)*PI/180.0)
hy = A*math.sin((30.0*H + 0.5*M)*PI/180.0)
mx = B*math.cos(6.0*M*PI/180.0)
my = B*math.sin(6.0*M*PI/180.0)

#時針は1時間に30度と0.5*分進む・分針は1分に6度進む

d = ((hx-mx)**2 + (hy-my)**2)**0.5

print("%.12f" %d)