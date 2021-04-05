def seaching(j):
    for k in num[j]:
        if temp[k]:
            return False
    return True

num = [[] for _ in range(10)]
num[0] = [4,7,10]
num[1] = [0,1,3,4,6,7,9,10,12,13]
num[2] = [3,4,10,11]
num[3] = [3,4,9,10]
num[4] = [1,4,9,10,12,13]
num[5] = [4,5,9,10]
num[6] = [4,5,10]
num[7] = [3,4,6,7,9,10,12,13]
num[8] = [4,10]
num[9] = [4,9,10]

n = int(input())

r = []

for _ in range(5):
    r.append(input())
    
number = []
for i in range(n):
    i *= 4
    temp = []
    for j in range(5):
        for k in range(3):
            m = 0
            if r[j][i+k] == '#':
                m = 1
            temp.append(m)
    store = []
    for j in range(10):
        if seaching(j):
            store.append(j)
    number.append(store)

result = []
d = 1
for arr in reversed(number):
    if not len(arr):
        result = [-1]
        break
    total = 0
    for i in arr:
        total += i*d
    result.append(total/len(arr))
    d *= 10
    
print(sum(result))
