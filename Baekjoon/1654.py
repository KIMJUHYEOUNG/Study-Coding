def get_len(val):
    result = 0
    for i in l:
        result += i // val
    return result

k,n = list(map(int,input().split()))

l = [int(input()) for _ in range(k) ]

start, end = 1,max(l)

while start <= end:
    mid = (start+end) // 2
    numbers = get_len(mid)
    if numbers < n:
        end = mid-1
    else:
        start = mid+1
print(end)
