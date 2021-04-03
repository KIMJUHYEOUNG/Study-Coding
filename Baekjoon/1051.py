def compare(n,m,k):
  for row in range(n-k+1):
        for col in range(m-k+1):
            j = i-1
            if array[row][col] == array[row][col+j] == array[row+j][col] == array[row+j][col+j]:
                print(i**2)
                return True
  return False

n,m = list(map(int,input().split()))

array = [list(map(int,list(input()))) for _ in range(n) ]

k = n if n<m else m
end = 0

for i in range(k,0,-1):
    if compare(n,m,i):
      break
