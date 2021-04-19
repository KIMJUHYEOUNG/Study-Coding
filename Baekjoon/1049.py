n,m = list(map(int,input().split()))

f = [ list(map(int,input().split())) for _ in range(m) ]

package = sorted(f,key = lambda x:x[0])
each = sorted(f,key = lambda x:x[1])

package = int(package[0][0])
each = int(each[0][1])

result = 0
if package < 6 * each:
    result = n // 6 * package
else:
    result = n // 6 * 6* each

n %= 6

if n * each >= package:
    result += package
else:
    result += n * each

print(result)
