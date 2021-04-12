def main():
    n,k = list(map(int,input().split()))
    cnt = 0
    
    while bin(n).count("1") > k:
        n += 1
        cnt += 1
    print(cnt)
        
if __name__=="__main__":
    main()
