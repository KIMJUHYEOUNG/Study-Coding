n = int(input())

book = [ input() for _ in range(n) ]

best = []

for i in book:
    key = False
    for j in range(len(best)):
        if i == best[j][0]:
            best[j][1] += 1
            key = True
    if not key:
        best.append([i,1])
best = sorted(best, key = lambda x:x[0])
best = sorted(best, key = lambda x:x[1], reverse = True)

print(best[0][0])
