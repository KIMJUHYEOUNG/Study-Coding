n,m = list(map(int,input().split()))

book = list(map(int,input().split()))

left = []
right = []

for i in book:
    if i < 0:
        left.append(i*-1)
    else:
        right.append(i)

left.sort(reverse=True); right.sort(reverse=True)

walk = 0
for i in range(0,len(left),m):
    walk += left[i] * 2
for i in range(0,len(right),m):
    walk += right[i] * 2

left_max = 0
right_max = 0

if len(left):
    left_max = max(left)
if len(right):
    right_max = max(right)

print(walk-max(left_max,right_max))
