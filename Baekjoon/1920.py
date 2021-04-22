import sys

def bs(start,end,key):
    if start > end:
        return False
    mid = (start+end) // 2

    if a[mid] == key:
        return True
    elif a[mid] > key:
        return bs(start,mid-1,key)
    else:
        return bs(mid+1,end,key)

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

a.sort()

m = int(input())

b = list(map(int,sys.stdin.readline().split()))
mmax = max(a)
mmin = min(a)
result = 0

for i in range(m):
    if mmax < b[i] or mmin > b[i]:
        print(0)
        continue
    if bs(0,n,b[i]):
        print(1)
    else:
        print(0)
