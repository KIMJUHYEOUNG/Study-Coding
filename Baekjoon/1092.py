def main():
    n = int(input())
    crain = list(map(int,input().split()))

    m = int(input())
    box = list(map(int,input().split()))

    sel = [0 for _ in range(n)]
    
    crain.sort(reverse=True); box.sort(reverse=True)
    
    if crain[0] < box[0]:
        print(-1)
        return 0
    
    cnt = 0
    while len(box):
        cnt += 1
        for c in crain:
            for b in range(len(box)):
                if box[b] <= c:
                    box.pop(b)
                    break
    print(cnt)
if __name__=="__main__":
    main()
    
