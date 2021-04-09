t = int(input())

init_zero = [1,0]
init_one = [0,1]

n = []
for _ in range(t):
    n.append(int(input()))
    
mmax = max(n)

for i in range(2,mmax+1):
    init_zero.append(init_one[i-1])
    init_one.append(init_zero[i-1]+init_zero[i])

for i in range(t):
    print(init_zero[n[i]],end=" ")
    print(init_one[n[i]])
