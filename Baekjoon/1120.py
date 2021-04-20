def strc(n):
    mmax = -1
    for i in range(n+1):
        ta = "$" * i + a + "$" * (n-i)
        cnt = 0
        for j in range(len(ta)):
            if ta[j] == b[j] or ta[j] == "$":
                cnt += 1
        mmax = max(mmax,cnt)
    return mmax

a,b = input().split()

length = len(b) - len(a)

if length == 0:
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
else:
    print(len(b)-strc(length))
