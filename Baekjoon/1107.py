import sys
input = sys.stdin.readline
def check(k):
    k = list(str(k))
    for i in k:
        if i in b:
            return False
    return True

n = int(input())
m = int(input())
b = list(input().strip())
    
mmin = abs(100-n)
for i in range(1000001):
    if check(i):
        mmin = min(mmin,abs(n-i)+len(str(i)))
print(mmin)

# 처음에는 사용가능한 숫자만 받은 후에 모든 중복 순열로 해결하려했으나 실패...
# iteration 라이브러리를 사용해야하며 코드가 길어짐

# 따라서 모든 가능한 숫자를 표시한 후에 망가진 숫자가 있는 지 확인함.
# 또한 sys.stdin.readline을 사용해야 EOFerror가 안나오므로 기본적으로 사용해야겠음
