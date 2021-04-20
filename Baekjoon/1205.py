import sys

def main():
    n,m,p = list(map(int,input().split()))

    score = list(map(int,sys.stdin.readline().split()))
    
    ranking = [ i+1 for i in range(n+1)]

    if n == 0:
        print(1)
        return
    
    score.append(m)
    score.sort(reverse = True)
    
    idx = score.index(m)
    if idx + 1 > p:
        print(-1)
        return
    elif score[-1] == m and n == p:
        print(-1)
        return

    print(score.index(m)+1)

if __name__ == "__main__":
    main()
