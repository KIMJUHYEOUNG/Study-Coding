from itertools import combinations

l,c = list(map(int,input().split()))

alphabet = list(map(str,input().split()))

alphabet.sort()

for i in combinations(alphabet,l):
    cnt = 0
    for j in i:
        if j in ['a','e','i','o','u']:
            cnt += 1
    if cnt >= 1 and cnt <= l-2:
        print("".join(i))
