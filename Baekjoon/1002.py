import math

t = int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split()))

    xy = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if not xy:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2 == xy or abs(r1-r2) == xy:
            print(1)
        elif xy < r1+r2 and abs(r1-r2) < xy:
            print(2)
        else:
            print(0)
