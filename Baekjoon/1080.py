def main():
    n,m = list(map(int,input().split()))

    a = [ list(map(int,input())) for _ in range(n)]

    b = [ list(map(int,input())) for _ in range(n)]
    
    if n < 3 or m < 3:
        if a == b:
            print(0)
        else:
            print(-1)
        return
    cnt = 0
    for i in range(0,n-2):
        for j in range(0,m-2):
            if a[i][j] != b[i][j]:
                a[i][j] = abs(a[i][j]-1)
                a[i][j+1] = abs(a[i][j+1]-1)
                a[i][j+2] = abs(a[i][j+2]-1)
                a[i+1][j] = abs(a[i+1][j]-1)
                a[i+1][j+1] = abs(a[i+1][j+1]-1)
                a[i+1][j+2] = abs(a[i+1][j+2]-1)
                a[i+2][j] = abs(a[i+2][j]-1)
                a[i+2][j+1] = abs(a[i+2][j+1]-1)
                a[i+2][j+2] = abs(a[i+2][j+2]-1)
                cnt += 1
    for i in range(n):
        if a[i] != b[i]:
            print(-1)
            return
    print(cnt)

            
if __name__=="__main__":
    main()
