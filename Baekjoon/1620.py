n,m = list(map(int,input().split()))

poke = {}
for i in range(1,n+1):
	name = input()
	poke[name] = i
	poke[str(i)] = name


for _ in range(m):
    q = input()
    print(poke[q])
