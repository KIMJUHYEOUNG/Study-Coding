def seaching(x,y,stump):
    get_stump = 0
    stump_idx = abs(stump-1)
    for i in range(8):
        for j in range(8):
            stump_idx = abs(stump_idx-1)
            if s[x+i][y+j] != set_stump[stump_idx]:
                get_stump += 1
        stump_idx = abs(stump_idx-1)
    return get_stump

set_stump = ['B','W']

n,m = list(map(int,input().split()))

s = [list(input()) for _ in range(n) ]

mmin = 1000
for i in range(n-7):
    for j in range(m-7):
        find_val = seaching(i,j,0)
        if mmin > find_val:
            mmin = find_val
        find_val = seaching(i,j,1)
        if mmin > find_val:
            mmin = find_val
        
print(mmin)
        
