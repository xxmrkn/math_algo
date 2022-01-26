x1,y1,r1 = map(float,input().split())
x2,y2,r2 = map(float,input().split())

dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

if dist < abs(r1-r2):
    print('1')
elif dist == abs(r1-r2):
    print('2')
elif r1 + r2 > dist:
    print(3)
elif r1 + r2 == dist:
    print(4)
else:
    print(5)

"""if r1 > r2:
    if r1 > dist:
        print(1)
    elif dist + r2 == r1:
        print(2)
    elif r1 + r2 > dist:
        print(3)
    elif r1 + r2 == dist:
        print(4)
    else:
        print(5)
elif r1 < r2:
    if r2 > dist:
        print(1)
    elif dist + r1 == r2:
        print(2)
    elif r1 + r2 > dist:
        print(3)
    elif r1 + r2 == dist:
        print(4)
    else:
        print(5)
else:
    print(2)"""