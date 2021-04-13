def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b =  list(map(int,input().split()))

p = gcd(a,b)

print('1'*p)
