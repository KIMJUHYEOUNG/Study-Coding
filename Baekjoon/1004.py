t = int(input())

for _ in range(t):
  
  sx,sy,dx,dy = list(map(int,input().split()))
  n = int(input())
  result = 0

  for i in range(n):
    cnt1,cnt2 = 0,0
    px,py,r = list(map(int,input().split()))
    
    if pow((sx-px),2) + pow((sy-py),2)< r*r:
        cnt1 += 1
    if pow((dx-px),2) + pow((dy-py),2) < r*r:
        cnt2 += 1
    result += abs(cnt1-cnt2)
  print(result)
