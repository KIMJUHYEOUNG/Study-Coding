def get_han(m):
    l = str(m)
    length = len(l)
    if length < 2:
        return True
    c = int(l[1])-int(l[0])
    
    for i in range(2,length):
        if int(l[i]) - int(l[i-1]) != c:
            return False
    return True
        

n = int(input())

k = [0] *  1001

for i in range(1,1001):
    if get_han(i):
        k[i] += k[i-1] + 1
    else:
        k[i] = k[i-1]

print(k[n])
