n,m = list(map(int,input().split()))

s = [list(map(int,input())) for _ in range(n) ]

k = int(input())

result = -1

for i in range(n):
    zerosum = m - sum(s[i])
    cnt = 0
    if zerosum <= k and zerosum % 2 == k % 2:
        for j in range(n):
            if s[i] == s[j]:
                cnt += 1
    result = max(result,cnt)
print(result)
