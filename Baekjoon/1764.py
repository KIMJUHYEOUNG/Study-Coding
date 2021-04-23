n,m = list(map(int,input().split()))

a = [ input() for _ in range(n) ]
b = [ input() for _ in range(m) ]

a = set(a)
b = set(b)

arr = list(a&b)
arr.sort()
print(len(arr))
for i in arr:
    print(i)
