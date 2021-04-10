n,k = list(map(int,input().split()))

key = -1
b = 0
for i in range(k,101):
    b = (i*i-i)//2
    if not (n-b) % i and (n-b) // i >= 0:
        key = i
        arr = [i for i in range((n-b)//key,(n-b)//key + key) ]
        for i in arr:
            print(i,end=" ")
        break

if key < 0:
    print(-1)
