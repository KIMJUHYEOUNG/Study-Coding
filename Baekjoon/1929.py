m,n = list(map(int,input().split()))

s = [True] * (n+1)
s[0],s[1] = False,False

for i in range(2,n+1):
    if not s[i]:
        continue
    for j in range(i*2,n+1,i):
        s[j] = False

for i in range(m,n+1):
    if s[i]:
        print(i)
