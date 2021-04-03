def stump(loc,row,col):
    bug = False
    if row-1 >= 0 and loc[row-1][col]:
        loc[row-1][col] = 0
        stump(loc,row-1,col)
        bug = True
    if col-1 >= 0 and loc[row][col-1]:
        loc[row][col-1] = 0
        stump(loc,row,col-1)
        bug = True
    if row+1 < n and loc[row+1][col]:
        loc[row+1][col] = 0
        stump(loc,row+1,col)
        bug = True
    if col+1 < m and loc[row][col+1]:
        loc[row][col+1] = 0
        stump(loc,row,col+1)
        bug = True
    return bug

t = int(input())
import sys
sys.setrecursionlimit(50*50)

for _ in range(t):
    n,m,k = list(map(int,input().split()))
    array = [[0 for i in range(m)] for j in range(n) ]
    result = 0
    for i in range(k):
        row,col = list(map(int,input().split()))
        array[row][col] = 1
    for i in range(n):
        for j in range(m):
            if array[i][j]:
                stump(array,i,j)
                result += 1
    print(result)
    
